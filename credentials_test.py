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

    def test_save_credential(self):
        """
        Test to confirm credentials are being saved
        """        

    def test_save_multiple_credentials(self):
        """
        Test to confirm multiple credentials can be saved
        """
    def test_delete_credential(self):
        """
        Test delete of a credential
        """     
    def display_credentials(self):
        """
        Test to confirm all credentials rea being returned
        """




if __name__=='__main__':
    unittest.main()