from Interface import delete_credential
from credentials import Credentials
import unittest

class TestCredentials(unittest.TestCase):
    Credentials.credentials_list=[]
    """
    Test calss that defines test cases for our credentials class behaviours
    unnittest.TetsCase:Testcase class that helps crete testcases
    """
    def setUp(self):
        """
        Setup method to run before each testcase
        """
        self.new_credential=Credentials("Facebook","mary","123456")

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
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        """
        Test to confirm multiple credentials can be saved
        """
        self.test_credential=Credentials("Facewsok","doe","123456")
        self.test_credential.save_credential()
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
       '''
        Credentials.credentials_list= []

    def test_delete_credential(self):
        """
        Test delete of a credential
        """     
        self.test_credential=Credentials("Facewsok","doe","123456")
        self.test_credential.save_credential()
        self.test_credential.delete_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),0)
        
    def display_credentials(self):
        """
        Test to confirm all credentials rea being returned
        """
        pass




if __name__=='__main__':
    unittest.main()