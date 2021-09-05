from credentials import Credentials
def create_credential(acc_name,acc_password):
    """Method to create new credential
    """
    new_credential=Credentials(acc_name,acc_password)
    return new_credential

def generate_password():
    newpass=Credentials.generate_password()
    return newpass


def main():
    twitter=create_credential("Twitter","123")
    print(twitter.acc_name)

instapass=generate_password()
print(f'My insta pass is{instapass}')

if __name__ == '__main__':
    main()