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
        self.new_user=User("wanjugu","Test@123$",{"twitter":"1w2@3","instagram":"wena"})

    def test_init(self):
        """
        Test to test if user object is being intialized properly
        """
        self.assertEqual(self.new_user.username,"wanjugu")
        self.assertEqual(self.new_user.password,"Test@123$")
        self.assertEqual(self.new_user.Account_credentials,{"twitter":"1w2@3","instagram":"wena"})

if __name__=='__main__':
    unittest.main()