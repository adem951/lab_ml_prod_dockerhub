import os
from datetime import date, timedelta
from models import User, Task
from app import _build_postgres_uri


# Test 1: User password hashing
def test_user_password():
    user = User(username='testuser')
    user.set_password('password123')
    assert user.check_password('password123') is True
    assert user.check_password('wrong') is False


# Test 2: Task overdue detection
def test_task_is_overdue():
    past_task = Task(title='Old', due_date=date.today() - timedelta(days=1), is_completed=False, user_id=1)
    assert past_task.is_overdue() is True
    
    future_task = Task(title='Future', due_date=date.today() + timedelta(days=1), is_completed=False, user_id=1)
    assert future_task.is_overdue() is False


# Test 3: Build PostgreSQL URI from environment
def test_build_postgres_uri():
    os.environ['POSTGRES_USER'] = 'testuser'
    os.environ['POSTGRES_PASSWORD'] = 'testpass'
    os.environ['POSTGRES_HOST'] = 'testhost'
    os.environ['POSTGRES_PORT'] = '5433'
    os.environ['POSTGRES_DB'] = 'testdb'
    
    uri = _build_postgres_uri()
    assert 'testuser' in uri
    assert 'testpass' in uri
    assert 'testhost' in uri
    assert '5433' in uri
    assert 'testdb' in uri
