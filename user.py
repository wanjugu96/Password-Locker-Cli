#create a password locker 
#with my details, a login username and password
from credentials import Credentials
class User:
    user_list=[]
    """
    Class generates a password locker accounts
    """
    def __init__(self,username,password,credentials_list):
        self.username=username
        self.password=password
        self.credential_list=credentials_list

        credentials_list=Credentials.credentials_list

    def save_user(self):
        """
        method to Save user logins
        """
        User.user_list.append(self)
    
    def user_login(self,password):
        """
        Method that takes in the username and password and determines if they match fo that account
        """
        if self.password==password:
            return True

    @classmethod
    def display_user_list(cls):
        return cls.user_list
        


   
