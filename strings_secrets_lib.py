from rich.console import Console
from rich.panel import Panel
import string
import secrets
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()

def generate_password():
    console.print(Panel("[bold cyan]Welcome to password generator![/bold cyan]..."))
    try:
        length = int(input("Enter the desired password length: (Example: 16) "))
        punctuation = input("Include punctuation? (y/n): ").lower()

        if punctuation == 'y':
            alphabet = string.ascii_letters + string.digits + string.punctuation
        else:
            alphabet = string.ascii_letters + string.digits

        clear()

        password = ''.join(secrets.choice(alphabet) for i in range(length))
        console.print(Panel(f"[yellow1]Generated password: [/yellow1][bright_green]{password}[/bright_green]"))
    except ValueError:
        console.print("[bold red]Error: Please enter a valid number![/bold red]")

generate_password()
