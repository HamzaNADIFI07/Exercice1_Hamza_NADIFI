import argparse
from controllers.todo_controller import ToDoController
from views.cli import CLIView

def main():
    parser = argparse.ArgumentParser(description="ToDoList MVC en ligne de commande")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="Afficher les tâches")

    add = sub.add_parser("add", help="Ajouter une tâche")
    add.add_argument("title")

    done = sub.add_parser("done", help="Marquer une tâche comme terminée")
    done.add_argument("index", type=int)

    delete = sub.add_parser("delete", help="Supprimer une tâche")
    delete.add_argument("index", type=int)

    args = parser.parse_args()
    controller = ToDoController(CLIView())

    if args.command == "add":
        controller.add_task(args.title)
    elif args.command == "list":
        controller.list_tasks()
    elif args.command == "done":
        controller.mark_done(args.index)
    elif args.command == "delete":
        controller.delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
