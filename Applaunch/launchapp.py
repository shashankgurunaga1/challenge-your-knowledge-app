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
