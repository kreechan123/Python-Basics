
class UserRegistration:

    def __init__(self):
        self.id = 0
        self.user = []

    def add_user(self, first_name, last_name, full_name, email):
        
        id = self.id
        user = {}
        user['ID'] = id
        user['First Name'] = first_name
        user['Last Name'] = last_name
        user['Full Name'] = full_name
        user['Email'] = email
        
        # user = {'ID' : id,'First Name': first_name, 'Last Name' : last_name, 'Full Name' : full_name, 'Email' : email }
        
        self.user.append(user)
        
        self.id += 1

        return (self.user)

    def update_user(self, user_id, first_name, last_name, full_name, email):

        for x in range(len(self.user)):
            if self.user[x]['ID'] == user_id:
                self.user[x]['First Name'] = first_name
                self.user[x]['Last Name'] = last_name
                self.user[x]['Full Name'] = full_name
                self.user[x]['Email'] = email

        return (self.user)

    def delete_user(self, user_id):

        for x in range(len(self.user)):
            if self.user[x]['ID'] == user_id:
                del self.user[x]
                break


    def display(self):
        return (self.user)


# user = UserRegistration("Darryl", "Diapolet", "Darryl Diapolet", "dar.diapolet@gmail.com")

user = UserRegistration()

choice = 1

while choice != 0:
    print("0. Exit")
    print("1. Add User")
    print("2. Show list of users")
    print("3. Remove User")
    print("4. Update User")

    choice = int(input("Enter choice: "))

    if choice == 1:
        first_name = raw_input("Enter First Name: ")
        last_name = raw_input("Enter Last Name: ")
        full_name = raw_input("Enter Full Name: ")
        email = raw_input("Enter Email: ")

        user.add_user(first_name, last_name, full_name, email)

        print("List: ", user.display())
    elif choice == 2:

        print("User: ", user.display())

    elif choice == 3:
        n = int(input("Enter ID to remove user: "))
        user.delete_user(n)
        print("List: ", user.display())
 
    elif choice == 4:
        n = int(input("Enter ID to update user: "))
        first_name = raw_input("Enter First Name: ")
        last_name = raw_input("Enter Last Name: ")
        full_name = raw_input("Enter Full Name: ")
        email = raw_input("Enter Email: ")

        user.update_user(n, first_name, last_name, full_name, email)
        print("List: ", user.display())

    elif choice == 0:
        print("Exiting!")

    else:
        print("Invalid choice!!")