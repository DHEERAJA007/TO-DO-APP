import pytest
from app import app, db, Task

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.drop_all()
        db.create_all()

        with app.test_client() as client:
            yield client

        db.session.remove()
        db.drop_all()


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_add_task(client):
    response = client.post(
        "/add",
        data={
            "title": "Complete CI/CD Project"
        },
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():
        task = Task.query.first()

        assert task is not None
        assert task.title == "Complete CI/CD Project"
        assert task.completed is False


def test_toggle_task(client):

    with app.app_context():

        task = Task(title="Learn Docker")

        db.session.add(task)
        db.session.commit()

        task_id = task.id

    response = client.get(
        f"/toggle/{task_id}",
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():

        updated_task = Task.query.get(task_id)

        assert updated_task.completed is True


def test_delete_task(client):

    with app.app_context():

        task = Task(title="Delete Me")

        db.session.add(task)
        db.session.commit()

        task_id = task.id

    response = client.get(
        f"/delete/{task_id}",
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():

        deleted_task = Task.query.get(task_id)

        assert deleted_task is None
