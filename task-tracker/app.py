import os
from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

APP_TITLE = os.getenv("APP_TITLE", "Personal Task Tracker")
TEAM_NAME = os.getenv("TEAM_NAME", "Team Task-It")

tasks = [
    {"id": 1, "name": "Finish IT-390 project", "completed": False},
    {"id": 2, "name": "Test Docker container", "completed": False}
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        title=APP_TITLE,
        team=TEAM_NAME,
        tasks=tasks
    )

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/add", methods=["POST"])
def add_task():
    name = request.form.get("task", "").strip()

    if name:
        tasks.append({
            "id": max((task["id"] for task in tasks), default = 0) + 1,
            "name": name,
            "completed": False
        })
    return redirect("/")

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    return redirect("/")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
