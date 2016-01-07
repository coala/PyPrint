import unittest

from pyprint.ContextManagers import retrieve_stdout


class ContextManagersTest(unittest.TestCase):

    def test_retrieve_stdout(self):  # Tests replace_stdout implicitly
        with retrieve_stdout() as sio:
            print("test")
            self.assertEqual(sio.getvalue(), "test\n")
