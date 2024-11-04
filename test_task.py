import unittest
import task
import numpy as np


class TestTask:
    def test_task():
        np.assert_allclose(task.a * task.x, task.b)


if __name__ == "__main__":
    unittest.main()
