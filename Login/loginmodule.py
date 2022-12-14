####################################################
# Function to create login window using Tkinter 
###################################################
def login_form():
        # tkinter login form 
        label.destroy()
        label100.destroy()
  
        clearFrame()
        global root_login

        root_login =frame
        
        label_reg_login_0 = Label(root_login, text="Login Details",width=20,font=("bold", 40),bg='grey', fg="white")
        label_reg_login_0.place(x=90,y=53)
        label_reg_login_1 = Label(root_login, text="*Username",width=20,font=("bold", 20),bg='grey', fg="white")
        label_reg_login_1.place(x=70,y=130)
        global entry_reg_login_1
        entry_reg_login_1 = Entry(root_login,width=20,bg='grey', fg="white")
        entry_reg_login_1.place(x=300,y=130)

        label_login_reg_5= Label(root_login, text="*Password:",width=20,font=("bold", 20),bg='grey', fg="white")
        label_login_reg_5.place(x=70,y=310)
        global entry_login_reg_5
        entry_login_reg_5 = Entry(root_login,width=20,bg='grey', fg="white")
        entry_login_reg_5.place(x=300,y=310)

        btn1=Button(root_login, text='Submit', width=20,bg='yellow', fg='red')
        btn1.place(x=180,y=380)
        btn1.bind('<Button-1>', onclick1_login)
######################################################
#Function to validate login  details 
#########################################################

def onclick1_login(event):
        
        
        global username
        # check if username filed is left blank , then  display the word "*mandatory" nect to username entry box in tkinter window
        username =str(entry_reg_login_1.get())
        if (len(username) == 0):
              label_reg_log11= Label(root_login, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_log11.place(x=500,y=130)

        # check if password filed is left blank , then  display the word "*mandatory" nect to username entry box in tkinter window
        password =str(entry_login_reg_5.get())
        if (len(password)== 0):
              label_reg_log12 = Label(root_login, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_log12.place(x=500,y=310)

        mycursor = mydb.cursor(prepared=True)
        
    
        # check if the username is present in the user_profile table for validation 

        sql_query="select count(*) from user_profile  where username=%s"
        mycursor.execute(sql_query,(str(username),))
        for row in mycursor:
            item =(
              row[0]
           )
        # if username name is present in the sql table , retrieve th password from db table 
        if (item >0):
            sql_query="select password from user_profile  where username=%s"
            mycursor.execute(sql_query,(str(username),))
            for row in mycursor:
                  password1 =(
                  row[0]
              )
            # match the database password with user given password 
            if (password == password1):
                menu_load(username)
                # is password matched , bring up the play game window
                play_game_functon()
            
            # if password does not match with database entry , then promot Password does not match
            else:
                label_reg_log13 = Label(root_login, text="Password does not match  ",font=("bold", 20),bg='grey', fg="red")
                label_reg_log13.place(x=80,y=410)

        # if username does not match with database, then prompt username does not exist  
        elif (item==0):
            label_reg_log13 = Label(root_login, text="Username does not exist ",font=("bold", 20),bg='grey', fg="red")
            label_reg_log13.place(x=80,y=410)
