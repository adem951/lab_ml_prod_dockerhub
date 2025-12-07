import os
import pytest
from sqlalchemy.orm import scoped_session, sessionmaker
from app import create_app
from extensions import db as _db
from models import User, Task


@pytest.fixture(scope='session')
def app():
    os.environ['POSTGRES_DB'] = 'taskmanager_test'
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture(scope='session')
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    
    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)
    
    db.session = session
    yield session
    
    session.remove()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def sample_user(session):
    user = User(username='testuser')
    user.set_password('password123')
    session.add(user)
    session.commit()
    return user


@pytest.fixture
def sample_task(session, sample_user):
    from datetime import date, timedelta
    task = Task(title='Test Task', due_date=date.today() + timedelta(days=7), user_id=sample_user.id)
    session.add(task)
    session.commit()
    return task


@pytest.fixture(scope='module')
def live_server(app):
    """Start Flask app for E2E tests"""
    import subprocess
    import time
    import signal
    
    # Créer un utilisateur de test dans la base de données
    with app.app_context():
        _db.create_all()
        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(username='testuser').first()
        if not existing_user:
            user = User(username='testuser')
            user.set_password('password123')
            _db.session.add(user)
            _db.session.commit()
    
    # Démarrer Flask en subprocess
    import sys
    env = os.environ.copy()
    env['FLASK_ENV'] = 'development'
    process = subprocess.Popen(
        [sys.executable, 'app.py'],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(3)  # Attendre que le serveur démarre
    
    yield
    
    # Arrêter le serveur
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
