import unittest
from pathlib import Path


class TaskSecondTest(unittest.TestCase):
    def test_1(self):
        path = Path('task2/beats.csv')
        self.assertEquals((str(path), path.is_file()), (str(path), True))
