from models import User, Task


# Test user registration
def test_register_user(client, session):
    response = client.post('/register', data={
        'username': 'newuser',
        'password': 'password123',
        'confirm': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    user = session.query(User).filter_by(username='newuser').first()
    assert user is not None


# Test task creation
def test_create_task(client, sample_user, session):
    client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    response = client.post('/add', data={
        'title': 'New Task',
        'description': 'Test'
    }, follow_redirects=True)
    assert response.status_code == 200
    task = session.query(Task).filter_by(title='New Task').first()
    assert task is not None


# Test task deletion
def test_delete_task(client, sample_user, sample_task, session):
    client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    task_id = sample_task.id
    response = client.get(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200
    deleted_task = session.query(Task).filter_by(id=task_id).first()
    assert deleted_task is None
