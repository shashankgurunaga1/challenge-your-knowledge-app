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
