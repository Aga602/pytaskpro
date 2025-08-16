import typer
from dataclasses import dataclass
from core.models import Task
from rich import print
from core.models import TaskFunctions 

@dataclass
class inputTask:
    inputs: Task

app = typer.Typer()

class CLI:
    def hello(self):
        """This is just a greeter"""
        name = typer.prompt("What is your name?")
        print(f"""
                [bold green]Hi {name.upper()} [bold green]
                [bold green]I am a Cli tool to maintaining your everyday Task[/bold green] \n
                Please add the task name, descriprion and also the status of task \n
                The accepted statuses are as follows \n
                1. [red]to-do[/red] \n
                2. [blue]done[/blue] \n
                3. [yellow]repeat[/yellow] \n
                """)


    def callable(self, option: TaskFunctions):
        option = TaskFunctions(option).name
        match option:
            case "hello":
                func = self.hello
            case "add_task": ...
            case "remove_task": ...
            case "change_status": ...
            case _: ...
        typer.run(func)

# if __name__ == "__main__":
#     try:
#         cli = CLI()
#         cli.callable("b")
#     except Exception as e:
#         print("Exception: ",e)