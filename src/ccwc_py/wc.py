from typing import Annotated

import typer

from .count import get_count_methods

app = typer.Typer()


@app.command()
def main(
    filename: Annotated[str, typer.Argument(help="The file to count words in")],
    count_bytes: Annotated[bool, typer.Option("-c")] = False,
    count_lines: Annotated[bool, typer.Option("-l")] = False,
    count_words: Annotated[bool, typer.Option("-w")] = False,
    count_chars: Annotated[bool, typer.Option("-m")] = False,
) -> None:
    count_methods = get_count_methods(
        count_bytes_flag=count_bytes,
        count_lines_flag=count_lines,
        count_words_flag=count_words,
        count_chars_flag=count_chars,
    )
    counts = [0] * len(count_methods)

    with open(filename, "r", newline="") as file:
        for line in file:
            for i, count_method in enumerate(count_methods):
                counts[i] += count_method(line)
    print(f"  {' '.join(str(c) for c in counts)} {filename}")
