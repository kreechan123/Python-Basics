class User(object):
    def __init__ (self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def display_users(self):
        return (self)

    # def get_fullname(self):
    #     retunrn

    # def add_user(self):
    #     return "{} is {} years old".format(self.name, self.age)


    # def showlist():
        # stud1 = UserRegistration("Christian", "Librando", "Christian Librando", "librandochris@gmail.com")

        # print("Name: {}.".format(stud1.fname))
        # print("Last Name: {}.".format(stud1.lname))
        # print("Full Name: {}.".format(stud1.fullname))
        # print("Email Add: {}.".format(stud1.email))

list_of_users = []

def register():
    fname = raw_input("Enter Firstname: ")
    lname = raw_input("Enter Last Name: ")
    email = raw_input("Enter Email: ")

    add = User(fname, lname, email)

    list_of_users.append(add)

    print list_of_users[0].fname, list_of_users[0].lname, list_of_users[0].email

        
        # insert newly created user to users list

    # def show_all_users():
    #     for user in list_of_users:
    #         print(user.get_fullname())


choice = 1

while choice != 0:
    print("0. Exit")
    print("1. Add User")
    print("2. Show list of users")
    print("3. Remove User")
    print("4. Update User")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register()



