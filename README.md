# Password-Locker
## Author

[Wanjugu Mung'au](https://github.com/wanjugu96)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.



## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do not want anymore.



## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ``https://github.com/wanjugu96/Password-Locker-Cli.git```

* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./interface.py
* To run test for the user class:
        $ python3 credentials_test.py

* To run test for the credentials class:
        $ python3 user_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./interface.py```|Hello Welcome to Password locker... <br> |
|Create account| input username and password| Account has been created succesfully! |
|Login | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a existing credential in the application| Enter ```store```|Enter Account, username, password<br>
|New credentials|choose ```new``` to enter new credentials| enter ```yes``` to generate password or ```no``` to enter own password|
|Display all stored credentials | Enter ```view```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |<br>
|Delete an existing credential that you don't want anymore|Enter ```delete```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|logout from application| Enter ```ex```| The logged out from the application|

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [shellmithwanjugu98@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Wanjugu Mung'au**