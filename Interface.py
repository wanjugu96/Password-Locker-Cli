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

def create_credential(acc_name,acc_username,acc_password):
    """Method to create new credential
    """
    new_credential=Credentials(acc_name,acc_username,acc_password)
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
    save_users(create_user("wanjugu","1234",[]))
    save_users(create_user("Doe","doe@123",[]))

    
    print("*************************************************************************************************************************************************************")
    print('\n')

    print("                                                         HELLO !                                                           ")
    print('\n')
    print("                                                  WELCOME TO PASSWORDLOCKER                       ")
    print('\n')

    print("*************************************************************************************************************************************************************")
    print('\n')
    # print("please Enter :")
    # print("signin - if already have an acccount") 
    # print("create - create an account")

    # login_input=input().lower()

    # if login_input=='create':  
    print(" Create your account below")
    print('\n')
    print(" Enter your username")
    acc_username=input()
    print('\n')
    print(" Enter your password")
    acc_password=input()

    allcreds=[]
    user=create_user(acc_username,acc_password,allcreds)
    save_users(user)
    print("*******************************************************************************************************************************")

    print(" Account created Successfully ")
    print('\n')
    while True:

        print(" login to your account below:")
        print('\n')
        print("*************************************************************************************************************************************************************")

        print(' Enter username:')
        login_name=input()
        print('\n')
        print(' Enter password:')
        print('\n')
        login_password=input()
        print('\n')

        print("*************************************************************************************************************************************************************")
        if user.password==login_password:
            print(" succsessfully logged in")
            print('\n')
            print("*************************************************************************************************************************************************************")
        
            while True:
                print("*************************************************************************************************************************************************************")


                print("  What would you like to do? ...Use the codes below:")
                print('\n')
                print("  store - To Store existinng account passwords ")
                print("  view -  To view saved account credentials") 
                print("  new -   To save new accounts credentials")
                print("  delete -To delete a saved credential")
                print("  ex -    To log out from  application")
                print('\n')
                print("*************************************************************************************************************************************************************")

                option=input().lower()
                print('\n')


                if option=='store':
                    print('Enter account name you want store eg twitter')
                    account_name=input()
                    print('\n')
                    print(f'Enter username of {account_name} account')
                    account_username=input()
                    print('\n')
                    print(f'Enter password for {account_name}')
                    account_password=input()
                    print('\n')
                    print(f"Credential for {account_name} saved successfully")
                    print('\n')

                
                    account_name=create_credential(account_name,account_username,account_password)
                    save_credential(account_name)


                elif option=='view':
                    if display_credentials():
                        print('\n')
                        print("your saved credentials are:")
                        print('\n')


                        user.credential_list=display_credentials()
                        for credential in user.credential_list:

                            print(f" -  {credential.acc_name} credentials are: Username is {credential.acc_username} password is:{credential.acc_password}")
                            
                            print("____________________________________________________________________________________________________________________________________________")


                            print("_____________________________________________________________________________________________________________________________________________")
                    else:
                        print('\n')

                        print("You dont have saved credentials")

                        

                elif option=='new':
                    
                    
                    print("Enter the name of the new account youd like to save:")
                    new_acc_name=input()
                    print('\n')
                    print(f"Enter the User name of {new_acc_name} account")
                    new_acc_username=input()
                    print('\n')
                    while True:

                        print(f"Would you like a generated password for {new_acc_name} account yes or no ?")
                        yes_no=input().lower()
                        print('\n')

                        if yes_no=='yes':
                            new_acc_pass=generate_password()
                            print(f"your generated password is{new_acc_pass}")
                            print('\n')
                            print(f"Credential for {new_acc_name} saved successfully")
                            save_credential(create_credential(new_acc_name,new_acc_username,new_acc_pass))
                            break
                        elif yes_no=='no':
                            print('please enter the password to new account:')
                            new_acc_pass=input()
                            print('\n')
                            print("Credential for {new_acc_name} saved successfully")
                            save_credential(create_credential(new_acc_name,new_acc_username,new_acc_pass))
                            break
                        
                        else:
                            #print('\n')
                            print("please enter valid option yes or no")
                            print('\n')
                            continue
                            


                        
                        

                    # else:
                    #     print("please enter valid option yes or no")
                    
                    
                

                elif option=='delete':
                    print("what is the name of the credential youd like to delete?")
                    delete_name=input()
                    print('\n')
                    for credential in user.credential_list:
                        if credential.acc_name!=delete_name:
                            (f"Credentials for {delete_name} do not exist")
                        
                
                        elif credential.acc_name==delete_name:
                            delete_credential(credential)
                            print(f"successfully deleted {credential.acc_name} account credentials")
                            print('\n')
                            
                elif option=='ex':
                    print('\n')
                    print(f"Bye bye {login_name}. Hope to see you again")
                    print('\n')

                    break


                else:
                    print("Oppsie please enter a valid option.")
                

        else:
            print("Wrong password please try again!")

            continue
            
                 



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