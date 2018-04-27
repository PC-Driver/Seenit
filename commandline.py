def print_menu():
        #MENU DESIGN!
        print (33* "-", "MENU" , 33 * "-")
        print( "|", 30 * " ", "insert", 30 * " ", "|", )
        print( "|", 30 * " ", "modify", 30 * " ", "|", )
        print( "|", 30 * " ", "delete", 30 * " ", "|", )
        print( "|", 30 * " ", "exit", 32 * " ", "|", )
        print (72* "-")

def insert():
    #insert sql commands go here
    print("you chose insert") 
def modify():
    #modify sql commands go here
    print("you chose modify")
def delete():
    #delete sql commands go here
    print("you chose delete")

loop = True

while True:
    print_menu()
   
    selection = input("\n") #for administrator - enter 0 to exit program
    if selection  == "insert":
        insert()
    elif selection  == "delete":
        delete()
    elif selection  == "modify":
        modify()
    elif selection  == "exit":
        print ("Thank you, and goodbye!")
        exit()
    else:
       print("we're sorry you entered something not on the menu. Please try again.")
 
