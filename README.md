# To-Do List Application with CI/CD Pipeline

A modern and responsive **To-Do List Application** built using **Flask** and **SQLite**, featuring task management capabilities such as adding, deleting, and marking tasks as completed. The project is containerized using **Docker** and integrated with a **GitHub Actions CI/CD pipeline** for automated testing and Docker image builds.

## ✨ Features

* Add new tasks
* Delete existing tasks
* Mark tasks as completed/incomplete
* Filter tasks (All, Active, Completed)
* Responsive glassmorphism UI
* Persistent storage using SQLite
* Automated unit testing with Pytest
* Docker containerization
* GitHub Actions CI pipeline for automated testing and image building

## 🛠️ Tech Stack

* Python 3.12
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML5
* Tailwind CSS
* JavaScript
* Docker
* GitHub Actions
* Pytest

## 📁 Project Structure

```
todo-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── test_app.py
├── database.db
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .github/
    └── workflows/
        └── ci.yml
```

## 🚀 Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd todo-app
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open:

```
http://localhost:5000
```

## 🧪 Running Tests

```bash
pytest
```

## 🐳 Running with Docker

Build the image:

```bash
docker build -t todo-app .
```

Run the container:

```bash
docker run -p 5000:5000 todo-app
```

Visit:

```
http://localhost:5000
```

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** to automate the development workflow.

On every push or pull request:

1. Repository checkout
2. Python environment setup
3. Dependency installation
4. Unit test execution using Pytest
5. Docker image build verification

This ensures code quality and deployment readiness before integration.

## 📸 Screenshots

Add screenshots of:

* Home Page
* Task Creation
* Completed Tasks
* Docker Execution
* GitHub Actions Success Workflow

## 📜 License

This project is created for educational and portfolio purposes.
