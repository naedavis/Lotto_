# Naeemah Davis
# Login Screen - Lotto
# Imports
# logins naeemah,0112345678910
from tkinter import *
from tkinter import messagebox
# Import for use of images later on
from PIL import ImageTk, Image
# Importing from Lottochoose screen the function where the screen is kept
from lottochoose import draw_lotto_screen

# Creating an empty string variable outside of the function to allow me to call this variable in another screen
current_user = ""


# Function that holds this screen, its design and its functions
def draw():
    main = Tk()
    main.geometry("700x700")
    main.config(bg="white")
    main.title("Login")

    #   function for changing screen from Login to Sign-Up
    def sign_up():
        main.destroy()
        import signup

    labelframe = LabelFrame(main, bg="#a11d33")
    labelframe.place(x=0, y=0, width=700, height=70)
    logins = Label(main, text="player id:naeemah, id: 0112345678910")
    logins.place(x=10, y=80)

#   Opening the image
    user_img = Image.open("./userform.jpg")
#   Resizing the image
    user_img = user_img.resize((200, 150))
#   storing the image in a variable
    test = ImageTk.PhotoImage(user_img)
#   displaying the image on a label
    lbl_img = Label(image=test)
    lbl_img.image = test
    lbl_img.place(x=250, y=100)

#   button that calls the sign up function defined above
#   highlightthickness, bd and relief used to allow button to not look like a button but to blend in with background
    btn_signup = Button(main, highlightthickness=0, bd=0, text="Sign-Up", fg="white", bg="#a11d33", font=" Arial 25",
                        command=sign_up, relief="sunken")
    btn_signup.place(x=500, y=7)
    lbl_player = Label(main, text="Player_Id", bg="white", fg="#a11d33", font="Arial 20 bold")
    lbl_player.place(x=200, y=260)
    e_name = Entry(main, fg="#a11d33", font="Arial 20 bold")
    e_name.place(x=200, y=300)
#   when Login is run, user will be able to enter details immediately instead of having to click first and then enter
    e_name.focus_set()
    lbl_id = Label(main, text="ID Number", bg="white", fg="#a11d33", font="Arial 20 bold")
    lbl_id.place(x=200, y=360)
    e_id = Entry(main, fg="#a11d33", font="Arial 20 bold")
    e_id.place(x=200, y=400)

#   function that checks if details entered correspond with previously entered details when signed-up
    def login():
        try:
            # reading user file that contains login information only
            reader = open("./users.txt", "r")
            file = reader.read()
            users = file.split("\n")

            # loop to check if username and password is the same
            for user in users:
                if user == "":
                    continue
                # variables that store the two values in users text file
                username = user.split(",")[0]
                id_number = user.split(",")[1]
                # only if both username and id both correspond do the following
                if username == e_name.get() and id_number == e_id.get():
                    messagebox.showinfo("Log in Successful", "Welcome " + e_name.get() + " Lets begin!")
                    current_user = e_id.get()
                    main.destroy()
                    # calling the function that the next screen is in because
                    # we want to keep the id number in a current user variable that was initially empty in the beginning
                    draw_lotto_screen(current_user)
                # else if either username or id doesnt match whats in the users text file do the following
                elif username != e_name.get() or id_number != e_id.get():
                    messagebox.showinfo("Error", "Invalid information entered")
                    e_name.delete(0, END)
                    e_id.delete(0, END)
                    e_name.focus_set()

        except:
            messagebox.showinfo("Error", "Invalid information entered" + "\n" + "Please try again or Sign Up")
#   calling the function that checks the login details entered
    btn_login = Button(main, text="Login", bg="#a11d33", fg="white", font="Arial 20 bold", command=login)
    btn_login.place(x=300, y=500)

    main.mainloop()

# without these lines the login screen will not display
if __name__ == '__main__':
#   function where login style and functions are stored is being called to run
    draw()

