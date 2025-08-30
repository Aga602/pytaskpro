import typer
from models import Task, TaskFunctions
from rich import print
from manager import TaskManager

app = typer.Typer()


class CLI:
    def hello(self):
        """This is just a greeter"""
        name = typer.prompt("What is your name?")
        print(
            f"""
                [bold green]Hi {name.upper()} [bold green]
                [bold green]I am a Cli tool to maintaining your
                everyday Task[/bold green] \n
                Please add the task name, descriprion and also
                the status of task \n
                The accepted statuses are as follows \n
                1. [red]to-do[/red] \n
                2. [blue]done[/blue] \n
                3. [yellow]repeat[/yellow] \n
                """
        )

    def add_task(self):
        """This is used to add task"""
        print("Provide the name of the Task")
        task = typer.prompt("Task")
        print("Add a description")
        description = typer.prompt("Description")
        print("Add Status")
        status = typer.prompt("Status")
        inputTask = [Task(title=task, description=description, status=status)]

        manager = TaskManager()
        manager.save_load_tasks(task=inputTask)

    def remove_task(self):
        """This removes the task if exists in db"""
        print("Add title to remove")
        title = typer.prompt("Prompt", confirmation_prompt=True)
        manager = TaskManager()
        manager.remove_task(title=title)

    def callable(self, option: TaskFunctions):
        option = TaskFunctions(option).name
        match option:
            case "hello":
                func = self.hello
            case "add_task":
                func = self.add_task
            case "remove_task":
                func = self.remove_task
            case "change_status":
                ...
            case _:
                ...
        typer.run(func)
