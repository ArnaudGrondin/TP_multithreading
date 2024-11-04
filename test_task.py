import unittest
from task import Task
import numpy as np
# TODO VERIFIER QUE LE TEST ECHOUE # uv run python unittest


class TestTask(unittest.TestCase):
    def test_task(self):
        t = Task()
        t.work()
        np.testing.assert_allclose(t.a @ t.x, t.b)


if __name__ == "__main__":
    unittest.main()
