import getpass
import os
import time
import datetime
from tkinter import *
import yagmail


class person(): #class for new users
    def __init__(self, gender, bio, password, birthYear, prefPartnerBirthYear, partnerGender, 
                 collegeYear, username, major, email,  Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, timestamp,
                 recent1, recent2, recent3, blockedList):
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
        self.email=email
        self.password=password
        self.username=username
        self.gender=gender
        self.major=major
        self.birthYear=birthYear
        self.partnerGender=partnerGender
        self.collegeYear=collegeYear
        self.prefPartnerBirthYear=prefPartnerBirthYear        
        self.timestamp=timestamp
        self.recent1 = recent1
        self.recent2 = recent2
        self.recent3 = recent3
        self.blockedList = blockedList
        
    def viewProfile(self, master): #view profile
        #os.system('cls')
     
        root=Toplevel()
        root.title(self.username+"'s profile: \n")
        t=Text(master)
        t.insert(END, "Username: " + self.username+'\n')
        t.insert(END, "Major: " + self.major+'\n')
        t.insert(END, "Gender: " + self.gender+'\n')
        t.insert(END, "Biography: " + self.bio+'\n')
        t.insert(END, "Last time " + self.username + " logged in: " + self.timestamp+'\n')
        t.pack()
        return

    def changeTimestamp(self):
        timeStamp=time.time()
        self.timestamp=datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d')

    def editQuestion(self, questions): #edit questions
        for i in range(0, len(questions)):
            print(str((i+1))+". "+questions[i])
        change=input("Which question number would you like to change?\n")
        os.system('cls')
        change=int(change)
        if change==1:
            print(questions[0])
            print("1. Yes")
            print("2. No") 
            choice=int(input("Enter selection: "))
            self.Q1=choice
        elif change==2: 
            print(questions[1])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection:"))
            self.Q2=choice
        elif change==3:
            print(questions[2])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q3=choice
        elif change==4:
            print(questions[3])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q4=choice
        elif change==5:
            print(questions[4])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q5=choice
        elif change==6:
            print(questions[5])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q6=choice
        elif change==7:
            print(questions[6])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q7 = choice
        elif change==8:
            print(questions[7])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q8=choice
        elif change==9:
            print(questions[8])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q9 = choice
        elif change==10:
            print(questions[9])
            print("1. Yes")
            print("2. No")
            choice=int(input("Enter selection: "))
            self.Q10=choice
        else:
            print("Invalid question number")

    def viewAnswers(self, questions): #view answers
        os.system('cls')
        print(self.Q1)
        root=Toplevel()
        t=Text(root)
        t.insert(END, "1. "+questions[0]+'\n')
        if self.Q1=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "2. "+questions[1]+'\n')
        if self.Q2=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "3. "+questions[2]+'\n')
        if self.Q3=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "4. "+questions[3]+'\n')
        if self.Q4=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "5. "+questions[4]+'\n')
        if self.Q5=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "6. "+questions[5]+'\n')
        if self.Q6=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "7. "+questions[6]+'\n')
        if self.Q7=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "8. "+questions[7]+'\n')
        if self.Q8=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "9. "+questions[8]+'\n')
        if self.Q9=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.insert(END, "10. "+questions[9]+'\n')
        if self.Q10=="1":
            t.insert(END, "Yes\n")
        else:
            t.insert(END, "No\n")
        t.pack()

    def getMatches(self, students):
        os.system('cls')
        root=Toplevel()
        matches=[]
        for i in range(0,len(students)):
            points=0
            if self.username==students[i].username:
                continue
            if self.partnerGender!=students[i].gender:
                continue
            if self.Q1==students[i].Q1:
                points+=3
            if self.Q2==students[i].Q2:
                points+=3
            if self.Q3==students[i].Q3:
                points+=1
            if self.Q4==students[i].Q4:
                points+=2.5
            if self.Q5==students[i].Q5:
                points+=3
            if self.Q6==students[i].Q6:
                points+=1.5
            if self.Q7==students[i].Q7:
                points+=1.5
            if self.Q8==students[i].Q8:
                points+=1
            if self.Q9==students[i].Q9:
                points+=1
            if self.Q10==students[i].Q10:
                points+=1.5
            if points>=6:
                matches.append(students[i].username)
            if len(matches)>=10:
                break
        t=Text(root)
        for i in matches:
            t.insert(END, i+'\n')
        t.pack()
        return

    def sendMessage(self, student):
        userMsg=input("Enter the username of the user you wish to send a message to: ")
        for i in range(0,len(student)):
            if userMsg==student[i].username:
                userMsg=student[i]
                msg=input("Enter your message: ")
                yagmail.SMTP("titanmatchteam@gmail.com").send(userMsg.email, "You've received a message from "+self.username, msg)
                print("Message sent successfully")
                return
        print("Could not find user with that name")
        return

    def deactivateProfile(self, student, master):
        os.system('cls')
        master.withdraw()
        root=Toplevel()
        t=Text(root)
        for i in range(0, len(student)):
            if(self.username==student[i].username):
                #del student[i]
                t.insert(END, "Deactivation complete, click button to exit\n")
                t.pack()
                writeV(student) #update the change
                exitButton=Button(root, text="Exit program", command=lambda: exitLoop(master), bg="navy", fg="orange")
                exitButton.config(width=15)
                exitButton.pack()
                break
        master.deiconify
        return

    def editProfile(self):
        os.system('cls')
        editProf=Toplevel()
        def editUsername(self, editProf):
            newUName=input("Enter your new username: ")
            self.username=newUName
            editProf.destroy()
            print("Success!")
            return
        def editPassword(self, editProf):
            newPW=input("Enter your new password: ")
            self.password=newPW
            editProf.destroy()
            print("Success!")
            return
        def editEmail(self, editProf):
            newEmail=input("Enter your new email: ")
            self.email=newEmail
            editProf.destroy()
            print("Success!")
            return
        def editMajor(self, editProf):
            newMajor=input("Enter your new major: ")
            self.major=newMajor
            editProf.destroy()
            print("Success!")
            return
        def editGender(self, editProf):
            newGender=input("Enter your new gender: ")
            self.gender=newGender
            editProf.destroy()
            print("Success!")
            return
        def editBirthday(self, editProf):
            newBirthday=input("Enter your new birthday: ")
            self.birthday=newBirthday
            editProf.destroy()
            print("Success!")
            return
        def editPrefGender(self, editProf):
            newPrefGender=input("Enter your preferred partner gender: ")
            self.partnerGender=newPrefGender
            editProf.destroy()
            print("Success!")
            return
        eUnameButton=Button(editProf, text="Edit username", command=lambda: editUsername(self, editProf), bg="navy", fg="orange")
        eUnameButton.config(width=15)
        eUnameButton.pack()
        ePWButton=Button(editProf, text="Edit password", command=lambda: editPassword(self, editProf), bg="navy", fg="orange")
        ePWButton.config(width=15)
        eUnameButton.pack()
        eEmailButton=Button(editProf, text="Edit email", command=lambda: editEmail(self, editProf), bg="navy", fg="orange")
        eEmailButton.config(width=15)
        eEmailButton.pack()
        eMajorButton=Button(editProf, text="Edit major", command=lambda: editMajor(self, editProf), bg="navy", fg="orange")
        eMajorButton.config(width=15)
        eMajorButton.pack()
        eGenderButton=Button(editProf, text="Edit gender", command=lambda: editGender(self, editProf), bg="navy", fg="orange")
        eGenderButton.config(width=15)
        eGenderButton.pack()
        eBirthdayButton=Button(editProf, text="Edit birthday", command=lambda: editBirthday(self, editProf), bg="navy", fg="orange")
        eBirthdayButton.config(width=15)
        eBirthdayButton.pack()
        ePrefGenderButton=Button(editProf, text="Edit pref gender", command=lambda: editPrefGender(self,editProf), bg="navy", fg="orange")
        ePrefGenderButton.config(width=15)
        ePrefGenderButton.pack()
        editProf.mainloop()
        return
