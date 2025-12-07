from datetime import date, timedelta
from models import User, Task


# Test password hashing
def test_user_password():
    user = User(username='testuser')
    user.set_password('password123')
    assert user.check_password('password123') is True
    assert user.check_password('wrong') is False


# Test task overdue detection
def test_task_is_overdue():
    past_task = Task(title='Old', due_date=date.today() - timedelta(days=1), is_completed=False, user_id=1)
    assert past_task.is_overdue() is True
    
    future_task = Task(title='Future', due_date=date.today() + timedelta(days=1), is_completed=False, user_id=1)
    assert future_task.is_overdue() is False


# Test task without due date
def test_task_no_due_date():
    task = Task(title='No date', due_date=None, is_completed=False, user_id=1)
    assert task.is_overdue() is False
