from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Writer(ABC):
    def __init__(self, file_path: Path | str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(exist_ok=True, parents=True)

    def _write_line(self, content: str):
        with self.file_path.open(mode="a") as f:
            print(content, file=f)

    @abstractmethod
    def write(self, content: dict[str, Any]):
        ...


class CSVWriter(Writer):
    def __init__(self, file_path: Path | str, sep=","):
        super().__init__(file_path=file_path)
        self.sep = sep

    def set_header(self, headers: list[str]):
        self.headers = list(map(str, headers))
        h = self.sep.join(self.headers)
        self._write_line(content=h)
        return self

    def write(self, d: dict[str, Any]):
        data = []
        for header in self.headers:
            data.append(d.get(header, ""))
        data = map(str, data)
        row = self.sep.join(data)
        self._write_line(content=row)