def load(student):
#<<splitlines() code>> used for storing elements of the loadVector into the variables above
#if we can make a person array we can write a for loop that write out each person
#into the txt file
#split lines lets us put each string into a vector. we can store each element into a data     
    bio = " "
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    Q5 = 0
    Q6 = 0
    Q7 = 0
    Q8 = 0
    Q9 = 0
    Q10 = 0
    email = " "
    password = " "
    username = " "
    gender = " "
    major = " "
    birthYear = " "
    partnerGender = " "
    collegeYear = " "
    prefPartnerBirthYear = " "
    timestamp= " "    
    finished = False    
    recent1 = None
    recent2 = None
    recent3 = None 
    blockedList = []  
    vectorIndex = 0
    read_file = open("output.txt", "r")
    loadVector = read_file.read().splitlines()
    vectorSize = len(loadVector) - 1
    p1 = (gender, bio, password, birthYear, prefPartnerBirthYear, partnerGender, collegeYear, username, major, email,  
          Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, timestamp, recent1, recent2, recent3, blockedList)

    while vectorSize - vectorIndex > 0:
        with open('output.txt') as read_file:
            #comment: setting each value to the element of the index
            blockedList = []
            finished = False
            bio = loadVector[vectorIndex]
            print (loadVector[vectorIndex])
            vectorIndex+=1
            Q1 = loadVector[vectorIndex]
            vectorIndex+=1
            Q2 = loadVector[vectorIndex]
            vectorIndex+=1
            Q3 = loadVector[vectorIndex]
            vectorIndex+=1
            Q4 = loadVector[vectorIndex]
            vectorIndex+=1
            Q5 = loadVector[vectorIndex]
            vectorIndex+=1
            Q6 = loadVector[vectorIndex]
            vectorIndex+=1
            Q7 = loadVector[vectorIndex]
            vectorIndex+=1
            Q8 = loadVector[vectorIndex]
            vectorIndex+=1
            Q9 = loadVector[vectorIndex]
            vectorIndex+=1
            Q10 = loadVector[vectorIndex]
            vectorIndex+=1
            email = loadVector[vectorIndex]
            vectorIndex+=1
            password = loadVector[vectorIndex]
            vectorIndex+=1
            username = loadVector[vectorIndex]
            vectorIndex+=1
            gender = loadVector[vectorIndex]
            vectorIndex+=1
            major = loadVector[vectorIndex]
            vectorIndex+=1
            birthyear = loadVector[vectorIndex]
            vectorIndex+=1
            partnerGender = loadVector[vectorIndex]
            vectorIndex+=1
            collegeYear = loadVector[vectorIndex]
            vectorIndex+=1
            prePartnerBirthYear = loadVector[vectorIndex]
            vectorIndex +=1 
            timestamp = loadVector[vectorIndex]
            vectorIndex += 1
            recent1 = loadVector[vectorIndex]
            vectorIndex += 1
            recent2 = loadVector[vectorIndex]
            vectorIndex += 1
            recent3 = loadVector[vectorIndex]
            print ("the last thing before")
            print (loadVector[vectorIndex])
            vectorIndex = vectorIndex + 1
            if loadVector[vectorIndex] == 'qUiCK':
                print("won't get added to list! : )")           
            print ("begin blockedList")          
            while (loadVector[vectorIndex] != 'qUiCK' and finished != True):
                if loadVector[vectorIndex] != "qUiCK":                  
                    blockedList.append(loadVector[vectorIndex])
                    vectorIndex += 1
                    
                    if loadVector[vectorIndex] == 'qUiCK':
                       
                        print (vectorSize)
                        finished = True
            
            if loadVector[vectorIndex] == "qUiCK":    
                vectorIndex += 1        
                               
            p1 = person(gender, bio, password, birthYear, prefPartnerBirthYear, partnerGender, collegeYear, username, 
                        major, email,  Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, timestamp, recent1, recent2, recent3, blockedList)
            student.append(p1)
                   

    else:
        read_file.close()
    
    
    
