import tempfile
import unittest
from pathlib import Path
from todo import TaskList

class TaskTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'tasks.json'
        self.tasks = TaskList(self.path)

    def test_add_and_reload(self):
        self.tasks.add('Купить хлеб')
        self.assertEqual(TaskList(self.path).items, [{'title': 'Купить хлеб', 'done': False}])

    def test_reject_empty(self):
        with self.assertRaises(ValueError): self.tasks.add('  ')

    def test_complete(self):
        self.tasks.add('Задача')
        self.tasks.complete(1)
        self.assertTrue(TaskList(self.path).items[0]['done'])

    def test_remove(self):
        self.tasks.add('Задача')
        self.tasks.remove(1)
        self.assertEqual(TaskList(self.path).items, [])

    def test_invalid_number(self):
        for n in (0, -1, 1):
            with self.assertRaises(ValueError): self.tasks.complete(n)
            with self.assertRaises(ValueError): self.tasks.remove(n)

if __name__ == '__main__': unittest.main()
