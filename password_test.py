import unittest # Importing the unittest module
from password import Member # Importing the members class


class TestMember(unittest.TestCase):

  '''
    Test class that defines test cases for the members class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''
def setUp(self):

         '''
        Set up method to run before each test cases.
        '''

         self.new_member = Member("Joseph","Karanja","0745345678", "JosepK", "jose@ms.com") # create member object

def test_init(self):
        '''
    test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_member.first_name,"Joseph")
        self.assertEqual(self.new_member.last_name,"Karanja")
        self.assertEqual(self.new_member.phone_number,"0712345678")
        self.assertEqual(self.new_member.username,"JosepK")
        self.assertEqual(self.new_member.email,"jose@ms.com")

if __name__ == '__main__':
    unittest.main()



    def test_save_member(self):
        '''
        test_save_member test case to test if the member object is saved into
         the member list
        '''

        self.new_member.save_member() # saving the new contact
        self.assertEqual(len(Member.member_list),1)

if __name__ ==  '__main__':
    unittest.main()
