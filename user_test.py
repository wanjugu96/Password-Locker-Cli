import unittest
from user import User
from credentials import Credentials
class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for our contact class behaviours
    unnittest.TetsCase:Testcase class that helps crete testcases
    """
    User.user_list=[]

    def setUp(self):
        """
        set up method to run before each testcase
        """
        Credentials.credentials_list=[]
        twitter=Credentials("twitter","mary","2edjh")
        twitter1=Credentials("twitter","mary","2edjh")
        twitter.save_credential()
        twitter1.save_credential()
        self.new_user=User("wanjugu","Test@123$",Credentials.credentials_list)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list=[]

    def test_init(self):
        """
        Test to test if user object is being intialized properly
        """
        twitter=Credentials("twitter","mary","2edjh")
        twitter1=Credentials("twitter","mary","2edjh")
        twitter.save_credential()
        twitter1.save_credential()
        self.assertEqual(self.new_user.username,"wanjugu")
        self.assertEqual(self.new_user.password,"Test@123$") 
        self.assertEqual(self.new_user.credential_list,Credentials.credentials_list)

    def test_save_user(self):
        """
        test to confirm if user credentials are being saved
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        """
        Test to confirm multiple user accounts are being added
        """
        self.new_user.save_user()
        self.test_user=User("Jane Doe","Doe123",Credentials.credentials_list)
        self.test_user.save_user()

        self.assertEqual(len(User.user_list),2)



if __name__=='__main__':
    unittest.main()