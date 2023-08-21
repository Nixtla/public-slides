import time
from rich.console import Console
from rich.align import Align

def number_representation(n):
    numbers = {
        '0': [
            ' 0000 ',
            '00  00',
            '00  00',
            '00  00',
            ' 0000 '
        ],
        '1': [
            '1111  ',
            '  11  ',
            '  11  ',
            '  11  ',
            '111111'
        ],
        '2': [
            ' 2222 ',
            '22  22',
            '   22 ',
            '  22  ',
            '222222'
        ],
        '3': [
            ' 3333 ',
            '33  33',
            '   333',
            '33  33',
            ' 3333 '
        ],
        '4': [
            '44  44',
            '44  44',
            '444444',
            '    44',
            '    44'
        ],
        '5': [
            '555555',
            '55    ',
            '55555 ',
            '    55',
            '55555 '
        ],
        '6': [
            ' 6666 ',
            '66    ',
            '66666 ',
            '66  66',
            ' 6666 '
        ],
        '7': [
            '777777',
            '   77 ',
            '  77  ',
            ' 77   ',
            '77    '
        ],
        '8': [
            ' 8888 ',
            '88  88',
            ' 8888 ',
            '88  88',
            ' 8888 '
        ],
        '9': [
            ' 9999 ',
            '99  99',
            ' 99999',
            '    99',
            ' 9999 '
        ]
    }
    
    # Return representation for a given number
    return '\n'.join(numbers[str(n)])

console = Console()
console.clear()

def vertical_padding(lines=1, skip_lines=0):
    """Return vertical padding to center text vertically."""
    height = console.size.height
    padding_lines = (height - lines) // 2 - skip_lines
    return '\n' * padding_lines

def center_print(message: str, duration: int = None, skip_lines=1):
    """Utility function to print centered text."""
    console.print(vertical_padding(skip_lines=skip_lines))
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
        center_print(f'[bold green]{number_representation(i)}[/bold green]', skip_lines=3)
        time.sleep(1)
    console.clear()
    center_print("[bold blue]Happy Forecasting! 😃🎉[/bold blue]", 3)
    time.sleep(900)

if __name__ == "__main__":
    centered_counter()

