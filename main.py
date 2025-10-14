from flask import Flask, jsonify, request
from controllers.todo_controller import ToDoController

def create_app():
    app = Flask(__name__)
    todo = ToDoController()

    def tasks_with_index():
        tasks = todo.list_tasks()
        return [
            {"index": i + 1, **t.to_dict()}
            for i, t in enumerate(tasks)
        ]

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/api/tasks")
    def list_tasks():
        return jsonify({"tasks": tasks_with_index()})

    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title", "")
        try:
            t = todo.add_task(title)
            return jsonify({"message": "Créée", "task": t.to_dict()}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id: int):
        try:
            t = todo.get_task(task_id)
            return jsonify(t.to_dict())
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    @app.patch("/api/tasks/<int:task_id>")
    def update_task(task_id: int):
        data = request.get_json(silent=True) or {}
        try:
            updated = None
            if "done" in data and bool(data["done"]):
                updated = todo.mark_done(task_id)
            if "title" in data:
                updated = todo.update_title(task_id, data["title"])
            if not updated:
                return jsonify({"error": "Spécifie 'title' ou 'done'."}), 400
            return jsonify(updated.to_dict())
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id: int):
        try:
            title = todo.delete_task(task_id)
            return jsonify({"message": f"Tâche supprimée: {title}"}), 200
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
