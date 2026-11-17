import getpass

name = input('User name :')
pass_code = getpass.getpass("Password :")

if name == "Fiddel" and  pass_code == "Thesecret":
    print(f'welcome {name}')
else:
    print("Unautheticated User.")
