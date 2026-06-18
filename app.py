
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ----------------------------
# Database Configuration
# ----------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ----------------------------
# Task Model
# ----------------------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


# ----------------------------
# Create Database
# ----------------------------
with app.app_context():
    db.create_all()


# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
def index():

    all_tasks = Task.query.order_by(Task.id.desc()).all()

    tasks = [
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in all_tasks
    ]

    return render_template(
        "index.html",
        tasks=tasks
    )


# ----------------------------
# Add Task
# ----------------------------
@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title")

    if title and title.strip():

        new_task = Task(
            title=title.strip()
        )

        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for("index"))


# ----------------------------
# Toggle Complete
# ----------------------------
@app.route("/toggle/<int:id>")
def toggle_task(id):

    task = Task.query.get_or_404(id)

    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("index"))


# ----------------------------
# Delete Task
# ----------------------------
@app.route("/delete/<int:id>")
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return redirect(url_for("index"))


# ----------------------------
# Edit Task
# ----------------------------
@app.route("/edit/<int:id>", methods=["POST"])
def edit_task(id):

    task = Task.query.get_or_404(id)

    new_title = request.form.get("title")

    if new_title and new_title.strip():

        task.title = new_title.strip()

        db.session.commit()

    return redirect(url_for("index"))


# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )