#from class1 import Person, Someone
import class1 as c1

new_person = c1.Person('Pierre', 'Gasly', 25, 'tall', 'AlphaTauri', 1)
someone_again = c1.Someone('Lando', 'Norris', 24, 'short', 'Aston Martin', 3, 'affluent')

print(new_person.friend_count())
print(someone_again.currentStatus())