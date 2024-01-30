

def signup(user_dict):
    username=input("enter your username :")
    password=input("enter your password :")
    if username in user_dict:
        print("your are already registerd ")
    else:
        print("registrion succefully ")
        user_dict.update({username:password})
        


def login(user_dict ):
    username=input("enter your username :")
    password=input("enter your password")
    #user=user_dict
    #if username in user and user[username] == user[password]:
    if user_dict[username] == password : 
        print("login succefully")
    else:
        print("plase enter valid details")  


def forget(user_dict):
    username=input("enter your username")
    if username in user_dict:
        password=input("enter your password")
        comfrom_password=input("enter your password ")
        if password==comfrom_password:
            user_dict[username]=password
        print("password changed succfully")
    else:
        print("Please enter a valid details")

user_dict={}
while True:
    print("\n1. Signup\n2. Login\n3. Reset Password\n4. Exit")
    choice=input("enter your choice: ")
    if choice=="1":
        signup(user_dict)
    elif choice=="2":
        login(user_dict)
    elif choice=="3":
        forget(user_dict)
    else:
        choice=="4"
        break
    
