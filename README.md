Project
Challenge your knowledge in Python

Objective

This is an application built in Python to play quiz and get coins based on the number of correct questions answered.
This application is useful to encourage students to check their knowledge in python and to create interest among students. It also allows students to purchase products based on his/her accumulated coins.
This is an authentication (login/registration) based application and also facilitated with an admin module to insert new quiz questions in the database table. 


Problem Definition 
(This application has been developed using Tkinter as Graphical User Interface, Mysql as database and MySQL connector to connect to database. Below is the high-level flow of the application.)

This Application is developed in below 7 modules.

a)	Launch the application
o	Launch the application by running the python program 
o	Error handling/Validation: 
i.	First time, when you launch the project, you will be only given login/register menu.
ii.	All other menus will be hidden and they only will appear based on successful login authentication.

b)	Role based Menu display 
o	If the user is standard user, on successful login, he /she will get two menus to choose from – Play the Quiz and also Purchase based on the coins he has in his account

o	If the user is admin –he additionally gets another menu to insert new quiz questions in the database

o	Upon successful login, the username is tracked in the entire session and login/registration menu gets disabled to avoid accidental re-login which could lose his session.

c)	Registration Module
o	This module asks first time user to enter important information like username, email, gender, password, age. 

o	On successful validation of the above entries, the application stores the user information in the database

o	Also, upon registration, 500 points are awarded to the first-time user. 

o	Error handling/Validation: 
i.	Username cannot be blank – shows *mandatory on screen next to username entry box. 
ii.	Password cannot be blank - shows *mandatory on screen next to password entry box. 
iii.	If user enters non integer value in age field, it will prompt that only integer is allowed
iv.	Check for same username existence in Database table – checks against user_profile table 
•	If username already exists, gives message, to user notifying the username already exists 

d)	Login Module
o	Once registered, user can login in the app using the username and password chosen by him/her.
o	On clicking the login option menu in application, user will be asked to provide username and password to login in the app 
o	On successful login (userid and password are validated against database user profile table) , the app will take the user to the quiz wizard.
o	Error handling/validation: 
I.	Username cannot be blank – shows *mandatory on screen next to username entry box 
II.	Password cannot be blank – shows *mandatory on screen next to password entry box 
III.	Check for Username’s presence in the database, else gives message “Username does not exist” 
IV.	Check for Password’s presence in the database else gives message “Password does not match “

e)	Play Module 
o	On successful login (userid and password are validated against database user profile table), the app will take the user to the quiz wizard.
o	In Quiz wizard, user will be given  max 5 MCQs in a single UI screen with 3 options for each question.
o	If the questions are already attempted by User, then they will not be coming again 
o	At the end of submission, it will show the number of correct questions and also will award 10 coins for each correct question.
o	It will also show the total coins in user account.

f)	Reward Module
o	In the reward / purchase module, user can buy the product available using his coins 
o	The available product will be displayed at the top along with the number of coins required to purchase them 
o	On purchase, coins will be deducted, and new total coins will be shown in the UI window
o	If the user enters an invalid product id, it will give an error message saying product id does not exist 

g)	Admin – Insert new Quiz Question Module 
o	If the logged-in user is admin, he will be getting an additional admin module to add new quiz questions





Block Diagram
*function names are mentioned in ()




<img width="538" alt="image" src="https://user-images.githubusercontent.com/98585901/203067383-507925bd-a1cb-4505-8e06-e66ca94335a3.png">




                                                                         






															




                                                                                                                              
                                                                                                                                   
                                                                                                                                            
														




							












Database Schema 
Below is the list of the tables used in this application.

a)	Table name: user_profile 
Description: Stores the user information.
Table information: 
Field	Type	Comments
username	Varchar(100)	This column is primary and not null
email	Varchar(255)	Email id  for the user
gender	Varchar(6)	Gender of the user
age	int	Age of the user
password	Varchar(100)	Password of the user 


b)	Table name: catalogue 
Description: Store the product details that are available for purchase using reward points
Table information: 
Field	Type	Comments              
Product_id	int	Product_id  is the primary and not null
Product_desc	Varchar(255)	Stores product description
Coins_required	int	Coins required to purchase each product

c)	Table name: currency 
Description: Store the currency for user 
Table information: 
Field	Type	Extra
username	Varchar(100)	Foreign key of username from user_profile table  .
This field is primary and not null for this table 
coins	int	Coins that user has 

d)	Table name: questions1 
Description: Stores the MCQ questions with 3 options and correct answer 
Table information: 
Field	Type	Extra
Q_no	int	Question_no is primary and not null 
Q_level	int	Question level can be 1 ,2 ,3 based on difficulty
Question_desc	Varchar(1000)	Question description 
Opt_a	Varchar(500)	 First option for answer in MCQ
Opt_b	Varchar(500)	 First option for answer in MCQ
Opt_c	Varchar(500)	 First option for answer in MCQ
ans	Varchar(500)	Contain the correct answer

