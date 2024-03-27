from dataclasses import dataclass


@dataclass
class Pattern:
    name: str

    # each tuple represents a coordinate of an alive cell in the grid
    alive_cells: set[tuple[int, int]]
