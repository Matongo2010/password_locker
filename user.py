class User:

    """
    Class that generates new instances of users
    """

    user_list = [] # Empty user list

    # Init method up here


    def __init__ (self,username, password):

        '''
        __init__ method that helps us define properties for our objects.
        '''

    
        self.username = username
        self.password = password

        #save multiple#

    def save_user(self):
        User.user_list.append(self)

        #delete user#

    def delete_user(self):

        '''
        delete a user account
        '''
        User.user_list.remove(self)

        #find user#

        @classmethod
        def find_user(cls, username):
            '''
            find username using search terms
            '''
            for user in cls.user_list:
                if user.username == username:
                    return  user