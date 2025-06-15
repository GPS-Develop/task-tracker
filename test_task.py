import unittest
from task import no_task, validate_digit

class TestTasks(unittest.TestCase):
    def test_returns_true_empty_list(self):
        tasks = []

        result = no_task(tasks, "No tasks.")
        self.assertEqual(result, True)

    def test_validate_digit(self):
        tasks = [{"name": "task1"}, {"name": "task2"}]

        result = validate_digit("3", tasks)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()