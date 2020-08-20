password = input("Password: ")
while len(password) < 5:
    print("Password must be 5 characters minimum")
    password = input("Password: ")
print(len(password)*"*")
