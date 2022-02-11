from dataclasses import dataclass
from rich.color import Color
from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table

@dataclass
class Pet:
    width: int = 80
    background_color: Color = Color.from_rgb(255, 255, 255)
    def __init__(self, name=None, breed=None, age=0):
        self.name = name
        self.breed = breed
        self.age = age
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        yield f"[b]Pet:[/b] #{self.name}"
        pet_table = Table(title="Pets")
        pet_table.add_column("Attribute",justify="left", style="cyan", no_wrap=True)
        pet_table.add_column("Value",style="magenta")
        pet_table.add_row("Breed", self.breed)
        pet_table.add_row("age", str(self.age))
        yield pet_table
    
    #def __rich__(self) -> str:
    #    return "[bold cyan]"+f"{self.name} is a {self.breed} and is {self.age} years old."
    
    def __str__(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old."

if __name__ == '__main__':
    pet = Pet("Fido", "Labrador", 3)
    #print(pet)
    console = Console()
    #console.log(pet)
    console.print(pet)