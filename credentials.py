
class Credentials:

    '''
    class that creates instaces of user accounts
    '''

    cred_list = []

        #assign property to credential list#

    def __init__(self, account , email , password):
    
        self.account = account
        self.email = email
        self.password = password

        #save credentials#

        def save_cred(self):
        
            Credentials.cred_list.append(self)

        #Delete credentials#

        def delete_cred(self):
         
            Credentials.cred_list.remove(self)

        #search for credentials#

        @classmethod
        def find_account(cls, account):
            '''
            search for accounts
            '''
            for cred in cls.cred_list:
                if cred.account == account:
                    return cred

        #confirm credentials#

        @classmethod
        def cred_exists(cls, account):
            '''
            confirm a class actually exists
            '''
            for cred in cls.cred_list:
                if cred.account == account:
                    return True
            return False   

        #Display credentials#

        @classmethod
        def display_cred(cls):
            '''
            method that returns all credentials
            '''
            return cls.cred_list

        #copy password#


        @classmethod
        def copy_password(cls, password):
            find_account = Credentials.find_account(password)
                 