def writeV(student):
    write_file = open("output.txt", "w")
    for i in range(len(student)):
        write_file.write(str(student[i].bio) + "\n" +
                         str(student[i].Q1) + "\n" +
                         str(student[i].Q2) + "\n" +
                         str(student[i].Q3) + "\n" +
                         str(student[i].Q4) + "\n" +
                         str(student[i].Q5) + "\n" +
                         str(student[i].Q6) + "\n" +
                         str(student[i].Q7) + "\n" +
                         str(student[i].Q8) + "\n" +
                         str(student[i].Q9) + "\n" +
                         str(student[i].Q10) + "\n" +
                         str(student[i].email) + "\n" +
                         str(student[i].password) + "\n" +
                         str(student[i].username) + "\n" +
                         str(student[i].gender) + "\n" +
                         str(student[i].major) + "\n" +
                         str(student[i].birthYear) + "\n" +
                         str(student[i].partnerGender) + "\n" +
                         str(student[i].collegeYear) + "\n" +
                         str(student[i].prefPartnerBirthYear) + "\n" +
                         str(student[i].timestamp) + "\n" +
                         str(student[i].recent1) + "\n" +
                         str(student[i].recent2) + "\n" +
                         str(student[i].recent3) + "\n")
        for j in range(0, len(student[i].blockedList)):
            write_file.write(str(student[i].blockedList[j]) + "\n" )
        write_file.write("qUiCK" + "\n")
    write_file.close()              
        
def login(loginUser, loginPass, student): #login to the database
    if not student: #checks if list is empty
        print("No users in database")
        return
    for i in range(0, len(student)):
        if loginUser==student[i].username:
            if loginPass==student[i].password:
                return student[i]
    return False

