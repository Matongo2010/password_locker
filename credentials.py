import pyperclip
class Credentials:

    '''
    class that creates instaces of user accounts
    '''

    credentials_list = []

        #assign property to credential list#

    def __init__(self, account , email , passlock):
    
        self.account = account
        self.email = email
        self.password = password

        #save credentials#

        def save_credentials(self):
        '''
        self credentials in cred_list
        '''
        Credentials.credentials_list.append(self)

        #Delete credentials#

        def delete_credentials(self):
        '''
        delete credentials 
        '''
        Credentials.credentials_list.remove(self)

        #search for credentials#

        @classmethod
        def find_account(cls, account):
        '''
        search for accounts
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

        #confirm credentials#

        @classmethod
        def credentials_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False   

        #Display credentials#

        @classmethod
        def display_credentials(cls):
        '''
        method that returns all credentials
        '''
        return cls.credentials_list

    ##########copy passwoed############     
