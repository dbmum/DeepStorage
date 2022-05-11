import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def main():   
    data_base = DataBase()
    choice = 0
    
    while choice != '6':

        if data_base.is_authenticated :
            print("\n1. View feed\
                \n2. Make Post\
                \n3. Update Password\
                \n4. Delete your account\
                \n5. Log Off\
                \n6. Exit")
        
            choice = input('Make Selection, type \"6\" to exit the app\n')

            if choice =='1':
                data_base.ViewFeed()
            
            
            if choice == '2':
                data_base.MakePost()
            
            if choice == '3':
                data_base.UpdatePassword()
            
            if choice == '4':
                data_base.DeleteUser()
            
            if choice == '5':
                data_base.is_authenticated = False
        
        else:
            print("\n1. Make User\
                \n2. Log In\
                \n6. Exit")
            
            choice = input('Make Selection, type \"6\" to exit the app\n')
            
            if choice == '1':
                data_base.MakeUser()
            
            if choice == '2':
                data_base.Authenticate()

class DataBase:
    
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = 'serviceAccountkey.json'
        firebase_admin.initialize_app(credentials.ApplicationDefault(),{
            'projectId': "deep--storage",
        })

        self.db = firestore.client()
        # self.selfauth = firebase.auth()
        # self.storage = firebase.storage()
        self.current_user = None
        self.is_authenticated = False

    def ViewFeed(self):
        results = self.db.collection('posts').get()
        for result in results:
            data = result.to_dict()
            print(data['user'])
            print(data['post'])
            print(data['time'])
            print("--------")


    def MakeUser(self):
        username = input('User Name: ')
        password = input('Password: ')
        result = self.db.collection('users').document(username).get()
        if result.exists:
            print('User already exists')
            return
        data = {'user':username,
                "password": password}
        self.db.collection('users').document(username).set(data)

    def MakePost(self):
        post = input('Make post here:\n')
        data = {'user': self.current_user,
                'post': post,
                'time': firestore.SERVER_TIMESTAMP}
        self.db.collection('posts').add(data)
            

    def UpdatePassword(self):
        new_password = input('What would you like to change your password to?\n')
        result = self.db.collection('users').document(self.current_user).get()

        data = result.to_dict()
        data['password'] = new_password

        self.db.collection('users').document(self.current_user).set(data)

    def DeleteUser(self):
        user = input('to delete your account FOREVER, type your username:\n')
        user_check = self.db.collection('users').document(user).get()

        if user_check.exists and user == self.current_user:
            user_check.reference.delete()

            print(f'User ~~{user}~~ has been deleted')

            self.is_authenticated = False
        
            
                
    def Authenticate(self):
        user = input('User Name: ')
        password = input('Password: ')
        user_check = self.db.collection('users').document(user).get()
        if user_check.exists:
            data = user_check.to_dict()
            if password == data['password']:
                self.current_user = user
                self.is_authenticated = True
            else:  
                print('USER DOES NOT EXIST')

main()