def forgotPassword(student):
    forgot=input("Enter your account name: ")
    for i in range(0, len(student)):
        if forgot==student[i].username:
            forgot=student[i]
            yagmail.SMTP("titanmatchteam@gmail.com").send(forgot.email, "Forgotten password", "Hey there! Here is your password: " + forgot.password)
            print("An email has been sent with your password")
            return
    print("Account not found")
    return

def newUser(master, student, questions): #new user will enter in these choices and they will be passed to class
    timeStamp=time.time()
    global userIn
    answers=[0]*11
    sUserName=input("Enter username: ")
    sPassword=getpass.getpass("Enter password: ")
    sEmail=input("Enter your CSUF email: ")
    if "@csu.fullerton.edu" not in sEmail:
        emailcorrect=False
        while emailcorrect==False:
            sEmail=input("Invalid email, must be a CSUF email, try again: ")
            if "@csu.fullerton.edu" not in sEmail:
                continue
            emailcorrect=True
    sBirthYear=input("Enter your birth year: ")
    sGender=input("Enter gender: ")
    sMajor=input("Enter major: ")
    sCollegeYear=input("What year are you in college? ")
    sPartnerGender=input("What gender are you looking for (m/m, m/f, f/m, ff)? ")
    sPrefPartnerBirthYear=input("Would you like your partner to be older or younger than you? ")
    sBio=input("Describe yourself! ")
    os.system('cls')
    choice=input("Would you like to answer the questions now or answer them later? Y/N: ")
    if choice[0].lower() == 'y':
        i=0
        while i<len(questions):
            print(str(i+1)+". "+str(questions[i]))
            i+=1
            print("1. Yes")
            print("2. No")
            selection=int(input("Enter selection: "))
            if selection>2 or selection<1:
                print("Invalid answer, try again!")
                i-=1
            #should we reprint the questions without clearing the screen? It will look cluttered?
            # perhaps a new line of dashes and the word retry question in CAPS? 
            else:
                answers[i]=selection
                os.system('cls')
        blockedList = []
        sNewUser=person(sGender, sBio, sPassword, sBirthYear, sPrefPartnerBirthYear, sPartnerGender, sCollegeYear, sUserName, sMajor, sEmail, answers[1], answers[2], answers[3], answers[4], answers[5], answers[6], answers[7], answers[8], answers[9],answers[10], datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d'),
                        None, None, None, blockedList) #we need to default recent to None for blockedUser I/O to work
        student.append(sNewUser)
        userIn = student[len(student)-1]
        writeV(student)
        master.destroy()
    elif choice[0].lower() == 'n':
        blockedList = []
        sNewUser=person(sGender, sBio, sPassword, sBirthYear, sPrefPartnerBirthYear, sPartnerGender, sCollegeYear, sUserName, sMajor, sEmail,None,None,None,None,None,None,None,None,None,None, datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d'),
                        None, None, None, blockedList) #we need to default recent to None for blockedUser I/O to work
        student.append(sNewUser)
        userIn = student[len(student)-1]
        #writeV(student) will only work if we default the multiple choice beforehand
        master.destroy()

def blockUser(student, master):
    os.system('cls')
    findUserName=input("Enter name of user you wish to block : ")
    for i in range(0, len(student)):
        if student[i].username == findUserName:            
            userIn.blockedList.append(findUserName)
            writeV(student)
            #keep appending to not lose blocked users
            print("User has been blocked.")
            return
    print("User not found")
    return

def searchUser(student, master):
     os.system('cls')
     findUserName=input("Enter name of user you wish to search for: ")
     for i in range(0, len(student)):
         if student[i].username==findUserName:
             for j in range(0, len(student[i].blockedList)):
                 if student[i].blockedList[j] == userIn.username:
                     print("User not found" + "\n" + "...")
                     return
             
             student[i].viewProfile(master)
             print (student[i].username)
             print (userIn.username)
             print (student[i].recent1)
             if student[i].username != userIn.username:
                if student[i].recent1 == " ":
                    student[i].recent1 = userIn.username
                    print (student[i].recent1)
                    writeV(student)                   
                    return 
                if student[i].recent2 == " ":
                    student[i].recent2 = userIn.username
                    writeV(student)                   
                    return 
                if student[i].recent3 == " ":
                    student[i].recent3 = userIn.username
                    writeV(student)                   
                    return 
                if student[i].recent1 != " " and student[i].recent2 != " " and student[i].recent3 != " ":
                    student[i].recent1 = student[i].recent2 
                    student[i].recent2 = student[i].recent3
                    student[i].recent3 = userIn.username   
             writeV(student)                   
             return 
     print("User not found")
     return

