from typing import Annotated

import typer

from .count import get_count_method

app = typer.Typer()


@app.command()
def main(
    filename: Annotated[str, typer.Argument(help="The file to count words in")],
    count_bytes: Annotated[bool, typer.Option("-c")] = False,
    count_lines: Annotated[bool, typer.Option("-l")] = False,
) -> None:
    count = 0
    count_method = get_count_method(count_bytes_flag=count_bytes, count_lines_flag=count_lines)

    with open(filename, "r", newline="") as file:
        for line in file:
            count += count_method(line)
    print(f"{count} {filename}")
