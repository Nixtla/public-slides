import time
from rich.console import Console
from rich.align import Align

console = Console()
console.clear()

def vertical_padding(lines=1):
    """Return vertical padding to center text vertically."""
    height = console.size.height
    padding_lines = (height - lines) // 2
    return '\n' * padding_lines

def center_print(message: str, duration: int = None):
    """Utility function to print centered text."""
    console.print(vertical_padding())
    aligned_message = Align.center(message)
    console.print(aligned_message)
    if duration:
        time.sleep(duration)

def centered_counter(duration=10):
    center_print("[bold yellow]Are you ready for TimeGPT?[/bold yellow]")
    time.sleep(2)
    console.clear()
    center_print("[bold violet] Let's count together from 9 to 0 (because of Python xD)[/bold violet]")
    time.sleep(2)
    for i in range(duration-1, -1, -1):
        console.clear()
        center_print(f'[bold green]{i}[/bold green]')
        time.sleep(1)
    console.clear()
    center_print("[bold blue]Happy Forecasting! 😃🎉[/bold blue]", 3)
    time.sleep(900)

if __name__ == "__main__":
    centered_counter()