def returningUser(master, student):
     global userIn
     loginUser=input("Enter username: ") 
     loginPass=getpass.getpass("Enter your password: ")
     userIn=login(loginUser, loginPass, student)
     if userIn==False: #if the input comes back false, user does not get to login
        print("wrong user/pass")
     master.destroy()
     os.system('cls')
     print (userIn.blockedList)
     return

def reportUser(master, student):
     choice=input("What is the username of the person you would like to report? ")
     report=input("Please describe the problems you have had with this person: ")
     for i in range(0, len(student)):
         if choice==student[i].username:
             yagmail.SMTP("titanmatchteam@gmail.com").send("titanmatchteam@gmail.com", "Report filed by "+userIn.username, report)
             print("Report has been successfully submitted.")
             return
     print("User not found")
     return

def exitLoop(master):
    master.destroy()
    sys.exit()

def main(): #end of menu loop
    master=Tk()
    timeStamp=time.time()
    master.title("TitanMatch")
    popUp=Toplevel()
    master.withdraw()
    student=[] #list of student objects
    load(student)
    #initTests(student)
    viewMatch=[]
    loginOver=False
    questions=["Do you want to eventually have children?", "Do you have kids?", "Was your longest relationship longer than a year?", "Is religion important to you?", "Would you consider dating someone outside your faith?", "Do you smoke?", "Do you drink more than once a week?", "Do you exercise?", "Do you prefer if your partner is taller than you?", "Do you enjoy discussing politics?"]
    returnUserButton=Button(popUp, text="Returning User", command=lambda: returningUser(popUp, student), bg="navy", fg="orange")
    returnUserButton.config(width=15)
    returnUserButton.pack()
    newUserButton=Button(popUp, text="New User", command=lambda: newUser(popUp, student, questions), bg="navy", fg="orange")
    newUserButton.config(width=15)
    newUserButton.pack()
    forgotPWButton=Button(popUp, text="Forgot password", command=lambda: forgotPassword(student), bg="navy", fg="orange")
    forgotPWButton.config(width=15)
    forgotPWButton.pack()
    exitLoginButton=Button(popUp, text="Exit", command=lambda: exitLoop(popUp), bg="navy", fg="orange")
    exitLoginButton.config(width=15)
    exitLoginButton.pack()
    popUp.wait_window()
    master.deiconify()
    userIn.changeTimestamp()
    writeV(student)
    returnUserButton.pack_forget()
    newUserButton.pack_forget()
    profButton=Button(master, text="View profile", command=lambda: userIn.viewProfile(master), bg="navy", fg="orange")
    profButton.config(width=15)
    profButton.pack()
    viewMatchButton=Button(master, text="View Matches", command=lambda: userIn.getMatches(student), bg="navy", fg="orange")
    viewMatchButton.config(width=15)
    viewMatchButton.pack()
    sendMsgButton=Button(master, text="Message a user", command=lambda: userIn.sendMessage(student), bg="navy", fg="orange")
    sendMsgButton.config(width=15)
    sendMsgButton.pack()
    b=Button(master, text="Edit questions", command=lambda: userIn.editQuestion(questions), bg="navy", fg="orange")
    b.config(width=15)
    b.pack()
    searchButton=Button(master, text="Search for user", command=lambda: searchUser(student, master), bg="navy", fg="orange")
    searchButton.config(width=15)
    searchButton.pack()
    searchButton=Button(master, text="Block user", command=lambda: blockUser(student, master), bg="navy", fg="orange")
    searchButton.config(width=15)
    searchButton.pack()
    viewAnswersButton=Button(master, text="View answers", command=lambda: userIn.viewAnswers(questions), bg="navy", fg="orange")
    viewAnswersButton.config(width=15)
    viewAnswersButton.pack()
    editProfileButton=Button(master, text="Edit profile", command=lambda: userIn.editProfile(), bg="navy", fg="orange")
    editProfileButton.config(width=15)
    editProfileButton.pack()
    reportButton=Button(master, text="Report user", command=lambda: reportUser(master, student), bg="navy", fg="orange")
    reportButton.config(width=15)
    reportButton.pack()
    deactivateProfileButton=Button(master, text="Deactivate profile", command=lambda: userIn.deactivateProfile(student, master), bg="navy", fg="orange")
    deactivateProfileButton.config(width=15)
    deactivateProfileButton.pack()
    exitButton=Button(master, text="Exit", command=lambda: exitLoop(master), bg="navy", fg="orange")
    exitButton.config(width=15)
    exitButton.pack()
    master.mainloop()

main()