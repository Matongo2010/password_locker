import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("facebook", "justineadriano@gmail", "matongo2010")

        def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []

        #6th test checking initialisation#

        def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "facebook")
        self.assertEqual(self.new_cred.email, "justineadriano@gmail.com")
        self.assertEqual(self.new_cred.password, "matongo2010")

        #7th test save credentials#

        def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

        #8th test saving multiple credentials#

        def test_saving_multiple_credentials(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("instagram", "testuser","password")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)

        #9th test delete credentials#

        def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("instagram", "testuser","password")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)

        #10th test search for credentials#

        def test_search_for_credential(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("instagram", "testuser","password")
        test_cred.save_cred()
        find_cred= Credentials.find_account("instagram")
        self.assertEqual(find_cred.account, test_cred.account)

        #11th test confirming accounts credentials#

    def test_confirm_credential_exists(self):
        '''
        confirming that credentials actually exists
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("instagram", "testuser","password")
        test_cred.save_cred()
        cred_exists = Credentials.cred_exists("instagram")
        self.assertTrue(cred_exists)

        #test 12th Displaying credentials#

        
        def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)

         #copy password test 13th#

        def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_cred.save_cred()
        Credentials.copy_password("meroka")
        #self.assertEqual(self.new_cred.password, pyperclip.paste())