import getpass


def get_input():
    first_name = input("Enter your name :")
    pass_code = getpass.getpass('Pass code :')
    return first_name ,pass_code

def Authentication(name ,pass_code):
    if name == "Fiddel" and pass_code =="Thesecret":
        print(f'Hello {name} welcome.')
    else:
        print("unautheticated User.")
        
if __name__ == "__main__":
    username, password  =  get_input()
    Authentication(username,password)
    

