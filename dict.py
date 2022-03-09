newdict = {'key': 'value', 'value': 100, 100: 'Another 100'}
# Accessing values in the dictionary
print(newdict)
print(newdict['key'])
print(newdict['value'])

# Accessing values in the dictionary but with the get() method this time
print(newdict.get(100))

# Editing the value using it's corresponding key
newdict['key'] = 'new value'
print(newdict['key'])

# Removing values from a dictionary using their keys
del newdict[100]
print(newdict)

# looping through key-value pairs
for key, value in newdict.items():
    print("\nKey: " + key)
    # Error because one of the values was an int and we couldn't concatenate. Fixed though!
    print("Value: " + str(value))

# looping through keys
print("Keys:")
for key in newdict.keys():
    print(key)

# looping through values
print("Values:")
for val in newdict.values():
    print(val)
