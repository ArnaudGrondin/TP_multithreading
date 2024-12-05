import time
import json
import numpy as np


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choose the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        d = {
            "identifier": self.identifier,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "size": self.size,
            "x": self.x.tolist(),
            "time": self.time,
        }
        return json.dumps(d)

    @staticmethod
    def from_json(text: str) -> "Task":
        d = json.loads(text)
        task = Task(d["identifier"], d["size"])
        task.a = np.array(d["a"])
        task.a = np.array(d["b"])
        task.x = np.array(d["x"])
        task.size = d["size"]
        task.time = d["time"]
        return task

    def __eq__(self, other: "Task") -> bool:
        same = self.identifier == other.identifier and self.size == other.size
        return same
