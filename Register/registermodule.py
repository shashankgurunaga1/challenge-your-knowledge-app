###################################################
# Function to create registration  window using tkinter 
###################################################
def register_form():
        label.destroy()
        label100.destroy()

        clearFrame()
        global root1
        root1 =frame
        # label to display the heading "registration form"
        label_reg_0 = Label(root1, text="Registration form",width=20,font=("bold", 40),bg='grey', fg="white")
        label_reg_0.place(x=90,y=53)
        # label to display the word username
        label_reg_1 = Label(root1, text="*Username",width=20,font=("bold", 20),bg='grey', fg="white")
        label_reg_1.place(x=70,y=130)
        # entry box to get the input for username as given by user during registration 
        global entry_reg_1
        entry_reg_1 = Entry(root1,width=20,bg='grey', fg="white")
        entry_reg_1.place(x=300,y=130)
        label_reg_2 = Label(root1, text="Email",width=20,font=("bold", 20),bg='grey', fg="white")
        label_reg_2.place(x=68,y=180)
        global entry_reg_2
        entry_reg_2 = Entry(root1,width=20,bg='grey', fg="white")
        entry_reg_2.place(x=300,y=180)
        label_reg_3 = Label(root1, text="Gender",width=20,font=("bold", 20),bg='grey', fg="white")
        label_reg_3.place(x=70,y=230)
        global var
        var = IntVar()
        r1= Radiobutton(root1, text="Male",padx = 5, variable=var, value=1)
        r1.place(x=300,y=230)
        r2=Radiobutton(root1, text="Female",padx = 20, variable=var, value=2)
        r2.place(x=370,y=230)
        label__reg_4 = Label(root1, text="Age:",width=20,font=("bold", 20),bg='grey', fg="white")
        label__reg_4.place(x=70,y=280)
        global entry_reg_4
        entry_reg_4 = Entry(root1,width=20,bg='grey', fg="white")
        entry_reg_4.place(x=300,y=280)

        label__reg_5= Label(root1, text="*Password:",width=20,font=("bold", 20),bg='grey', fg="white")
        label__reg_5.place(x=70,y=310)
        global entry_reg_5
        entry_reg_5 = Entry(root1,width=20,bg='grey', fg="white")
        entry_reg_5.place(x=300,y=310)

        btn1=Button(root1, text='Submit', width=20,bg='yellow', fg='red')
        btn1.place(x=180,y=380)
        btn1.bind('<Button-1>', onclick1_register)
def onclick1_register(event):
        flag = 0

        # If username  value is not given then show it as mandatory so that the user can put the value again 
        username =str(entry_reg_1.get())
        if (len(username) == 0):
              label_reg_11 = Label(root1, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=130)
              flag=1
        
        # If email  value is not given it will take as None
        email =str(entry_reg_2.get())
        if (len(email) == 0):
              email=None
      
        # If gender value is not given it will take as None
        gender=str(var.get ())
        if (len(gender) == 0):
              gender=None

        # If age value is not given it will take as None
        age=str(entry_reg_4.get())
        if (len(age) == 0):
              age=0
        else:
                  # check whether integer value is given for age , else throw error
                  try:
                        age=int(age)
                  except ValueError:
                        label_reg_11 = Label(root1, text="*Should be Integer",width=20,font=("bold", 20),bg='grey', fg="red")
                        label_reg_11.place(x=500,y=280)
                        flag=1

        # If password  value is not given then show it as mandatory so that the user can put the value again                 
        password =str(entry_reg_5.get())
        if (len(password)== 0):
              label_reg_11 = Label(root1, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=310)
              flag=1

        mycursor = mydb.cursor(prepared=True)
        
    
        # check if the username being inserted is already present

        sql_query="select count(*) from user_profile  where username=%s"
        mycursor.execute(sql_query,(str(username),))
        for row in mycursor:
            item_user =(
              row[0]
           )
        ## if same usename already present in the database table , it will say Username Exists 
        if ((item_user >0) and (flag==0)) :
            label_reg_11 = Label(root1, text="Username Exists ",width=20,font=("bold", 20),bg='grey', fg="red")
            label_reg_11.place(x=80,y=400)
        elif ((item_user==0) and (flag==0)) :
            sql ='insert into user_profile(username,email,gender, age,password) values(%s,%s,%s,%s,%s)'
            mycursor.execute(sql,(str(username),str(email),str(gender),str(age), str(password)))
            mydb.commit()
            sql1 = "insert into currency(username,coins) values(%s,500)"
            mycursor.execute(sql1,(str(username),))
            mydb.commit()
            label_reg_11 = Label(root1, text="Registration Successful ",width=20,font=("bold", 20),bg='grey', fg="red")
            label_reg_11.place(x=80,y=400)
            
