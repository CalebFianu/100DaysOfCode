# Quitting a program using a while loop

prompt = "To quit this program enter 'q'"
prompt += "\nEnter a letter: "
message = " "

# while message != 'q':
#     message = input(prompt)
#     print(message)

# Using 'flags'. Basically makes the while loop simpler

# active = True
# while active:
#     message = input(prompt)

#     if message == 'q':
#         active = False
#     else:
#         print(message)

# Using a break statement
while True:
    message = input(prompt)
    if message == 'q':
        break
    else:
        print(message)

# And now continue...
new_message = 0
while new_message < 10:
    new_message += 1
    if new_message % 2 == 0:
        continue
print("new_message: " + str(new_message))
