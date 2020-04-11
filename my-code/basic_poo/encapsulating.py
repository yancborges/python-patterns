class dataBase:

    def __init__(self):
        self.__data = {}


    def add_user(self, _id, name):
        if 'users' not in self.__data:
            self.__data['users'] = {_id: name}
        else:
            self.__data['users'].update({_id: name})


    def delete_user(self, _id):
        del self.__data['users'][_id]

        
db = dataBase()
db.add_user(1, 'A')
db.add_user(2, 'B')
db.add_user(3, 'C')
print(db.__data)