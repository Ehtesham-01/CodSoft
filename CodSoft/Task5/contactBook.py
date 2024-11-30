#Contact Book
contact={}
def add_contact():
    name=input("Enter name= ")
    phone=int(input("Enter phone number= "))
    email=input("Enter E-mail (like abcd123@gmail.com) = ")
    address=input("Enter Address= ")
    contact[name]={"Phone":phone,"E-mail":email,"Address":address}
    print(f"{name} contact added successfully..")
def view_contact_list():
    permission=input("You want to check your contact list?('yes'/'no')=")
    if permission.strip().lower() == "yes" :
        if contact:
            for name, info in contact.items():
                print(f"Name:{name},Phone:{info['Phone']},E-mail:{info['E-mail']},address:{info['Address']}")
        else:
            print("contact not found..")
    else:
        print("You didn't give permisson..") 
def search_contact():
    name=input("Enter name= ")
    if name in contact:
        print(f"Name:{name},Phone:{contact[name]['Phone']},E-mail:{contact[name]['E-mail']},address:{contact[name]['Address']}")
    else:
                print("contact not found..")
      
def update_contact():
    name=input("Enter name= ")
    if name in contact:
        phone=int(input("Enter new phone number you want to update: "))
        email=input("Enter new email= ")
        address=input("Enter new Address= ")
        contact[name]={"Phone":phone,"E-mail":email,"Address":address}
        print(f"{name} contact was successfully updated.")
    else:
        print("contact not found..")
def delete_contact():
    name= input("Enter name= ")
    if name in contact:
        del contact[name]
        print(f"{name} contact successfully deleted")
    else:
        print("contact not found..")
while True:
    print("----Contact List----")
    print("   1.Add contact")
    print("   2.View contact list")
    print("   3.search contact")
    print("   4.update contact")
    print("   5.delete contact")
    choice=int(input("Enter choice= "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact_list()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        print("Invalid choice..")