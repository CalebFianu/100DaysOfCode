import json

person = {
    "names": {
        "First Name": 'Caleb',
        "Last Name": 'Fianu'
    }   
}

more_data = {"age":"10"}


#Serializing
with open('Sample.json', 'w') as s:
    json.dump(person,s)

#Deserializing
with open('Sample.json', 'r') as d:
    des = json.load(d)
    des.update(more_data)
    print(des)
    print("Deserialization complete.")