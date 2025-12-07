import os
import pytest
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
    session = db.create_scoped_session(options={"bind": connection})
    db.session = session
    yield session
    transaction.rollback()
    connection.close()
    session.remove()


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
