import json
import os
from flask import Flask, render_template, request, redirect

try:
    import redis
except ImportError:
    redis = None

app = Flask(__name__)

APP_TITLE = os.getenv("APP_TITLE", "Personal Task Tracker")
TEAM_NAME = os.getenv("TEAM_NAME", "Team Task-It")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
TASKS_KEY = "task_it:tasks"

default_tasks = [
    {"id": 1, "name": "Finish T-390 project", "completed": False},
    {"id": 2, "name": "Test Docker container", "completed": False},
]

memory_tasks = [dict(t) for t in default_tasks]


def get_redis_client():
    if REDIS_HOST and redis is not None:
        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        if not client.exists(TASKS_KEY):
            client.set(TASKS_KEY, json.dumps(default_tasks))
        return client
    return None


def load_tasks():
    client = get_redis_client()
    if client is not None:
        raw = client.get(TASKS_KEY)
        return json.loads(raw) if raw else []
    return memory_tasks


def save_tasks(updated_tasks):
    global memory_tasks
    client = get_redis_client()
    if client is not None:
        client.set(TASKS_KEY, json.dumps(updated_tasks))
    else:
        memory_tasks = updated_tasks


@app.route("/")
def home():
    return render_template(
        "index.html",
        title=APP_TITLE,
        team=TEAM_NAME,
        tasks=load_tasks(),
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


@app.route("/add", methods=["POST"])
def add_task():
    name = request.form.get("task", "").strip()
    if name:
        current = load_tasks()
        current.append({
            "id": max((t["id"] for t in current), default=0) + 1,
            "name": name,
            "completed": False,
        })
        save_tasks(current)
    return redirect("/")


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    current = load_tasks()
    for task in current:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(current)
    return redirect("/")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
