import os
import hashlib
from rich.console import Console
from rich.panel import Panel

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hasher():
    console.print(Panel("[yellow1]Welcome to hash calculator![/yellow1]", title="[bold cyan]Hash Calculator[/bold cyan]"))
    text = input("Enter the text to hash: ")
    if not text:
        console.print("[red]Lütfen bir metin girin![/red]")
        return

    clear()

    # MD5
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    
    # SHA-1
    sha1_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    
    # SHA-256
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

    clear()

    console.print(f"\n[yellow1]Target Text:[/yellow1] {text}")
    console.print(f"[bold cyan]MD5 Hash:[/bold cyan] {md5_hash}")
    console.print(f"[bold cyan]SHA1 Hash:[/bold cyan] {sha1_hash}")
    console.print(f"[bold cyan]SHA256 Hash:[/bold cyan] {sha256_hash}")

if __name__ == "__main__":
    hasher()
