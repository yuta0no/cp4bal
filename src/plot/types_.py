from dataclasses import dataclass


@dataclass
class ResultPaths:
    name: str
    paths: list[str]
