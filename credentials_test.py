import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_credential = Credentials("facebook", "justineadriano@gmail", "matongo2010")

        def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.credentials_list = []

        #6th test checking initialisation#

        def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_credential.account, "facebook")
        self.assertEqual(self.new_credential.email, "justineadriano@gmail.com")
        self.assertEqual(self.new_credential.password, "matongo2010")

        #7th test save credentials#

        def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_credential.save_cred()
        self.assertEqual(len(Credentials.credentials_list),1)

        #8th test saving multiple credentials#

        def test_saving_multiple_credentials(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_credential.save_cred()
        test_credential = Credentials("instagram", "testuser","password")
        test_credential.test_save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

        #9th test delete credentials#

        def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("instagram", "testuser","password")
        test_credential.save_credential()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.cred_list), 1)

        #10th test search for credentials#

        def test_search_for_credential(self):
        '''
        test if credentials can be searched for
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("instagram", "testuser","password")
        test_credential.save_credential()
        find_credential= Credentials.find_account("instagram")
        self.assertEqual(find_credential.account, test_credential.account)

        #11th test confirming accounts credentials#

    def test_confirm_credential_exists(self):
        '''
        confirming that credentials actually exists
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("instagram", "testuser","password")
        test_credential.save_credential()
        credential_exists = Credentials.credential_exists("instagram")
        self.assertTrue(credential_exists)

        #test 12th Displaying credentials#

        
        def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credential(), Credentials.credentials_list)

         #copy password test 13th#

        def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_credential.save_credential()
        Credentials.copy_password("meroka")
        self.assertEqual(self.new_credential.password, pyperclip.paste())