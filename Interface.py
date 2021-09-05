from credentials import Credentials
from user import User

def create_user(username,password,credential_list):
    new_user=User(username,password,credential_list)
    return new_user
    
def save_users(user):
    user.save_user()

def display_users():
    return User.display_user_list()

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

    #while True:
    print("Welcome to passwordLocker")
    print("Create your account below")
    print("Enter your username")
    acc_username=input()
    print("Enter your password")
    acc_password=input()

    allcreds=[]
    user=create_user(acc_username,acc_password,allcreds)
    #save_users(user)

    print("Account created Successfully")
    print("login to system below")
    print("Enter your account  username")
    login_name=input()
    print("enter your password")
    login_password=input()
    print(f"The username is {user.username} password is {user.password}")
    if user.password==login_password:

        print("succsessfully logged in")
        print('\n')
        while True:
            print("What would you like to do:")
            print('\n')
            print("Enter:store-To Store existinng account password , view-To view saved passwords , new-To delete saved credentials,delete-to delete a saved credential  ")
            option=input().lower()


            if option=='store':
                print('Enter accoutn name you want store eg twitter')
                account_name=input()
                print('\n')
                print('Enter password for that account eg twittes123')
                account_password=input()

               
                account_name=create_credential(account_name,account_password)
                save_credential(account_name)


            elif option=='view':
                if display_credentials():
                    print("your saved credentials are:")

                    user.credential_list=display_credentials()
                    for credential in user.credential_list:
                        print(f"name is:{credential.acc_name} pass is:{credential.acc_password}")
                        #print(f")
                else:
                    print("You dont have saved credentials")

                    

            elif option=='new':
                print("Enter the name of the new account youd like to save:")
                new_acc_name=input()

                print("Would you like a generated password yes or no ?")
                yes_no=input().lower()

                if yes_no=='yes':
                    new_acc_pass=generate_password()
                elif yes_no=='no':
                    print('please enter the password to new account:')
                    new_acc_pass=input()
                
                save_credential(create_credential(new_acc_name,new_acc_pass))

                # else:
                #     print("please enter valid option yes or no")
                
                
               

            elif option=='delete':
                print("what is the name of the credential youd like to delete?")
                delete_name=input()
                for credential in user.credential_list:
                    if credential.acc_name==delete_name:
                        delete_credential(credential)


            else:
                print("please enter a valid option.")
            


    else:
        print("Wrong password")

        # for user in display_users():
        # print(f"user added name is {user.username}")

            
        #while True:
            













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
    
    allcredss=[]
    shelly=create_user("Shelly","1234",allcreds)

    allcredss=shelly.credential_list

    print(shelly.username)

    shelly.credential_list=display_credentials()

    for credential in shelly.credential_list:
        print(f"name is:{credential.acc_name} pass is:{credential.acc_password}")

        



    instapass=generate_password()
    print(f'My insta pass is{instapass}')

if __name__ == '__main__':
    main()