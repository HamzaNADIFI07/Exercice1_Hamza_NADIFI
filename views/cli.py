class CLIView:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("📭 Aucune tâche trouvée.")
        for i, t in enumerate(tasks, 1):
            status = "✔️" if t.done else "❌"
            print(f"[{i}] {status} {t.title} ({t.created_at})")

    @staticmethod
    def show_message(msg):
        print(msg)
