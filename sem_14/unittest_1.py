import unittest

from task_1 import filter_string


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.result = 'abc'
    def test_no_changes(self):
        self.assertEqual(filter_string('abc'), self.result)

    def test_case_change(self):
        self.assertEqual(filter_string('Abc'), self.result)

    def test_remove_punct(self):
        self.assertEqual(filter_string('a.b.c'), self.result)

    def test_remove_other_alphs(self):
        self.assertEqual(filter_string('abcабв'), self.result)
        
    def test_complete_changes(self):
        self.assertEqual(filter_string('A.b.c.абв'), self.result)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)