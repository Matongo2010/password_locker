class Member:

    """
    Class that generates new instances of members
    """

    member_list = [] # Empty contact list

    # Init method up here

    def save_member(self):

        '''
        save_member method saves member objects into member_list
        '''

        Member.member_list.append(self)


    def __init__ (self, first_name, last_name, phone_number, username, email)

    '''
        __init__ method that helps us define properties for our objects.
    '''

    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = number
    self.username = username
    self.email = email