a)	Table name: questions_attempted
Description: Stores the questions attempted by user so that next time they are not repeated 
Table information: 
Field	Type	Extra
Username 	int	Primary key , not null and also Foreign key of username from user_profile table  

Q_level	int	Question level can be 1 ,2 ,3 based on difficulty
Attempt_no	int	Capture the user attempt number  
Q1	int	Stores the first question id out of the 5 questions attempted by user
Q2	int	 Stores the second question id out of the 5 questions attempted by user
Q3	int	Stores the third question id out of the 5 questions attempted by user
Q4	int	Stores the fourth question id out of the 5 questions attempted by user
Q5	int	Stores the fifth question id out of the 5 questions attempted by user




Module Wise Analysis 
A. Launch the application 

     Input: Nothing specific (just run the python program) 
     Output: Application launched with registration and login menu
     List of datafiles/database: None 
     Code: 
#######################################
# Menu load based on username #######
#######################################



def menu_load(username):

          # if first time the application is loaded , it will only show login and register menu 
	  
          # the check is made by checking username is None
	  
        if( username is None):
                global file3 
                file3 = Menu(menubar, tearoff = 0) 
                menubar.add_cascade(label ='Login/Register', menu = file3) 
                file3.add_command(label ='Register', command = register_form) 
                file3.add_command(label ='Login', command = login_form) 
                file3.add_separator() 
                file3.add_command(label ='Exit', command = main_root.quit) 
        # once the user is logged in , username will be not None 
        # here username is a global variable , used in different functions 
        elif ( username is not None) : 
                # delete the login submenu so the user cant try relogin or reregister once logged in 
                file3.delete(0,END)

                # Display Play game menu  
                file = Menu(menubar, tearoff = 0) 
                menubar.add_cascade(label ='Play Game', menu = file) 
                file.add_command(label ='Start', command = play_game_functon) 
                file.add_separator() 
                file.add_command(label ='Exit', command = main_root.quit) 

                # Display Reward menu 
                file1 = Menu(menubar, tearoff = 0) 
                menubar.add_cascade(label ='Reward', menu = file1) 
                file1.add_command(label ='Purchase Product', command=purchase_module)
                file1.add_separator() 

       # if user is admim , display admin module also
        if (username =='admin'):
                file2 = Menu(menubar, tearoff = 0) 
                menubar.add_cascade(label ='Admin Module', menu = file2) 
                file2.add_command(label ='Add Record', command = insert_question_form) 
                file2.add_separator() 

################################
#Main UI in tkinter#
####################################

global username
username = None 

# create root window
main_root = Tk()
main_root.title("Challenge Your Knowledge")
main_root.geometry("1200x800")

# create frame
global frame
frame=Frame(main_root,bg='grey')
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

main_root.configure(bg='grey')

# menubar
menubar = Menu(main_root)

main_root.config(menu = menubar) 
global label,label100
label = Label(main_root, text="Welcome to Challenge Your Knowledge App", font=('Times New Roman',  '60'), fg="black", bg="grey")
label.place(relx = 0.5,  rely = 0.5, anchor = 's') 
label100 = Label(main_root, text='New user select register from Menu else Select login', font=('Times New Roman',  '20'), fg="black", bg="grey")
label100.place(relx = 0.5,  rely = 0.5, anchor = 'n') 
# load menu
menu_load(username)
       
 
## Destroy the window at the end 
main_root.mainloop()

