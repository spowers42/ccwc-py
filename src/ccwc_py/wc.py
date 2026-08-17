from typing import Annotated

import typer

from .count import get_count_method

app = typer.Typer()


@app.command()
def main(
    filename: Annotated[str, typer.Argument(help="The file to count words in")],
    count_bytes: Annotated[bool, typer.Option("-c")] = False,
) -> None:
    count = 0
    count_method = get_count_method(count_bytes_flag=count_bytes)

    with open(filename, "r") as file:
        for line in file:
            count += count_method(line)
    print(f"{count} {filename}")
