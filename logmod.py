USERNAME="admin"
PASSWORD="1234"
def login(user,pwd):
  if user == USERNAME and pwd == PASSWORD:
    return true
  else:
    return False

print("---Login System--")
u=input("Enter Username:")
p=input("enter password:")
if login(u,p):
  print("Login successfull welcome",u)
else:
  print("Invalid username or password")
  
