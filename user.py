#create a password locker 
#with my details, a login username and password

class User:
    user_list=[]
    """
    Class generates a password locker accounts
    """
    def __init__(self,username,password,Account_credentials):
        self.username=username
        self.password=password
        self.Account_credentials=Account_credentials

    def save_user(self):
        """
        method to Save user logins
        """
        User.user_list.append(self)
    
    def user_login(self):
        """
        Method that takes in the username and password and determines if they match fo that account
        """
        if self.username==self.password:
            return True


   
