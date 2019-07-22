from credentials import Credentials
from user import User
import random

#new user# 
#create your account#
def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user

    #save user#
def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

     #search user#

def find_user(username):
    '''
    method for find user using username
    '''
    return User.find_user(username)

     # create credentials#

def create_credentials(account, email, password):
    '''
    method credentials details
    '''
    new_credential = Credentials(account, email, password)
    return new_credential

    #save credential#

def save_credential(credential):
    '''
    save credentials
    '''
    credential.save_credential()

    #dispaly credential#

def display_credential():
    '''
    method to display all the saved credentials
    '''
    return Credentials.display_credential()