Sample output:  
![image](https://user-images.githubusercontent.com/98585901/203063453-99334443-2175-40f6-bfc9-c467fa09c4af.png)

 


B .  Registration Module

Input: Username, email, age, gender, password
Output: 
•	All inputs are validated  and authenticated. 
•	On successful validation,  username and other info is stored in user_profile table in database
•	Give 500 coins to the new user in the currency table
List of database tables used in this module: 
•	user_profile 
•	currency 
Code: 

Function to create the registration window in tkinter
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




Function to validate registration information 


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
            
          



Sample output: 

Case 1: 
•	All the entries are validated successfully 
•	User gets the message: Registration successful 


 ![image](https://user-images.githubusercontent.com/98585901/203063596-8ae6d87d-6b1c-4490-b469-5d9fd5820463.png)




 Case 2:
•	If username or password field is empty: 
•	The word Mandatory is displayed in the screen next to username/password in red on the screen 

 ![image](https://user-images.githubusercontent.com/98585901/203063676-5c2f7863-4dd2-4f40-baf2-f8d65c8687d5.png)



 Case 3: 
•	If a non-integer value is entered in age field
•	A message is prompt in red next to age field saying it would be integer 
![image](https://user-images.githubusercontent.com/98585901/203063728-0f567ecc-1363-4c1f-9291-a67343bae37a.png)

 

Case 4:
•	If username already exists in database
•	A message is prompt in red saying Username Exists 

 
![image](https://user-images.githubusercontent.com/98585901/203063797-b1010f9c-155b-4401-a367-ae9f5615cb3f.png)


C .  Login Module 
Input: Username, password
Output: 
o	All inputs are valid and authenticated. 
o	User is taken to the quiz wizard
o	At the top of the application, user will see menus like Play Games, Rewards for a standard user 
o	For admin user, he will see an addition menu named Admin Module 
o	Upon successful login register/login menu will be disabled to prevent accidental re-login
List of database tables used in this module: 
•	user_profile 
•	question1
Code: 
Function to create login form 
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

Function to validate login information 
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

Sample Output: 


Case 1: Valid username and password entered          
              User will be taken to quiz wizard on successful authentication 
 

 ![image](https://user-images.githubusercontent.com/98585901/203063975-fe391609-a09c-4303-9320-8fc6905a6735.png)
![image](https://user-images.githubusercontent.com/98585901/203064045-a5986a1b-4950-48d5-ae2e-97c7e93ee3bd.png)



 

Case 2 : When username and password are blank, user will be prompted with field mandatory notification 
 ![image](https://user-images.githubusercontent.com/98585901/203064091-9bcc24d4-f67f-4933-b252-f5d2e94d9c79.png)


Case 2: When username does not exist in the database
               User will be prompted with Username does not exist message
 
![image](https://user-images.githubusercontent.com/98585901/203064141-bbc37eb7-62d9-4d8a-864a-06eb8f55bcb8.png)

Case 3: When username is valid but password does not match 
               User will be prompted with Password does not match message

 ![image](https://user-images.githubusercontent.com/98585901/203064179-ae8df918-60a3-4268-b4e0-907609b9b5eb.png)

               

D .  Play Module

Input: None
Output: 
•	User will be given 5 MCQs with 3 options for each question at a time.
•	If the questions are already attempted by user, then they will not be coming again. 
•	If user miss answering any question, the user message saying mandatory will be prompted next to the question.
•	At the end of submission, it will show the number of correct questions and also will award 10 coins for each correct question.
•	It will also show the updated total coins in user account.
•	When no more un-attempted questions are left, it will show the message No quiz questions left to take 

List of database tables in this module:
•	currency 
•	questions1
•	questions attempted 

Code: 
######################################################################
# Function for Play game 
########################################################################

def play_game_functon():
        # passing the question_level 
        query_qids_not_attempted_by_user(1)

#########################################################################
#  Function to get question ids  not attempted by user previously
##########################################################################
def query_qids_not_attempted_by_user(q_level):

            # clear the frame and destroy the first screen labels
            label.destroy()
            label100.destroy()

            clearFrame()
            global root1_play
            root1_play =frame

            # check for question nos that are not attempted . This query will give all the questions id that are still not attempted by user
            items_qids=[]
            global str_qno
            str_qno =""
            mycursor = mydb.cursor(prepared=True)
         
            sql_query_q= "select * from questions1 where q_level =%s and qno_no not in (select q1 from questions_attempted where username=%s union select q2 from questions_attempted where username=%s union select q3 from questions_attempted where username=%s union select q4 from questions_attempted where username=%s union select q5 from questions_attempted where username=%s)"
            mycursor.execute(sql_query_q,(str(q_level),str(username),str(username),str(username),str(username),str(username)))
            count=0
            for row in mycursor:
                  item =(
                        row[0]
                        )      
            
                  # add the question nos retrieved from table that are unattmpted in variable str_qno 
                  str_qno = str_qno + str(item) + ","

            # if no questions are left to try , display the same message
            if (str_qno ==""):
                  label_reg_0 = Label(root1_play, text="No quiz questions left to take" ,font=("bold", 30),bg='grey', fg="pink")
                  label_reg_0.place(x=90,y=100)
            
            else:
                  str_qno = str_qno[:-1]
                  ### the below function will get the questions details based on question nos not attempted by user so far
            
                  play_game_get_questions_not_attempted(q_level,str_qno)

###############################################################################################
#### Function to get questions details based on the question nos passed from the function query_qids_not_attempted_by_user
#str_no contains the questions nos 
####################################################################################################
def   play_game_get_questions_not_attempted(q_level,str_qno):
            
            global que1 
            global que2
            global que3
            global que4
            global que5
            global que1_qno
            global que2_qno
            global que3_qno
            global que4_qno
            global que5_qno

            que1 = StringVar()
            que2 = StringVar()
            que3 = StringVar()
            que4 = StringVar()
            que5 = StringVar()
            
            # get the questions from questions table based on the questions number passed
            mycursor = mydb.cursor()
            
            sql_query_q1= "select qno_no, qno_desc,opt_a,opt_b,opt_c from questions1 where q_level =%s and qno_no in " + "(" + str_qno +")"

            mycursor.execute(sql_query_q1,(str(q_level),))

            label_reg_0 = Label(root1_play, text="Play Python Knowledge Challenge",font=("bold", 30),bg='grey', fg="pink")
            label_reg_0.place(x=90,y=10)

            # x_row and y_col is to position the components in tkinter
            x_row =90
            y_col =53

            # counter to keep count of the questions 
            i=0
        
            for row in mycursor:
                  
                  # display 5 questions using tkinter label. each row will contain details about single question like q_no, q_desc, options and answer 
                  #row[1] – is question decrption
                  
                  var1 ="Question " + str(i+1) +": "+ str(row[1]) 
                  x_row =50
                  
                  # radio buttons for the first question answers 
                  if (i==0):
                        label_reg_0 = Label(root1_play, text=var1,bg='grey', fg="yellow")
                        label_reg_0.place(x=10,y=y_col)
                        y_col =y_col+25
                        que1_qno=row[0]
                        r1= Radiobutton(root1_play, text=row[2],padx = 50, variable=que1, value=row[2])
                        r1.place(x=x_row,y=y_col)
                        r2=Radiobutton(root1_play, text=row[3],padx = 50, variable=que1, value=row[3])
                        r2.place(x=x_row+150,y=y_col)
                        r3=Radiobutton(root1_play, text=row[4],padx = 50, variable=que1, value=row[4])
                        r3.place(x=x_row+300,y=y_col)
                        y_col =y_col+25

                  # radio buttons for the second question answers      
                  elif(i==1):
                        label_reg_0 = Label(root1_play, text=var1,bg='grey', fg="yellow")
                        label_reg_0.place(x=10,y=y_col)
                        y_col =y_col+25
                        que2_qno=row[0]
                        #que2 = StringVar()
                        r1= Radiobutton(root1_play, text=row[2],padx = 50, variable=que2, value=row[2])
                        r1.place(x=x_row,y=y_col)
                        r2=Radiobutton(root1_play, text=row[3],padx = 50, variable=que2, value=row[3])
                        r2.place(x=x_row+150,y=y_col)
                        r3=Radiobutton(root1_play, text=row[4],padx = 50, variable=que2, value=row[4])
                        r3.place(x=x_row+300,y=y_col)
                        y_col =y_col+25

                  # radio buttons for the third question answers  
                  elif(i==2):
                        label_reg_0 = Label(root1_play, text=var1,bg='grey', fg="yellow")
                        label_reg_0.place(x=10,y=y_col)
                        y_col =y_col+25
                        que3_qno=row[0]
                        #que3 = StringVar()
                        r1= Radiobutton(root1_play, text=row[2],padx = 50, variable=que3, value=row[2])
                        r1.place(x=x_row,y=y_col)
                        r2=Radiobutton(root1_play, text=row[3],padx = 50, variable=que3, value=row[3])
                        r2.place(x=x_row+150,y=y_col)
                        r3=Radiobutton(root1_play, text=row[4],padx = 50, variable=que3, value=row[4])
                        r3.place(x=x_row+300,y=y_col)
                        y_col =y_col+25

                  # radio buttons for the 4th question answers  
                  elif(i==3):
                        label_reg_0 = Label(root1_play, text=var1,bg='grey', fg="yellow")
                        label_reg_0.place(x=10,y=y_col)
                        y_col =y_col+25
                        que4_qno=row[0]
                        #que4 = StringVar()
                        r1= Radiobutton(root1_play, text=row[2],padx = 50, variable=que4, value=row[2])
                        r1.place(x=x_row,y=y_col)
                        r2=Radiobutton(root1_play, text=row[3],padx = 50, variable=que4, value=row[3])
                        r2.place(x=x_row+150,y=y_col)
                        r3=Radiobutton(root1_play, text=row[4],padx = 50, variable=que4, value=row[4])
                        r3.place(x=x_row+300,y=y_col)
                        y_col =y_col+25
                  
                  # radio buttons for the fifth question answers  
                  elif(i==4):
                        label_reg_0 = Label(root1_play, text=var1,bg='grey', fg="yellow")
                        label_reg_0.place(x=10,y=y_col)
                        y_col =y_col+25
                        que5_qno=row[0]
                        #que5 = StringVar()
                        r1= Radiobutton(root1_play, text=row[2],padx = 50, variable=que5, value=row[2])
                        r1.place(x=x_row,y=y_col)
                        r2=Radiobutton(root1_play, text=row[3],padx = 50, variable=que5, value=row[3])
                        r2.place(x=x_row+150,y=y_col)
                        r3=Radiobutton(root1_play, text=row[4],padx = 50, variable=que5, value=row[4])
                        r3.place(x=x_row+300,y=y_col)
                        y_col =y_col+25

                  
                  i=i+1
                  
            
            btn1=Button(root1_play, text='Submit', width=20,bg='yellow', fg='red')
            btn1.place(x=180,y=350)
            btn1.bind('<Button-1>', onclick1_play)


######### As the user hits the submit buttion in play game page 
######## The following function will be called . 

def  onclick1_play(event):
      flag =0
      global response1,response2,response3,response4,response5

      global correct_qno
      correct_qno =""
      
      # check if user has answered all questions 

      # if one  or question is deplayed in the screen and first question is not answered 
      if ((len(que1.get()) != 0) and (no_of_q >=1)):      
            response1=str(que1.get())
      elif (len(que1.get()) == 0):  
            label_reg_111 = Label(root1_play, text="*All questions are Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
            label_reg_111.place(x=30,y=400)
            flag=1

      # if  two  or question is deplayed in the screen and second question is not answered 
      if ((len(que2.get()) != 0)and (no_of_q >=2)): 
            response2=str(que2.get())
      elif ((len(que2.get()) == 0) and (no_of_q >=2)):  
            label_reg_111 = Label(root1_play, text="*All questions are Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
            label_reg_111.place(x=30,y=400)
            flag=1

      # if three  or question is deplayed in the screen and third question is not answered 
      if ((len(que3.get()) != 0) and (no_of_q >=3)): 
            response3=str(que3.get())
      elif ((len(que3.get()) == 0) and (no_of_q >=3)):  
            label_reg_111 = Label(root1_play, text="*All questions are Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
            label_reg_111.place(x=30,y=400)
            flag=1

      # if four  or question is deplayed in the screen and fourth question is not answered 
      if ((len(que4.get()) != 0)  and (no_of_q >=4)): 
            response4=str(que4.get())
      elif ((len(que4.get()) == 0) and (no_of_q >=4)):
              label_reg_111 = Label(root1_play, text="*All questions are Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_111.place(x=30,y=400)
              flag=1

      # if five  or question is deplayed in the screen and fifth question is not answered         
      if ((len(que5.get()) != 0) and (no_of_q >=5)): 
            response5=str(que5.get())
      elif ((len(que5.get()) == 0) and (no_of_q >=5)):
              label_reg_111 = Label(root1_play, text="*All questions are Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_111.place(x=30,y=400)
              flag=1
      
      

      global correct 
      correct =0

      # if user has answered all questions 

      if (flag==0):
            if (len(que1.get()) != 0): 
                  #validate the first question response with the answer wtored in  database 
                  correct = verify_question(correct_qno, correct,que1_qno,que1.get()) 
                  str_qno1 =str(que1_qno) +","+ str(0)+","+ str(0)+","+ str(0)+","+ str(0)

            if (len(que2.get()) != 0): 
                  #validate the second question response with the answer wtored in  database 
                  correct=verify_question(correct_qno,correct,que2_qno,que2.get())
                  str_qno1 =str(que1_qno) + ","+ str(que2_qno) +","+ str(0)+","+ str(0)+","+ str(0)

            if (len(que3.get()) != 0):
                  #validate the third question response with the answer wtored in  database 
                  correct= verify_question(correct_qno,correct,que3_qno,que3.get())
                  str_qno1 =str(que1_qno) + ","+ str(que2_qno) + ","+ str(que3_qno)+","+ str(0)+","+ str(0)

            if (len(que4.get()) != 0): 
                  #validate the fourth  question response with the answer wtored in  database 
                  correct= verify_question(correct_qno,correct,que4_qno,que4.get())
                  str_qno1 =str(que1_qno) + ","+ str(que2_qno) + ","+ str(que3_qno)+","+ str(que4_qno)+","+ str(0)
            if (len(que5.get()) != 0): 
                  #validate the fifth question response with the answer wtored in  database  
                  correct= verify_question(correct_qno,correct,que5_qno,que5.get())
                  str_qno1 =str(que1_qno) + ","+ str(que2_qno) + ","+ str(que3_qno)+","+ str(que4_qno)+","+ str(que5_qno)

            ######## Display total correct anwser 
            no_of_q_temp=0
            if (no_of_q >5):
                no_of_q_temp=5
            elif (no_of_q <=5):
                no_of_q_temp=no_of_q
                
            text34 = "Answered "+ str(correct) +" out of " +  str(no_of_q_temp) + " questions properly." 

            label_reg_11 = Label(root1_play, text=text34, font=("bold", 20),bg='grey', fg="yellow")
            label_reg_11.place(x=50,y=375)

            # give 10 points for each corrected question 
            points_earned = 10*correct
 
            #get current points of the user and add the points earned 
            current_currency_ofuser= user_currency_coin_details(username)

            # add points earned 
            new_point=points_earned + current_currency_ofuser

            # disdplay the earned point to the user 
            text35 = "You have earned " + str(points_earned)+ " new Points !"
            label_reg_12 = Label(root1_play, text=text35, font=("bold", 20),bg='grey', fg="yellow")
            label_reg_12.place(x=50,y=405)

            # update new currency 
            update_currency_or_coin_post_purchase(username,new_point)

            #Display total points
            text36 = "Your total points now " + str(new_point)
            label_reg_12 = Label(root1_play, text=text36, font=("bold", 20),bg='grey', fg="yellow")
            label_reg_12.place(x=50,y=435)

            #update attempt table
            update_attempted_table(username, str_qno1)



############################################
# Validate user answers with database and mark it correct if they match 

###############################################      
def verify_question(correct_qno,correct,que_qno,option):
      
      mycursor = mydb.cursor(prepared=True)
      sql_query_q11= "select ans from questions1 where qno_no =%s"
      mycursor.execute(sql_query_q11,(str(que_qno),))
      for row in mycursor:
            if (row[0] == option):
                  correct = correct +1
                  correct_qno =str(correct_qno)  + str (que_qno) + " ,"
      return correct


################################
## Update question attempted table when the user submits the questions so that next time when the user is playing same question is not repeated #########
################################
def update_attempted_table(username, str_qno):

      #  get attempt no for the user from db table 
      mycursor = mydb.cursor(prepared=True)
      sql_query1 ="SELECT max(attempt_no) + 1 FROM questions_attempted where username =%s"  
      mycursor.execute(sql_query1,(str(username),))
      for row in mycursor:
                attempt_no =(
                  row[0]
                  ) 
      
      if (attempt_no is None):
              attempt_no=1;

      ## Add the attempt no and attempted question numbers to the questions attempted table 
      sql_query_q11= "insert into questions_attempted(username,attempt_no,q1,q2,q3,q4,q5) values(" +"'" + username +"'," +str(attempt_no) +","+str(str_qno) +")"
      mycursor.execute(sql_query_q11)
      mydb.commit()





########################################################
# Update the user currency based on activity  
########################################################

def update_currency_or_coin_post_purchase(username,money):
          mycursor = mydb.cursor(prepared=True)
          update_query="update currency set coins=%s where username=%s"
          mycursor.execute(update_query,(money,str(username)))
          mydb.commit()




Sample output: 

 ![image](https://user-images.githubusercontent.com/98585901/203064349-1bccacd1-75b3-418d-9484-8d1619a816ef.png)


When no more un-attempted questions left 
 ![image](https://user-images.githubusercontent.com/98585901/203064404-31df1831-828a-4568-9630-6d4e3a833589.png)



E .  Reward Module 
Input: None
Output: 
•	In the reward / purchase module, user can buy the product available using his coins 
•	The available product will be displayed at the top along with the number of coins required to purchase them 
•	On purchase, coins will be deducted and new total coins will be shown in the UI window
•	If the user enters an invalid product id, it will give an error message saying product id does not exist 
List of database tables:
•	catalog
•	currency 
Code:
####################################################################
#function to design the purchase window 
######################################################################
def purchase_module():
       
        label.destroy()
        label100.destroy()
        clearFrame()
        global root
        root =frame
        
      
        root.columnconfigure(0,weight =1)
        root.columnconfigure(1,weight =2)
        
     
        label_01 =Label(root,text="Hi "+ username, width=20,font=("bold",20),bg='grey', fg="white")
      
        label_01.grid(row =0 , column = 0, sticky = W, pady = 2,columnspan=3) 

        label_0 =Label(root,text="Welcome to Purchase Central! ", width=20,font=("bold",20),bg='grey', fg="white")
        label_0.grid(row = 1, column = 0, sticky = W, pady = 2,columnspan=3) 

        #setting the table as per the products available to Purchase ###############

        label_1 =Label(root,text="Items available to Purchase", width=20,font=("bold",20),bg='grey', fg="white")
        label_1.grid(row = 2, column = 0, sticky = W, pady = 2,columnspan=3)


        #for displaying the table data set the table headings via label ##########
        e1 = Entry(root, width=20, fg='blue',bg ='yellow',font=('Arial',16,'bold'))
        e1.grid(row=4,column=0,ipadx=10, ipady=10, sticky="EW")
        e1.insert(END,"Product_id")

        e2 = Entry(root, width=20, fg='blue',bg ='yellow',font=('Arial',16,'bold'))
        e2.grid(row=4, column=1, ipadx=10, ipady=10, sticky="EW")
        e2.insert(END,"Product Description")

                          
        e3 = Entry(root, width=20, fg='blue',bg ='yellow',font=('Arial',16,'bold'))
        e3.grid(row=4, column=2, ipadx=10, ipady=10, sticky="EW")
        e3.insert(END,"Coins reqd to Purchase")

        ### display the catalogue table data in the Window in a table format #########
        global total_row 
        total_row= display_all_catalogue_data()  

        ## to give more gap
        total_row = total_row+6

        # Notify the user about the currnecy and coins he has ###

        user_currency_info_to_be_shown_in_gui(username)

        ### Ask the user what product he wants to buy ##########

        label_5 =Label(root,text="Please enter the product id for what you want ot buy :", width=40,font=("bold",20),bg='grey', fg="white")
        label_5.grid(row = 12+total_row, column = 0, sticky = W, pady = 2,columnspan =2)

        ## textbox to provide the product id which he wqants to buy based on products displayed in the table ########
        global e5
        e5=Entry(root)
        e5.grid(row=12+total_row, column=1)


        ############## call the function to validate whether user has money to buy based on username,  product_id and preferred mode of currency ######
        ### preferred mode of currency and product_id to be inputted by user in the GUI ##########
        text3 =""
        text4=""
        btn=Button(root, text='Submit', width=20,bg='yellow', fg='red')
        btn.grid(row=12+total_row, column=2)
        btn.bind('<Button-1>', onclick_purchase)


Python program to create a table to display the product catalogue data 

def display_all_catalogue_data():

          class Table:

                      def __init__(self,root):

                          # code for creating table
                          for i in range(total_rows):
                              for j in range(total_columns):

                                  self.e = Entry(root, width=20, fg='blue',bg='grey',
                                                font=('Arial',16,'bold'))
                  
                                  self.e.grid(row=5+i, column=j, ipadx=10, ipady=10, sticky="EW")
                                  self.e.insert(END, lst[i][j])

          # take the data

          lst = query_all_in_catalogue()

          # find total number of rows and
          # columns in list
          total_rows = len(lst)
          total_columns = len(lst[0])
          t = Table(root)
          return total_rows



#########################################
#Function to display the user currency and coin information ###
###########################################

def user_currency_info_to_be_shown_in_gui(username):
          # Notify the user about the currnecy and coins he has ###

          label_2 =Label(root,text="You have ", width=20,font=("bold",20),bg='grey', fg="white")
          label_2.grid(row = 7+total_row, column = 0, sticky = W, pady = 2)

          currency_1 = user_currency_coin_details(username)
          text1 = str(currency_1) + " coins "

          label_3 =Label(root,text=text1,bg="green", fg="yellow",  width=20,font=("bold",20))
          label_3.grid(row = 7+total_row, column = 1, sticky = W, pady = 2)




####################################################
# get User coin details#
##################################################

def user_currency_coin_details(username):

          item=()
          mycursor = mydb.cursor(prepared=True)
          sql_query="select  coins  from currency where username=%s"
          mycursor.execute(sql_query,(str(username),))
          for row in mycursor:
            item =(
                  row[0]
                  )
          return(item)  


#############################################

# Clicking on submit button in purchase module ###

###############################################
def onclick_purchase(event):
          product_availability_based_on_currency(username,str(e5.get()))



def product_availability_based_on_currency(username,productid):
            mycursor = mydb.cursor(prepared=True)

            ### check the product price in terms of  in catalogue table based on product id chosen by user############
            
            productid=int(productid)

            # check if product id given exists in DB 
            sql_query1="select count(*) from catalogue where product_id=%s"

            mycursor.execute(sql_query1,str(productid))
            for row in mycursor:
                item3 =(
                  row[0]
                  ) 

            if (item3 ==0):
              text3 ="Product id does not exist"  
              text4="Please select produc id from the above table "
            elif (item3 > 0):
                      sql_query="select coins_required from catalogue where product_id=%s"

                      mycursor.execute(sql_query,str(productid))
                      for row in mycursor:
                          item =(
                            row[0]
                            ) 
                      #### check  user coin from database ###########
                    
                      sql_query="select coins from currency where username=%s"
                      mycursor.execute(sql_query,(str(username),))
                    
                      for row in mycursor:
                          item1 =(
                            row[0]
                            )  

                    ### compare if user coin is enough to purchase the product he has chosen #######
                    ### if user has money , then purchase the product he has opted for and deduct the amount from his account ##################

                     
                      if (item1>=item):
                        item1= item1-item
                        text3 ="Congrats !Your purchase is succssful"
                        update_currency_or_coin_post_purchase(username,item1)
                        text4 = "Please check for your latest currency status above"
                      elif (item1<item):
                        text3 ="Sorry! You dont have enough money "

         
          #### update the GUI with the text3 message ###########
            label_6 =Label(root,text=text3,bg="yellow", width=40,font=("bold",20))
            label_6.grid(row = 15+total_row, column = 0, columnspan =3, sticky = W, pady = 2)

            label_7 =Label(root,text=text4, bg="yellow", width=40,font=("bold",20))
            label_7.grid(row = 17+total_row, column = 0,columnspan =3,sticky = W, pady = 2)

          #### call the function to display his latest money status ##########
            user_currency_info_to_be_shown_in_gui(username)

Sample output: 
Case 1: Pre purchase , display the product to purchase , and gives option to enter product id to purchase the corresponding product 
![image](https://user-images.githubusercontent.com/98585901/203064744-a07c4910-e4e6-4a4a-8075-08c3b4137d0a.png)

 

Post successful purchase , the user will be displayed with updated currency and a purchase confirmation message
 ![image](https://user-images.githubusercontent.com/98585901/203064806-5cfe7f66-c1b3-44d8-931e-07a55fdf0c3c.png)


Case 2 : If product id does not exist user will be prompted with the message that Product id does not exist to purchase
![image](https://user-images.githubusercontent.com/98585901/203064871-0cbfbcb2-d2be-408a-92e7-6c0473e7801b.png)

 

Case3 : If user does not have enough money to purchase, user will be prompted with the message that You don’t have enough money to purchase
 ![image](https://user-images.githubusercontent.com/98585901/203064934-aabebbe2-0e25-47da-8307-881ffee8f534.png)


F .  Admin Module 
Input: user should login as admin  
Output: 
o	If the logged-in user is an admin, he will be getting an additional admin module to add new quiz questions
o	The question_no will be auto incremented by one while adding new question in the database so that there is no two questions added with same question_no
o	All fields are mandatory for insert question UI , if anything is empty , it would prompt as mandatory.

List of database tables:
•	Questions1

Code 

##############################################
# Function to design the insert question UI form 
##################################################
def insert_question_form():
        label.destroy()
        label100.destroy()
        
        clearFrame()
        global root_insert
        root_insert=frame

        # label to display question form heading 
        label_insert_0 = Label(root_insert, text="Insert Question form",width=20,font=("bold", 40),bg='grey', fg="white")
        label_insert_0.place(x=90,y=53)
        # labek to read question level ( not used )
        label_insert_1 = Label(root_insert, text="*Question Level",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_1.place(x=80,y=130)
        # entry box to read question level 
        global entry_insert_1
        entry_insert_1 = Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_1.place(x=300,y=130)

        # label to read question description 
        label_insert_2 = Label(root_insert, text="Qestion Description",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_2.place(x=68,y=180)
        # entry box  to read question description 
        global entry_insert_2
        entry_insert_2 = Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_2.place(x=300,y=180)
        label_insert_3 = Label(root_insert, text="Option 1",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_3.place(x=70,y=230)
        global entry_insert_3
        entry_insert_3 = Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_3.place(x=300,y=230)
        
        label_insert_4 = Label(root_insert, text="Option 2",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_4.place(x=70,y=280)
        global entry_insert_4
        entry_insert_4 = Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_4.place(x=300,y=280)

        label_insert_5= Label(root_insert, text="Option 3",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_5.place(x=70,y=310)
        global entry_insert_5
        entry_insert_5 = Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_5.place(x=300,y=310)

        label_insert_6= Label(root_insert, text="Answer",width=20,font=("bold", 20),bg='grey', fg="white")
        label_insert_6.place(x=70,y=350)
        global entry_insert_6
        entry_insert_6= Entry(root_insert,width=20,bg='grey', fg="white")
        entry_insert_6.place(x=300,y=350)


        btn1=Button(root_insert, text='Submit', width=20,bg='yellow', fg='red')
        btn1.place(x=180,y=380)
        # on button click , call the function onlicki1_insert_data 
        btn1.bind('<Button-1>', onclick1_insert_data)

##########################################################
# Insert question in the database questions1 table as admin 
###########################################################

def  onclick1_insert_data(event):
        mycursor = mydb.cursor(prepared=True)  
        # validation for checking if q_level is empty , then show *mandatry next to teh q_level entry box 
        q_level =str(entry_insert_1.get())
        if (len(q_level) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=130)

         # validation for checking if qno_dssc is empty , then show *mandatry next to teh q_level entry box 
        qno_desc =str(entry_insert_2.get())
        if (len(qno_desc) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=180)

        opt_a =str(entry_insert_3.get())
        if (len(opt_a) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=230)
        
        opt_b =str(entry_insert_4.get())
        if (len(opt_a) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=280)
        
        opt_c =str(entry_insert_5.get())
        if (len(opt_a) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=310)

        ans =str(entry_insert_6.get())
        if (len(ans) == 0):
              label_reg_11 = Label(root_insert, text="*Mandatory",width=20,font=("bold", 20),bg='grey', fg="red")
              label_reg_11.place(x=500,y=330)
        

        # qno_no will be auto incremented , and inserted . For that , it will read the latest qno from db table and increment by 1 and then insert for new question 
        sql_query1 ="SELECT max(qno_no) + 1 FROM questions1"  
        mycursor.execute(sql_query1)
        for row in mycursor:
                item4 =(
                  row[0]
                  ) 
      
        if (item4 is None):
              item4=1;

        ###  insert new question in db table 
        insert_query1="insert into questions1(qno_no,q_level,qno_desc,opt_a,opt_b,opt_c,ans) values(%s,%s,%s,%s,%s,%s,%s)"

        mycursor.execute(insert_query1,(str(item4),str(q_level),str(qno_desc),str(opt_a),str(opt_b),str(opt_c),str(ans)))
        mydb.commit()

        # check if data is inserted 
        sql_query2="select count(*) from  questions1 where qno_no =%s"
        mycursor.execute(sql_query2,(str(item4),))
        for row in mycursor:
                item5 =(
                  row[0]
                  ) 
        
        if (item5==1):
              label_insert_7= Label(root_insert, text="Record Inserted Successfully",width=20,font=("bold", 20),bg='grey', fg="yellow")
              label_insert_7.place(x=70,y=430)


Sample output 
![image](https://user-images.githubusercontent.com/98585901/203065026-10b1107a-58b5-4697-baba-d9fe410b96e6.png)

 


Message for successful record insertion 


![image](https://user-images.githubusercontent.com/98585901/203065195-ef5b36a5-c949-40d0-a0cb-68710e84b7f0.png)

 


Bibliography
List of reference links:
https://docs.python.org/3/library/tkinter.html
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://www.geeksforgeeks.org/create-mysql-database-login-page-in-python-using-tkinter/
https://www.plus2net.com/python/tkinter-mysql.php

