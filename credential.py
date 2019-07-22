import string
import pyperclip
from random import choice
class Credential:

    credential_list = []  


def __init__(self, account, password, account_password):



        self.account = account
        self.password = account_password
        self.account_password = account_password
        
def save_credential(self):

        '''
        save_credential method saves credentials objects into credential_list
        '''

        Credential.credential_list.append(self) 
        
@classmethod
def generate_password(cls):
        '''
        Method that generates a random alphanumeric password
        '''
        
        size = 14


        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase


        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password
##Check credentials exist

# @classmethod
# def credential_exist(cls, account):

        
#         for credential in cls.credential_list:
#             if credential.account == account:
#                 return True
            
#         return False
##Display credentials
# @classmethod
# def display_credential(cls,password):

        # user_credential_list = []

        # for credential in cls.credential_list:
        #     if credential.user_password == password:
        #         user_credential_list.append(credential)

        # return user_credential_list
    