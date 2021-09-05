from logging import StringTemplateStyle
import random
import string
#from user import User

class Credentials(): 

    credentials_list=[]
    """
    Class generates various accounts with passwords
    """
    def __init__(self,acc_name,acc_password):
        self.acc_name=acc_name
        self.acc_password=acc_password
    
    def save_credential(self):
        """
        Method to save added credentials
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Method to delete credentials
        """
        Credentials.credentials_list.remove(self)
    def generate_password():
        
        lower=string.ascii_lowercase
        upper=string.ascii_uppercase
        num=string.digits
        symbols=string.punctuation
        all=lower+upper+num+symbols
        temp=random.sample(all,8)
        password="".join(temp)
        return password

    @classmethod
    def display_credential_list(cls):
        return cls.credentials_list


    
