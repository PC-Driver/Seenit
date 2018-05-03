import crypt

#Register
reg_pass = input("Create password: ") #Input firealarm
salt = '2y' #To make sure that encryption remains the same everytime
#We can have salt as any value we want
# Note: If value of salt changes, the value of encryption also changes.
hashed = crypt.crypt(reg_pass,salt) #Hashed = Password (z) in encrypted form
print("Hashed version: "+hashed)
#We save this value in our database







#******************************************************************************************************************************************
#Database
#Let's say the encrypt value is saved in our database like this:
encrypt = '2yj8fYM5DQStQ' #This is the encrypted version of firealarm which is going to be saved after registration
print("The encrypted version saved in database: "+encrypt)

#******************************************************************************************************************************************
#Login
login_pass = input ("Enter Login Password: ")
login_hashed = crypt.crypt(login_pass,salt) #When the user logs in, the login password gets encrypted again
print("Login hashed version: "+login_hashed)

if(login_hashed==encrypt): #To compare the encrypted version of imput (firealarm with the encrypted version which is already there)
    print("Login Success")
else:
    print("Incorrect Password")

