import unittest
import task
import numpy as np


class TestTask(unittest.TestCase):
    def test_task(self):
        t = task()
        np.assert_allclose(t.a @ t.x, t.b)


if __name__ == "__main__":
    unittest.main()
