import time
from rich.console import Console
from rich.align import Align

console = Console()

def center_print(message: str, duration: int = None):
    """Utility function to print centered text."""
    aligned_message = Align.center(message)
    console.print(aligned_message)
    if duration:
        time.sleep(duration)

def centered_counter(duration=10):
    center_print("[bold yellow]Are you ready for TimeGPT?[/bold yellow]")
    time.sleep(2)
    console.print("\n")
    for i in range(duration, -1, -1):
        console.clear()
        center_print(f'[bold green]{i}[/bold green]')
        time.sleep(1)
    console.clear()
    center_print("[bold blue]Happy Forecasting! 😃🎉[/bold blue]", 3)
    time.sleep(900)

if __name__ == "__main__":
    centered_counter()

