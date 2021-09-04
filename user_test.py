import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for our contact class behaviours
    unnittest.TetsCase:Testcase class that helps crete testcases
    """

    def setUp(self):
        """
        set up method to run before each testcase
        """
        self.new_User=User("wanjugu","Test@123$")

        def test_init(self):
