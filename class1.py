
#simple person class + inheritance
class Person():
    def __init__(self, firstname, lastname, age, height, address, friends):
        #Initialize attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.address = address
        self.friends = friends
    
    def single(self):
        print(self.firstname + " is single.")

    def married(self):
        print(self.firstname + " is married.")
    
    def friend_count(self):
        friend = self.firstname + " has " + str(self.friends) + " friend(s)."
        return friend

    #Method to modify
    def update_friends(self, new_friends):
        self.friends = new_friends
    
    def details(self):
        person_details = self.firstname.title() + " " + self.lastname.title() + " is pretty " + self.height + "."
        return person_details 

class Someone(Person):
    def __init__(self, firstname, lastname, age, height, address, friends, status):
        super().__init__(firstname, lastname, age, height, address, friends)
        self.status = status
    
    def currentStatus(self):
        return self.firstname + " " + self.lastname + " is " + self.status + "."

    def details(self):
        return "Someone else is called " + self.firstname + " " + self.lastname + "." 

someone_else = Someone('New', 'Guy', 21, 'short', 'Accra', 7, "affluent")
#print(someone_else.details())
#print(someone_else.currentStatus())


#Creating an instance of the class
#new_person = Person('Kabaka', 35, 'Ikorodu')
# another_person = Person('Kabaka', 'Jnr', 13, 'short', 'Ikorodu',0)

# #Calling class methods
# # new_person.single()
# print(another_person.details())
# print(another_person.friend_count())

# #Modifying attributes
# another_person.friends = 3
# print(another_person.friend_count())

# another_person.update_friends(5)
# print(another_person.friend_count())