class Credentials:
    #save credential
    #deletecredential
    #display credentials
    #genearate rand pass
    credentials_list=[]
    """
    Class generates various accounts with passwords
    """
    def __init__(self,acc_name,acc_password):
        self.acc_name=acc_name
        self.acc_password=acc_password
    
    def save_credential(self):
        Credentials.credentials_list.append(self)
    
    @classmethod
    def display_credential_list(cls):
        return cls.credentials_list


    
