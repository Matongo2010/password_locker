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
