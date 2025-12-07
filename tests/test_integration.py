from models import User, Task


# Test 1: Register and login flow
def test_register_and_login(client, session):
    # Register new user
    response = client.post('/register', data={
        'username': 'newuser',
        'password': 'password123',
        'confirm': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    user = session.query(User).filter_by(username='newuser').first()
    assert user is not None
    
    # Login with new user
    response = client.post('/login', data={
        'username': 'newuser',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200


# Test 2: Create task via POST
def test_create_task(client, sample_user, session):
    client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    response = client.post('/tasks/new', data={
        'title': 'New Task',
        'description': 'Test'
    }, follow_redirects=True)
    assert response.status_code == 200
    task = session.query(Task).filter_by(title='New Task').first()
    assert task is not None


# Test 3: Toggle task completion
def test_toggle_task(client, sample_user, sample_task, session):
    client.post('/login', data={'username': 'testuser', 'password': 'password123'})
    task_id = sample_task.id
    initial_status = sample_task.is_completed
    
    response = client.post(f'/tasks/{task_id}/toggle', follow_redirects=True)
    assert response.status_code == 200
    
    session.expire_all()
    updated_task = session.query(Task).filter_by(id=task_id).first()
    assert updated_task.is_completed != initial_status
