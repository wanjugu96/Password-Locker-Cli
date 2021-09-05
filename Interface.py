from credentials import Credentials
from user import User

def create_user(username,password,credential_list):
    new_user=User(username,password,credential_list)
    return new_user

def login(credential,password):
    return User.user_login(password)

def create_credential(acc_name,acc_password):
    """Method to create new credential
    """
    new_credential=Credentials(acc_name,acc_password)
    return new_credential

def generate_password():
    newpass=Credentials.generate_password()
    return newpass

def save_credential(credential):
    credential.save_credential()

def display_credentials():
    
    return Credentials.display_credential_list()

def delete_credential(credential):
    return Credentials.delete_credentials(credential)



    
def main():
    print("Welcome to passwordLocker")
    print("Create your account below")
    print("Enter your username")
    acc_username=input()
    print("Enter your password")
    acc_password=input()
    allcreds=[]
    user=create_user(acc_username,acc_password,allcreds)
    print("Account created Successfully")
    print("login to system below")
    print("Enter your accounr username")
    login_name=input()
    print("enter your password")
    login_password=input()
    if user.password==login_password:
        print("succsessfully logged in")

    else:
        print("Wrong password")












    print("============================================================Random tests==========================================================")

    print("============================================================Random tests===============================================================")
    twitter=create_credential("Twitter","123")
    print(twitter.acc_name)
    insta=create_credential("Insta","4567")
    Fb=create_credential("fb","1234")

    twitter.save_credential()
    insta.save_credential()
    allcreds=display_credentials()

    #print(display_credentials())
    
    delete_credential(twitter)
    allcreds=display_credentials()

    shelly=create_user("Shelly","1234",allcreds)
    print(shelly.username)
    for credential in allcreds:
        print(f"name is:{credential.acc_name}")
        print(f"pass is:{credential.acc_password}")



    instapass=generate_password()
    print(f'My insta pass is{instapass}')

if __name__ == '__main__':
    main()