import getpass

class person(): #class for new users
    def __init__(self, gender, bio, password, username, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10):
        self.bio=bio
        self.Q1=Q1
        self.Q2=Q2
        self.Q3=Q3
        self.Q4=Q4
        self.Q5=Q5
        self.Q6=Q6
        self.Q7=Q7
        self.Q8=Q8
        self.Q9=Q9
        self.Q10=Q10
        self.password=password
        self.username=username
        self.gender=gender
    def viewProfile(self): #view profile
        print(self.username)
        print(self.bio)

#if we can make a person array we can write a for loop that write out each person
#into the txt file

def login(loginUser, loginPass, student): #login to the database
    for i in range(0, len(student)):
        if loginUser==student[i].username:
            if loginPass==student[i].password:
                return student[i]
    return False

def menu(): #print menu choices
    print("1. View Profile")
    print("2. View Matches")
    print("3. Edit Profile")
    print("4. Exit")

def newUser(student): #new user will enter in these choices and they will be passed to class
    sUserName=input("Enter username: ")
    sPassword=getpass.getpass("Enter password: ")
    sGender=input("Enter gender: ")
    sBio=input("Describe yourself! ")
    return

def main():


    exit=False #end of menu loop
    student=[] #list of student objects
    newUse=person("male", "this is a bio", "testPass", "testUser", None, None, None, None, None, None, None, None, None, None) #used only for tests, will be removed in final product
    student.append(newUser) #will be removed in final product
    print("1. Returning User")
    print("2. New User")
    choice=int(input("Enter choice: "))
    if choice==1: #a returning user enters username and password
        loginUser=input("Enter username: ") 
        loginPass=getpass.getpass("Enter your password: ")
        userIn=login(loginUser, loginPass, student)
        if userIn==False: #if the input comes back false, user does not get to login
            print("wrong user/pass")
        else:
            while exit == False: #else the user gets prompted with menu
                menu()
                choice=int(input("Enter choice: "))
                if choice==1:
                    None
                elif choice == 2:
                    None
                elif choice==3:
                    None
                elif choice==4:
                    exit = True
    if choice==2:
        newUser(student) #new user goes to enter their info then gets promped with the menu
        while exit==False:
            menu()
            choice=(input("Enter choice: "))
            if choice== "1":  
                None
            elif choice=="2":
                None
            elif choice=="3":
                None
            elif choice=="4":
                #start writing data into a textFile
                #inspired by the KhaMain.cpp file for library catalogs
#                write_file = open("data.txt", "w") <- creates the writing document
#                for i in range(len(personArray)-1):
#                   write_file.write(str(personArray[i].bio + " ")
#                   write_file.write(str(personArray[i].Q1 + " ")
#                   write_file.write(str(personArray[i].Q2 + " ")
#                   write_file.write(str(personArray[i].Q3 + " ")
#                   write_file.write(str(personArray[i].Q4 + " ")
#                   write_file.write(str(personArray[i].Q5 + " ")
#                   write_file.write(str(personArray[i].Q6 + " ")
#                   write_file.write(str(personArray[i].Q7 + " ")
#                   write_file.write(str(personArray[i].Q8 + " ")
#                   write_file.write(str(personArray[i].Q9 + " ")
#                   write_file.write(str(personArray[i].Q10 + " ")
#                   write_file.write(str(personArray[i].password + " ")
#                   write_file.write(str(personArray[i].username + " ")
#                   write_file.write(str(personArray[i].gender + " ")
#                   write_file.close()

                exit = True
            else:
                print("Invalid answer - please enter numbers")

main()