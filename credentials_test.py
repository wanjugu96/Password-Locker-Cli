from credentials import Credentials
import unittest

class TestCredentials(unittest.TestCase):
    """
    Test calss that defines test cases for our credentials class behaviours
    unnittest.TetsCase:Testcase class that helps crete testcases
    """
    def setUp(self):
        """
        Setup method to run before each testcase
        """
        self.new_credential=Credentials("Facebook","123456")

    def test_init(self):
        """
        Test to confirm the proper initialization of a credential
        """

        self.assertEqual(self.new_credential.acc_name,"Facebook")
        self.assertEqual(self.new_credential.acc_password,"123456")



if __name__=='__main__':
    unittest.main()