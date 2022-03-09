import json

#json string
person = '{"firstname": "New", "lastname": "Person", "age": "3"}'

#converting json to dictionary
person_dict = json.loads(person)
print(person_dict)
print(type(person_dict))
print("\n")


person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))