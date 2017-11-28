import os
import time
import datetime
from random import SystemRandom
from random import*
import random
from tkinter import *
import yagmail
#from PIL import ImageTk, Image
import urllib
import urllib.request
import string

class person(): #class for new users
    def __init__(self, gender, bio, password, birthYear, prefPartnerBirthYear, partnerGender, collegeYear, username, major, email,  Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, 
                 timestamp, recent1, recent2, recent3, blockedList):
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
        self.blockedList = blockedList
        self.timestamp=timestamp      
        self.recent3=recent3
        self.recent2=recent2
        self.recent1=recent1
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global j
        global k
        global l
        global m
        global n
        global findLogin
        global findPassword
        
    def viewProfile(self): #view profile
        root=Toplevel()
        root.title(self.username+"'s profile: \n")
        #t=Text(root)
        #t.insert(END, "Username: " + self.username+'\n')
        #t.insert(END, "Major: " + self.major+'\n')
        #t.insert(END, "Gender: " + self.gender+'\n')
        #t.insert(END, "Biography: " + self.bio+'\n')
        #t.insert(END, "Last time " + self.username + " logged in: " + self.timestamp+'\n')
        #t.grid(row=0, sticky=S)
        label1=Label(root, text="Username: "+self.username+'\n')
        label1.grid(row=0, sticky=S)
        label2=Label(root, text="Major: "+self.major+'\n')
        label2.grid(row=1, sticky=S)
        label3=Label(root, text="Gender: "+self.gender+'\n')
        label3.grid(row=2, sticky=S)
        label4=Label(root, text="Biography: "+self.bio+'\n')
        label4.grid(row=3, sticky=S)
        label5=Label(root, text="Last time "+self.username+" logged in: "+self.timestamp+'\n')
        label5.grid(row=4, sticky=S)
        return

    def changeTimestamp(self):
        timeStamp=time.time()
        self.timestamp=datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d')

    def editQuestion(self, questions): #edit questions, maybe turn make them like the ones in new user, default value on option menu would be users current answer.
        def findChange(self, questions, root, but,a,b,c,d,e,f,g,h,x,y,label1,label2,label3,label4,label5,label6,label7,label8,label9,label10):
            Label(root, text="Success!").grid(row=10, sticky=S)
            but.destroy()
            self.Q1=a.get()
            self.Q2=b.get()
            self.Q3=c.get()
            self.Q4=d.get()
            self.Q5=e.get()
            self.Q6=f.get()
            self.Q7=g.get()
            self.Q8=h.get()
            self.Q9=x.get()
            self.Q10=y.get()
        root=Toplevel()
        #t=Text(root)
        #for i in range(0, len(questions)):
        #    t.insert(END, str(i+1)+". "+questions[i]+"\n")
        #t.insert(END, "\n")
        #t.insert(END, "Which question number would you like to change?")
        #image=Image.open("C:\\Users\\kylej\\Desktop\\tuffy.png")
        #bImage=ImageTk.PhotoImage(image)
        #bLabel=Label(root, image=bImage)
        #bLabel.place(x=0, y=0, relwidth=1, relheight=1)
        label1=Label(root, text="1. "+questions[0])
        label1.grid(row=0, sticky=S)
        label2=Label(root, text="2. "+questions[1])
        label2.grid(row=1, sticky=S)
        label3=Label(root, text="3. "+questions[2])
        label3.grid(row=2, sticky=S)
        label4=Label(root, text="4. "+questions[3])
        label4.grid(row=3, sticky=S)
        label5=Label(root, text="5. "+questions[4])
        label5.grid(row=4, sticky=S)
        label6=Label(root, text="6. "+questions[5])
        label6.grid(row=5, sticky=S)
        label7=Label(root, text="7. "+questions[6])
        label7.grid(row=6, sticky=S)
        label8=Label(root, text="8. "+questions[7])
        label8.grid(row=7, sticky=S)
        label9=Label(root, text="9. "+questions[8])
        label9.grid(row=8, sticky=S)
        label10=Label(root, text="10. "+questions[9])
        label10.grid(row=9, sticky=S)
        a=StringVar()
        a.set(self.Q1)
        om1=OptionMenu(root, a, "Yes", "No")
        om1.config(bg="navy", fg="orange")
        om1.grid(row=0, column=1)
        pickQ=StringVar()
        b=StringVar()
        b.set(self.Q2)
        om2=OptionMenu(root, b, "Yes", "No")
        om2.config(bg="navy", fg="orange")
        om2.grid(row=1, column=1)
        c=StringVar()
        c.set(self.Q3)
        om3=OptionMenu(root, c, "Yes", "No")
        om3.config(bg="navy", fg="orange")
        om3.grid(row=2, column=1)
        d=StringVar()
        d.set(self.Q4)
        om4=OptionMenu(root, d, "Yes", "No")
        om4.config(bg="navy", fg="orange")
        om4.grid(row=3, column=1)
        e=StringVar()
        e.set(self.Q5)
        om5=OptionMenu(root, e, "Yes", "No")
        om5.config(bg="navy", fg="orange")
        om5.grid(row=4, column=1)
        f=StringVar()
        f.set(self.Q6)
        om6=OptionMenu(root, f, "Yes", "No")
        om6.config(bg="navy", fg="orange")
        om6.grid(row=5, column=1)
        g=StringVar()
        g.set(self.Q7)
        om7=OptionMenu(root, g, "Yes", "No")
        om7.config(bg="navy", fg="orange")
        om7.grid(row=6, column=1)
        h=StringVar()
        h.set(self.Q8)
        om8=OptionMenu(root, h, "Yes", "No")
        om8.config(bg="navy", fg="orange")
        om8.grid(row=7, column=1)
        x=StringVar()
        x.set(self.Q9)
        om9=OptionMenu(root, x, "Yes", "No")
        om9.config(bg="navy", fg="orange")
        om9.grid(row=8, column=1)
        y=StringVar()
        y.set(self.Q10)
        om10=OptionMenu(root, y, "Yes", "No")
        om10.config(bg="navy", fg="orange")
        om10.grid(row=9, column=1)
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: findChange(self, questions, root, but,a,b,c,d,e,f,g,h,x,y,label1,label2,label3,label4,label5,label6,label7,label8,label9,label10)
        but.grid(row=11, sticky=S)
        for i in range(0, len(questions)):
            print(str((i+1))+". "+questions[i])
        change=input("Which question number would you like to change?\n")
         
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
         
        print(self.Q1)
        root=Toplevel()
        t=Text(root)
        t.insert(END, "1. "+questions[0]+'\n')
        t.insert(END, self.Q1+"\n")
        t.insert(END, "2. "+questions[1]+'\n')
        t.insert(END, self.Q2+"\n")
        t.insert(END, "3. "+questions[2]+'\n')
        t.insert(END, self.Q3+"\n")
        t.insert(END, "4. "+questions[3]+'\n')
        t.insert(END, self.Q4+"\n")
        t.insert(END, "5. "+questions[4]+'\n')
        t.insert(END, self.Q5+"\n")
        t.insert(END, "6. "+questions[5]+'\n')
        t.insert(END, self.Q6+"\n")
        t.insert(END, "7. "+questions[6]+'\n')
        t.insert(END, self.Q7+"\n")
        t.insert(END, "8. "+questions[7]+'\n')
        t.insert(END, self.Q8+"\n")
        t.insert(END, "9. "+questions[8]+'\n')
        t.insert(END, self.Q9+"\n")
        t.insert(END, "10. "+questions[9]+'\n')
        t.insert(END, self.Q10+"\n")
        t.pack()

    def showRecentViews(self, student):
        print(userIn.recent1)
        if userIn.recent1!=None:
            root=Toplevel()
            label1=Label(root, text="Here's who's viewed you since you last logged in!")
            label1.grid(row=0, sticky=S)
            if userIn.recent1 is not None:
                label2=Label(root, text=userIn.recent1)
                label2.grid(row=1, sticky=S)
            if userIn.recent2 is not None:
                label3=Label(root, text=userIn.recent2)
                label3.grid(row=2, sticky=S)
            if userIn.recent3 is not None:
                label4=Label(root, text=userIn.recent3)
                label4.grid(row=3, sticky=S)
            self.recent1=None
            self.recent2=None
            self.recent3=None
            writeV(student)
        #t.insert(END, "Here's who recently viewed your profile!")
        #t.insert(END, self.recent1)
        #t.insert(END, self.recent2)
        #t.insert(END, self.recent3)
        #t.grid(row=0, sticky=N)

    def blockUsers(self, student):        
        root=Toplevel()
        label1=Label(root, text="Enter the name of the user you want to block: ")
        label1.grid(row=0, sticky=S)
        e=Entry(root)
        e.grid(row=1, sticky=S)
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: actualBlock(student, root, e, but, label1)
        but.grid(row=2, sticky=S)
        def actualBlock(student, root, e, but, label1):
            blockUser=e.get()
            label1.grid_forget()
            e.grid_forget()
            but.destroy()
            for i in range(0, len(student)):
                if student[i].username==blockUser:
                    for j in range(0, len(userIn.blockedList)):
                        if blockUser == userIn.blockedList[j]:                    
                            label1=Label(root, text = "Already blocked")
                            label1.grid()
                            return
                    userIn.blockedList.append(blockUser)            
                    writeV(student)
            label1=Label(root, text="Blocked user")
            label1.grid()
            
    def unblockUsers(self, student):
        root=Toplevel()
        label1=Label(root, text="Enter the name of the user you want to unblock: ")
        label1.grid(row=0, sticky=S)
        e=Entry(root)
        e.grid(row=1, sticky=S)
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: actualUnblock(student, root, e, but, label1)
        but.grid(row=2, sticky=S)
        def actualUnblock(student, root, e, but, label1):
            unblockUser=e.get()
            label1.grid_forget()
            e.grid_forget()
            but.destroy()
            if unblockUser not in userIn.blockedList:
                label1=Label(root, text="User not in block list")
                label1.grid(row=0, sticky=S)
                return
            print(unblockUser)
            userIn.blockedList.remove(unblockUser)
            writeV(student)
            label1=Label(root, text="Unblocked")
            label1.grid(row=0, sticky=S)

    def getMatches(self, students): 
         
        root=Toplevel()
        matches=[]
        buttons=[]
        for i in range(0,len(students)):
            points=0            
            if self.username==students[i].username:
                continue
            if self.partnerGender!=students[i].gender:
                continue
            if self.gender != students[i].partnerGender:
                continue            
            if self.Q1==students[i].Q1:
                points+=1
            if self.Q2==students[i].Q2:
                points+=1
            if self.Q3==students[i].Q3:
                points+=1
            if self.Q4==students[i].Q4:
                points+=1
            if self.Q5==students[i].Q5:
                points+=1
            if self.Q6==students[i].Q6:
                points+=1
            if self.Q7==students[i].Q7:
                points+=1
            if self.Q8==students[i].Q8:
                points+=1
            if self.Q9==students[i].Q9:
                points+=1
            if self.Q10==students[i].Q10:
                points+=1
            for j in range(0, len(students[i].blockedList)):
                if students[i].blockedList[j] == userIn.username:
                     points = 0
            if points>=6:
                matches.append(students[i].username)
                buttons.append(student[i])
            if len(matches)>5:
                break
        #t=Text(root)
        #for i in matches:
        #    t.insert(END, i+'\n') #add button to click and view other profiles
        #t.pack()
        #if checklabel1==true:
        print(*matches)
        if len(matches)==0:
            Label(root, text="No matches :(").grid(row=0, sticky=S)
        label1=Label(root, text=str(matches[0])).grid(row=0, sticky=S)
        but1=Button(root, text="Check them out!", command=lambda: buttons[0].viewProfile(), bg="navy", fg="orange").grid(row=0, column=1, sticky=E)
        label2=Label(root, text=str(matches[1])).grid(row=1, sticky=S)
        but2=Button(root, text="Check them out!", command=lambda: buttons[1].viewProfile(), bg="navy", fg="orange").grid(row=1, column=1, sticky=E)
        #if checklabel3==true:
        label3=Label(root, text=str(matches[2])).grid(row=2, sticky=S)
        but3=Button(root, text="Check them out!", command=lambda: buttons[2].viewProfile(), bg="navy", fg="orange").grid(row=2, column=1, sticky=E)
        #if checklabel4==true:
        label4=Label(root, text=str(matches[3])).grid(row=3, sticky=S)
        but4=Button(root, text="Check them out!", command=lambda: buttons[3].viewProfile(), bg="navy", fg="orange").grid(row=3, column=1, sticky=E)
        #if checklabel5==true:
        label5=Label(root, text=str(matches[4])).grid(row=4, sticky=S)
        but5=Button(root, text="Check them out!", command=lambda: buttons[4].viewProfile(), bg="navy", fg="orange").grid(row=4, column=1, sticky=E)
        #if checklabel2==true:
        return

    def sendMessage(self, student, master):
        root=Toplevel()
        def getUsername(self, root, but, label1, e):
            global f
            userMsg=e.get()
            #t.pack_forget()
            label1.grid_forget()
            e.grid_forget()
            but.destroy()
            for i in range(0,len(student)):
                if userMsg==student[i].username:
                    for j in range(0, len(student[i].blockedList)):
                        if student[i].blockedList[j] == userIn.username:
                            print("User not found" + "\n" + "...")
                            return
                    userMsg=student[i]
                    #t=Text(root)
                    #t.insert(END, "Enter your message: ")
                    #t.pack()
                    label1=Label(root, text="Enter your message")
                    label1.grid(row=0, sticky=S)
                    f=Entry(root)
                    f.grid(row=1, sticky=S)
                    but=Button(root, text="Send", bg="navy", fg="orange")
                    but['command']=lambda: sendActualMessage(self, root, userMsg, but, f, label1)
                    but.grid(row=2, sticky=S)
                    return
            Label(root, text="User not found").grid(row=0, sticky=S)
            #t.insert(END, "User not found")
            return
        def sendActualMessage(self, mroot, userMsg, but, f, label1):
            but.destroy()
            label1.grid_forget()
            msg=f.get()
            f.grid_forget()
            #t.pack_forget()
            yagmail.SMTP("titanmatchteam@gmail.com").send(userMsg.email, "You've received a message from "+self.username, msg)
            #t=Text(master)
            #t.insert(END, "Message sent successfully\n")
            #t.pack()
            Label(root, text="Message sent successfully\n").grid(row=0, sticky=S)
            return
        #t=Text(root)
        #t.insert(END, "Enter the name of the user you would like to search for")
        #t.pack()
        label1=Label(root, text="Enter the name of the user you would like to search for: ")
        label1.grid(row=0, sticky=S)
        e=Entry(root)
        e.grid(row=1, sticky=S)
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: getUsername(self, root, but, label1, e)
        but.grid(row=2, sticky=S)
        return

    def deactivateProfile(self, student, master):
         
        master.withdraw()
        root=Toplevel()
        #t=Text(root)
        for i in range(0, len(student)):
            if(self.username==student[i].username):
                #del student[i]
                #t.insert(END, "Deactivation complete, click button to exit\n")
                #t.pack()
                Label(root, text="Deactivation complete, click button to exit.").grid(row=0, sticky=S)
                writeV(student) #update the change
                exitButton=Button(root, text="Exit program", command=lambda: exitLoop(master), bg="navy", fg="orange")
                exitButton.config(width=15)
                exitButton.grid(row=1, sticky=S)
                break
        master.deiconify
        return

    def editProfile(self): #change these from being pack
         
        editProf=Toplevel()
        def editUsername(self):
            #t=Text(root)
            #t.insert(END, "Enter your new username")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your new username: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeUNameChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makeUNameChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.username=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                return
        def editPassword(self):
            #t=Text(root)
            #t.insert(END, "Enter your new password")
            #t.pack()
            root=Toplevel()
            label1=Label(root, Text="Enter your new password: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makePWChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makePWChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.password=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newPW=input("Enter your new password: ")
            self.password=newPW
            root.destroy()
            print("Success!")
            return
        def editEmail(self):
            #t=Text(root)
            #t.insert(END, "Enter your new email: ")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your new email: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeEmailChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makeEmailChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                       label1=Label(root, text="Nothing entered")
                       label1.grid(row=0, sticky=S)
                       return
                self.email=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newEmail=input("Enter your new email: ")
            self.email=newEmail
            root.destroy()
            print("Success!")
            return
        def editMajor(self):
            #t=Text(root)
            #t.insert(END, "Enter your new major: ")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your new major: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeMajorChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makeMajorChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.major=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newMajor=input("Enter your new major: ")
            self.major=newMajor
            root.destroy()
            print("Success!")
            return
        def editGender(self):
            #t=Text(root)
            #t.insert(END, "Enter your new gender: ")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your new gender: ")
            label1.grid(row=0, sticky=S)
            e=StringVar()
            e.set(self.gender)
            om1=OptionMenu(root, e, "Male", "Female")
            om1.config(bg="navy", fg="orange")
            om1.grid(row=1, sticky=S)
            but=Button(root,  text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeGenderChange(self, root, e, but, label1, om1)
            but.grid(row=2, sticky=S)
            def makeGenderChange(self, root, e, but, label1, om1):
                om1.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.gender=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newGender=input("Enter your new gender: ")
            self.gender=newGender
            root.destroy()
            print("Success!")
            return
        def editBirthday(self):
            #t=Text(root)
            #t.insert(END, "Enter your new birthday: ")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your new birthday: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeBirthdayChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makeBirthdayChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.birthday=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newBirthday=input("Enter your new birthday: ")
            self.birthday=newBirthday
            root.destroy()
            print("Success!")
            return
        def editPrefGender(self):
            #t=Text(root)
            #t.insert(END, "Enter your preferred partner gender: ")
            #t.pack()
            root=Toplevel()
            label1=Label(root, text="Enter your preferred partner gender: ")
            label1.grid(row=0, sticky=S)
            e=StringVar()
            e.set(self.partnerGender)
            om1=OptionMenu(root, e, "Male", "Female")
            om1.config(bg="navy", fg="orange")
            om1.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makePrefGenderChange(self, root, e, but, label1,om1)
            but.grid(row=2, sticky=S)
            def makePrefGenderChange(self, root, e, but, label1, om1):
                om1.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.partnerGender=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                #t.delete("1.0", END)
                #t.insert(END, "Success!")
                return
            newPrefGender=input("Enter your preferred partner gender: ")
            self.partnerGender=newPrefGender
            root.destroy()
            print("Success!")
            return
        def editBio(self):
            root=Toplevel()
            label1=Label(root, text="Update your bio: ")
            label1.grid(row=0, sticky=S)
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Submit", bg="navy", fg="orange")
            but['command']=lambda: makeBioChange(self, root, e, but, label1)
            but.grid(row=2, sticky=S)
            def makeBioChange(self, root, e, but, label1):
                e.grid_forget()
                but.destroy()
                label1.grid_forget()
                if len(e.get())==0:
                    label1=Label(root, text="Nothing entered")
                    label1.grid(row=0, sticky=S)
                    return
                self.bio=e.get()
                label1=Label(root, text="Success!")
                label1.grid(row=0, sticky=S)
                return
        eUnameButton=Button(editProf, text="Edit username", command=lambda: editUsername(self), bg="navy", fg="orange")
        eUnameButton.config(width=15)
        eUnameButton.pack()
        ePWButton=Button(editProf, text="Edit password", command=lambda: editPassword(self), bg="navy", fg="orange")
        ePWButton.config(width=15)
        eUnameButton.pack()
        eEmailButton=Button(editProf, text="Edit email", command=lambda: editEmail(self), bg="navy", fg="orange")
        eEmailButton.config(width=15)
        eEmailButton.pack()
        eMajorButton=Button(editProf, text="Edit major", command=lambda: editMajor(self), bg="navy", fg="orange")
        eMajorButton.config(width=15)
        eMajorButton.pack()
        eGenderButton=Button(editProf, text="Edit gender", command=lambda: editGender(self), bg="navy", fg="orange")
        eGenderButton.config(width=15)
        eGenderButton.pack()
        eBirthdayButton=Button(editProf, text="Edit birthday", command=lambda: editBirthday(self), bg="navy", fg="orange")
        eBirthdayButton.config(width=15)
        eBirthdayButton.pack()
        ePrefGenderButton=Button(editProf, text="Edit pref gender", command=lambda: editPrefGender(self), bg="navy", fg="orange")
        ePrefGenderButton.config(width=15)
        ePrefGenderButton.pack()
        eBioButton=Button(editProf, text="Edit bio", command=lambda: editBio(self), bg="navy", fg="orange")
        eBioButton.config(width=15)
        eBioButton.pack()
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
            #print (loadVector[vectorIndex])
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
            #print ("the last thing before")
            #print (loadVector[vectorIndex])
            vectorIndex = vectorIndex + 1
            #if loadVector[vectorIndex] == 'qUiCK':
            #    print("won't get added to list! : )")           
            #print ("begin blockedList")          
            while (loadVector[vectorIndex] != 'qUiCK' and finished != True):
                if loadVector[vectorIndex] != "qUiCK":                  
                    blockedList.append(loadVector[vectorIndex])
                    vectorIndex += 1
                    #print (username)
                    #print (bio)                    
                    #print (blockedList)
                    if loadVector[vectorIndex] == 'qUiCK':
                        #print ("finished!")
                        #print ("index:")
                        #print (vectorIndex)
                        #print ("size:")
                        #print (vectorSize)
                        finished = True
            
            if loadVector[vectorIndex] == "qUiCK":    
                vectorIndex += 1        
                               
            p1 = person(gender, bio, password, birthYear, prefPartnerBirthYear, partnerGender, collegeYear, username, 
                        major, email,  Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, timestamp, recent1, recent2, recent3, blockedList)
            student.append(p1)
            #print ("index:")
            #print (vectorIndex)
            #print ("size:")
            #print (vectorSize)           

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
                  
def randomStr():
    letters=string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
        
def forgotPassword(student):
    global e
    root=Toplevel()
    #t=Text(root)
    #t.insert(END, "Enter your account name: ")
    #t.pack()
    label1=Label(root, text="Enter your account name: ")
    label1.grid(row=0, sticky=S)
    e=Entry(root)
    e.grid(row=0, column=1)
    #e.pack()
    #e.focus_set()
    but=Button(root, text="Submit", bg="navy", fg="orange")
    but['command']=lambda: forgottenPassword(student, root,e, but)
    but.grid(row=1, sticky=S)
    def forgottenPassword(student, root,e, but):
        forgot=e.get()
        e.grid_forget()
        but.destroy()
        for i in range(0, len(student)):
            if forgot==student[i].username:
                student[i].password=randomStr()
                writeV(student)
                forgot=student[i]
                yagmail.SMTP("titanmatchteam@gmail.com").send(forgot.email, "Forgotten password", "Hey there! Here is your password: " + forgot.password)
                label1=Label(root, text="An email has been sent with your password")
                label1.grid(row=0, sticky=S)
                return
        label1=Label(root, text="Account not found")
        label1.grid(row=1, sticky=S)
        return

def newUser(master, student, questions): #new user will enter in these choices and they will be passed to class
    def firstStep(root, master, student, questions, a,b,c,d,e,f,g,h,i,j,label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, gend, prefGend):
        sUserName=a.get()
        sPassword=b.get()
        sEmail=c.get()
        sBirthYear=d.get()
        sGender=gend.get()
        sMajor=f.get()
        sCollegeYear=g.get()
        sPartnerGender=prefGend.get()
        sPrefPartnerAge=i.get()
        sBio=j.get()
        a.grid_forget()
        b.grid_forget()
        c.grid_forget()
        d.grid_forget()
        e.grid_forget()
        f.grid_forget()
        g.grid_forget()
        h.grid_forget()
        i.grid_forget()
        j.grid_forget()
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.grid_forget()
        label5.grid_forget()
        label6.grid_forget()
        label7.grid_forget()
        label8.grid_forget()
        label9.grid_forget()
        label10.grid_forget()
        Label(root, text="1. "+questions[0]).grid(row=0, sticky=S)
        Label(root, text="2. "+questions[1]).grid(row=1, sticky=S)
        Label(root, text="3. "+questions[2]).grid(row=2, sticky=S)
        Label(root, text="4. "+questions[3]).grid(row=3, sticky=S)
        Label(root, text="5. "+questions[4]).grid(row=4, sticky=S)
        Label(root, text="6. "+questions[5]).grid(row=5, sticky=S)
        Label(root, text="7. "+questions[6]).grid(row=6, sticky=S)
        Label(root, text="8. "+questions[7]).grid(row=7, sticky=S)
        Label(root, text="9. "+questions[8]).grid(row=8, sticky=S)
        Label(root, text="10. "+questions[9]).grid(row=9, sticky=S)
        a=StringVar()
        a.set("Yes")
        om1=OptionMenu(root, a, "Yes", "No")
        om1.config(bg="navy", fg="orange")
        om1.grid(row=0, column=1)
        b=StringVar()
        b.set("Yes")
        om2=OptionMenu(root, b, "Yes", "No")
        om2.config(bg="navy", fg="orange")
        om2.grid(row=1, column=1)
        c=StringVar()
        c.set("Yes")
        om3=OptionMenu(root, c, "Yes", "No")
        om3.config(bg="navy", fg="orange")
        om3.grid(row=2, column=1)
        d=StringVar()
        d.set("Yes")
        om4=OptionMenu(root, d, "Yes", "No")
        om4.config(bg="navy", fg="orange")
        om4.grid(row=3, column=1)
        e=StringVar()
        e.set("Yes")
        om5=OptionMenu(root, e, "Yes", "No")
        om5.config(bg="navy", fg="orange")
        om5.grid(row=4, column=1)
        f=StringVar()
        f.set("Yes")
        om6=OptionMenu(root, f, "Yes", "No")
        om6.grid(row=5, column=1)
        om6.config(bg="navy", fg="orange")
        g=StringVar()
        g.set("Yes")
        om7=OptionMenu(root, g, "Yes", "No")
        om7.config(bg="navy", fg="orange")
        om7.grid(row=6, column=1)
        h=StringVar()
        h.set("Yes")
        om8=OptionMenu(root, h, "Yes", "No")
        om8.config(bg="navy", fg="orange")
        om8.grid(row=7, column=1)
        i=StringVar()
        i.set("Yes")
        om9=OptionMenu(root, i, "Yes", "No")
        om9.config(bg="navy", fg="orange")
        om9.grid(row=8, column=1)
        j=StringVar()
        j.set("Yes")
        om10=OptionMenu(root, j, "Yes", "No")
        om10.config(bg="navy", fg="orange")
        om10.grid(row=9, column=1)
        
        but=Button(root, text="Submit", command=lambda: secondStep(root, master, student, questions, sUserName, sPassword, sEmail,sBirthYear, sGender, sMajor, sCollegeYear, sPartnerGender, sPrefPartnerAge, sBio, a,b,c,d,e,f,g,h,i,j,answers), bg="navy", fg="orange").grid(row=10, sticky=S)
    def secondStep(root, master, student, questions, sUserName, sPassword, sEmail, sBirthYear, sGender, sMajor, sCollegeYear, sPartnerGender, sPrefPartnerAge, sBio, a,b,c,d,e,f,g,h,i,j,answers):
        timeStamp=time.time()
        global userIn
        answers[1]=a.get()
        print(answers[1][0])
        answers[2]=b.get()
        answers[3]=c.get()
        answers[4]=d.get()
        answers[5]=e.get()
        answers[6]=f.get()
        answers[7]=g.get()
        answers[8]=h.get()
        answers[9]=i.get()
        answers[10]=j.get()
        blockedList = []
        recent1 = "None"
        recent2 = "None"
        recent3 = "None"
        sNewUser=person(sGender, sBio, sPassword, sBirthYear, sPrefPartnerAge, sPartnerGender, sCollegeYear, sUserName, 
                        sMajor, sEmail, answers[1], answers[2], answers[3], answers[4], answers[5], answers[6], answers[7], 
                        answers[8], answers[9],answers[10], datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d'),
                        recent1, recent2, recent3, blockedList)
        student.append(sNewUser)
        
        userIn=student[len(student)-1]
        writeV(student)
        master.destroy()
        root.destroy()
        return
    global userIn
    answers=[0]*11
    root=Toplevel()
    gend=StringVar(root)
    gend.set("Male")
    prefGend=StringVar(root)
    prefGend.set("F")
    label1=Label(root, text="Enter username: ")
    label2=Label(root, text="Enter password: ")
    label3=Label(root, text="Enter your email: ")
    label4=Label(root, text="Enter your birthday: ")
    label5=Label(root, text="Enter your gender: ")
    label6=Label(root, text="Enter your major: ")
    label7=Label(root, text="Enter your college year: ")
    label8=Label(root, text="Enter your preferred gender: ")
    label9=Label(root, text="Would you like your partner to be older or younger than you?")
    label10=Label(root, text="Describe yourself: ")
    t=Text(root)
    #t.insert(END, "Enter username: \n")
    #t.insert(END, "Enter password: \n")
    #t.insert(END, "Enter your email: \n")
    #t.insert(END, "Enter your birthday: \n")
    #t.insert(END, "Enter your gender: \n")
    #t.insert(END, "Enter your major: \n")
    #t.insert(END, "Enter your college year: \n")
    #t.insert(END, "Enter your preferred gender: \n")
    #t.insert(END, "Would you like your partner to be older or younger than  you?\n")
    #t.insert(END, "Describe yourself: \n")
    #t.pack()
    a=Entry(root)
    b=Entry(root, show="*")
    c=Entry(root)
    d=Entry(root)
    e=OptionMenu(root, gend, "Male", "Female")
    e.config(bg="navy", fg="orange")
    f=Entry(root)
    g=Entry(root)
    h=OptionMenu(root, prefGend, "M", "F")
    h.config(bg="navy", fg="orange")
    i=Entry(root)
    j=Entry(root)
    label1.grid(row=0, sticky=S)
    label2.grid(row=1, sticky=S)
    label3.grid(row=2, sticky=S)
    label4.grid(row=3, sticky=S)
    label5.grid(row=4, sticky=S)
    label6.grid(row=5, sticky=S)
    label7.grid(row=6, sticky=S)
    label8.grid(row=7, sticky=S)
    label9.grid(row=8, sticky=S)
    label10.grid(row=9, sticky=S)
    #a.pack()
    a.grid(row=0, column=1)
    #b.pack()
    b.grid(row=1, column=1)
    #c.pack()
    c.grid(row=2, column=1)
    #d.pack()
    d.grid(row=3, column=1)
    #e.pack()
    e.grid(row=4, column=1)
    #f.pack()
    f.grid(row=5, column=1)
    #g.pack()
    g.grid(row=6, column=1)
    #h.pack()
    h.grid(row=7, column=1)
    #i.pack()
    i.grid(row=8, column=1)
    #j.pack()
    j.grid(row=9, column=1)
    but=Button(root, text="Submit", command=lambda: firstStep(root, master, student, questions, a,b,c,d,e,f,g,h,i,j,label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, gend, prefGend), bg="navy", fg="orange").grid(row=10, sticky=S)
    return

def searchUser(student, master): 
      
     root=Toplevel()
     #t=Text(root)
     #t.insert(END, "Enter the name of the user you wish to search for: ")
     #t.pack()
     label1=Label(root, text="Enter the name of the user you want to search for: ")
     label1.grid(row=0, sticky=S)
     e=Entry(root)
     e.grid(row=1, sticky=S)
     #e.focus_set()
     but=Button(root, text="Submit", bg="navy", fg="orange")
     but['command']=lambda: findUserName(student, root, e, but, label1)
     but.grid(row=2, sticky=S)
     def findUserName(student,root, e, but, label1):
        findUname=e.get()
        but.destroy()
        e.grid_forget()
        label1.grid_forget()
        #t.pack_forget()
        for i in range(0, len(student)):
            if student[i].username==findUname:
                for j in range(0, len(student[i].blockedList)):
                 if student[i].blockedList[j] == userIn.username:
                     label1=Label(root, text="User not found.")
                     label1.grid(row=0, sticky=S)
                     return
                root.destroy()
                student[i].viewProfile()
                print("Here: "+student[i].recent1)
                if student[i].username!=userIn.username:
                    if student[i].recent1==None:
                        student[i].recent1==userIn.username
                        writeV(student)
                        return
                    if student[i].recent2==None:
                        student[i].recent2=userIn.username
                        writeV(student)
                        return
                    if student[i].recent3==None:
                        student[i].recet3=userIn.username
                        writeV(student)
                        return
                    if student[i].recent1 != None and student[i].recent2 != None and student[i].recent3 != None:
                        student[i].recent1=student[i].recent2
                        student[i].recent2=student[i].recent3
                        student[i].recent3=userIn.username
                writeV(student)
                return
        Label(root, text="User not found").grid(row=0, sticky=S)    
        print("User not found")
        return
     return

def returningUser(master, student):
    global userIn
    root=Toplevel()
    label1=Label(root, text="Username")
    label2=Label(root, text="Password")
    #t=Text(master)
    #t.insert(END, "Username: \n")
    #t.insert(END, "Password: \n")
    #t.pack()
    findLogin=Entry(root)
    findPassword=Entry(root, show="*")
    label1.grid(row=0, sticky=S)
    label2.grid(row=1, sticky=S)
    findLogin.grid(row=0, column=1)
    findPassword.grid(row=1, column=1)
    but=Button(root, text="Submit", command=lambda: login(master, student, root), bg="navy", fg="orange").grid(row=2, sticky=S)
    def login(master, student, root):
       global userIn
       loginUser=findLogin.get()
       loginPass=findPassword.get()
       if not student: #checks if list is empty
           print("No users in database")
           return
       for i in range(0, len(student)):
           if loginUser==student[i].username:
            if loginPass==student[i].password:
                  userIn=student[i]
       root.destroy()
       master.destroy()
        
       return
    return
def contactUs(student):
    def FAQ():
        root=Toplevel()
        t=Text(root)
        t.insert(END, "How to create a good profile: \n")
        t.insert(END, " Answer the questions! They'll help you find people like you.\n")
        t.insert(END, " Fill in your biography, but keep it short.\n")
        t.insert(END, " Update everything as often as possible!\n")
        t.insert(END, " \n")
        t.insert(END, "Trying to write a good message?\n")
        t.insert(END, " Keep it short and sweet, around 40-60 characters.\n")
        t.insert(END, " Talk about something from their profile!\n")
        t.insert(END, " Check your grammar before sending it.\n")
        t.insert(END, " Really into someone but no response? One followup message is usually ok, but it wouldn't hurt to try out other matches.\n")
        t.insert(END, " \n")
        t.insert(END, "Account settings\n")
        t.insert(END, " To delete your account, press the deactivate profile button in the main menu.\n")
        t.insert(END, " To change your username, password, email, gender, or biography settings, click the edit profile button in the main menu.")
        t.insert(END, " \n")
        t.insert(END, "Using Titan Match\n")
        t.insert(END, " Report any offensive profiles through the report option under the 'Problem?' option in the main menu.\n")
        t.insert(END, " Send messages to any person you may feel a connection with using the 'Message a user' option in the main menu.\n")
        t.insert(END, " Trouble signing in? Try using the 'Forgot Password' option on the login menu.\n")
        t.insert(END, " Being troubled by a user persistently messaing you? Try blocking them and reporting them using the 'Block User' option.\n")
        t.pack()
        return
    def contactus(student):
        def sendEmail(student, e, label1, but):
            contactEmail=e.get()
            e.grid_forget()
            but.grid_forget()
            label1.grid_forget()
            yagmail.SMTP("titanmatchteam@gmail.com").send("titanmatchteam@gmail.com", "Message sent by "+userIn.username, contactEmail)
            label1=Label(root, text="Email sent")
            label1.grid(row=0, sticky=S)
            return
        root=Toplevel()
        label1=Label(root, text="Please enter your message: ")
        label1.grid(row=0, sticky=S)
        e=Entry(root)
        e.grid(row=1, sticky=S)
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: sendEmail(student, e, label1, but)
        but.grid(row=2, sticky=S)
        
    def reportUser(student):
        root=Toplevel()
        #t=Text(root)
        #t.insert(END, "What is the name of the user you would like to report?")
        #t.pack()
        label1=Label(root, text="What is the name of the user you would like to report?")
        label1.grid(row=0, sticky=S)
        e=Entry(root)
        e.grid(row=1, sticky=S)
        #e.focus_set()
        but=Button(root, text="Submit", bg="navy", fg="orange")
        but['command']=lambda: actualReport(root, student,e, label1, but)
        but.grid(row=2, sticky=S)
        def actualReport(root, student,e, label1, but):
            userReport=e.get()
            e.grid_forget()
            label1.grid_forget()
            but.destroy()
            label1=Label(root, text="Describe the problems that you've had: ")
            label1.grid(row=0, sticky=S)
            #t.delete('1.0', END)
            #t.insert(END, "Describe the problems that you've had: ")
            #t.pack()
            e=Entry(root)
            e.grid(row=1, sticky=S)
            but=Button(root, text="Send report", bg="navy", fg="orange")
            but['command']=lambda: sendReport(root, student, e, userReport, but, label1)
            but.grid(row=2, sticky=S)
            return
        def sendReport(root, student, e, choice, but, label1):
            report=e.get()
            e.grid_forget()
            but.destroy()
            label1.grid_forget()
            #t.delete('1.0', END)
            for i in range(0, len(student)):
                if choice==student[i].username:
                    yagmail.SMTP("titanmatchteam@gmail.com").send("titanmatchteam@gmail.com", "Report filed by "+userIn.username+" on "+student[i].username, report)
                    label1=Label(root, text="Report successfully submitted")
                    label1.grid(row=0, sticky=S)
         #          t.insert(END, "Report successfully submitted")
            Label(root, text="User not found").grid(row=0, sticky=S)
    root=Toplevel()
    reportButton=Button(root, text="Report user", command=lambda: reportUser(student), bg="navy", fg="orange")
    reportButton.config(width=15)
    reportButton.pack()
    faqButton=Button(root, text="F.A.Q.", command=lambda: FAQ(), bg="navy", fg="orange")
    faqButton.config(width=15)
    faqButton.pack()
    contactButton=Button(root, text="Contact Us", command=lambda: contactus(student), bg="navy", fg="orange")
    contactButton.config(width=15)
    contactButton.pack()
    return

def exitLoop(master):
    master.destroy()
    sys.exit()


master=Tk()
timeStamp=time.time()
master.title("TitanMatch")
#master.wm_iconbitmap("C:/Users/kylej/Downloads/tuffy_cTO_icon.ico")
popUp=Toplevel()
master.withdraw()
student=[] #list of student objects
#urllib.request.urlretrieve("https://docs.google.com/document/d/1SCZwIfFXLxFRp_W12WdP6plGV4Nwf9fu5u24areRJbk/export?format=txt", "output.txt")
load(student)
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
#userIn.changeTimestamp()
writeV(student)
returnUserButton.pack_forget()
newUserButton.pack_forget()
userIn.changeTimestamp()
userIn.showRecentViews(student)
#userIn.showRecentViews(student)
profButton=Button(master, text="View profile", command=lambda: userIn.viewProfile(), bg="navy", fg="orange")
profButton.config(width=15)
profButton.pack()
viewMatchButton=Button(master, text="View Matches", command=lambda: userIn.getMatches(student), bg="navy", fg="orange")
viewMatchButton.config(width=15)
viewMatchButton.pack()
sendMsgButton=Button(master, text="Message a user", command=lambda: userIn.sendMessage(student, master), bg="navy", fg="orange")
sendMsgButton.config(width=15)
sendMsgButton.pack()
b=Button(master, text="Edit questions", command=lambda: userIn.editQuestion(questions), bg="navy", fg="orange")
b.config(width=15)
b.pack()
searchButton=Button(master, text="Search for user", command=lambda: searchUser(student, master), bg="navy", fg="orange")
searchButton.config(width=15)
searchButton.pack()
viewAnswersButton=Button(master, text="View answers", command=lambda: userIn.viewAnswers(questions), bg="navy", fg="orange")
viewAnswersButton.config(width=15)
viewAnswersButton.pack()
editProfileButton=Button(master, text="Edit profile", command=lambda: userIn.editProfile(), bg="navy", fg="orange")
editProfileButton.config(width=15)
editProfileButton.pack()
blockButton=Button(master, text="Block user", command=lambda: userIn.blockUsers(student), bg="navy", fg="orange")
blockButton.config(width=15)
blockButton.pack()
unblockButton=Button(master, text="Unblock user", command=lambda: userIn.unblockUsers(student), bg="navy", fg="orange")
unblockButton.config(width=15)
unblockButton.pack()
contactUsButton=Button(master, text="Problem?", command=lambda: contactUs(student), bg="navy", fg="orange")
contactUsButton.config(width=15)
contactUsButton.pack()
deactivateProfileButton=Button(master, text="Deactivate profile", command=lambda: userIn.deactivateProfile(student, master), bg="navy", fg="orange")
deactivateProfileButton.config(width=15)
deactivateProfileButton.pack()
exitButton=Button(master, text="Exit", command=lambda: exitLoop(master), bg="navy", fg="orange")
exitButton.config(width=15)
exitButton.pack()
master.mainloop()