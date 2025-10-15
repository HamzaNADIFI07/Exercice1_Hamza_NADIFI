from flask import Flask, jsonify, request
from controllers.todo_controller import ToDoController

def create_app():
    app = Flask(__name__)
    todo = ToDoController()

    def tasks_with_index():
        """Formate les tâches avec leur index pour la réponse JSON."""
        tasks = todo.list_tasks()
        return [{"index": i + 1, **t.to_dict()} for i, t in enumerate(tasks)]

    # Vérification de l’état de l’API
    @app.get("/health")
    def health():
        return jsonify({
            "status": "ok",
            "message": "L'API fonctionne"
        })

    # Liste toutes les tâches
    @app.get("/api/tasks")
    def list_tasks():
        return jsonify({"tasks": tasks_with_index()})

    # Crée une nouvelle tâche
    @app.post("/api/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title", "")
        try:
            t = todo.add_task(title)
            return jsonify({"message": "Tâche créée avec succès", "task": t.to_dict()}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    # Récupère une tâche par ID
    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id: int):
        try:
            t = todo.get_task(task_id)
            return jsonify(t.to_dict())
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    # Met à jour une tâche (titre )
    @app.patch("/api/tasks/<int:task_id>")
    def update_task(task_id: int):
        data = request.get_json(silent=True) or {}
        try:
            updated = None
            if "title" in data:
                updated = todo.update_title(task_id, data["title"])
            return jsonify({"message": "Tâche mise à jour", "task": updated.to_dict()})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    # Supprime une tâche par ID
    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id: int):
        try:
            title = todo.delete_task(task_id)
            return jsonify({"message": f"Tâche supprimée : {title}"}), 200
        except KeyError:
            return jsonify({"error": f"Tâche id={task_id} introuvable."}), 404

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
