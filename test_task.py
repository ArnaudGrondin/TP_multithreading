import unittest
from task import Task
import numpy as np
# pour  verifier que le test échoue $ uv run python unittest


class TestTask(unittest.TestCase):
    def test_task(self):
        t = Task()
        t.work()
        np.testing.assert_allclose(t.a @ t.x, t.b)

    def test_serialisation(self):
        a = Task()
        txt = a.to_json()

        b = Task.from_json(txt)
        np.testing.assert_equal(a, b)


if __name__ == "__main__":
    unittest.main()
