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
