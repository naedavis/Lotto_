# Naeemah davis
# Sign-Up Screen - Lotto
# Imports
from tkinter import *
from tkinter import messagebox
import datetime
# Importing from login screen the function where the screen is kept
from main import draw

signup = Tk()
signup.geometry("700x700")
signup.config(bg="white")
signup.title("Sign Up Here")

labelframe = LabelFrame(signup, bg="#a11d33")
labelframe.place(x=0, y=0, width=700, height=70)

lbl_name = Label(signup, text="Name", bg="white", fg="#a11d33", font="Arial 20 bold")
lbl_name.place(x=200, y=120)
e_name = Entry(signup, fg="#a11d33", font="Arial 20 bold")
e_name.place(x=200, y=150)
lbl_Id = Label(signup, text="I.D No", bg="white", fg="#a11d33", font="Arial 20 bold")
lbl_Id.place(x=200, y=220)
e_Id = Entry(signup, fg="#a11d33", font="Arial 20 bold")
e_Id.place(x=200, y=250)
lbl_email = Label(signup, text="Email", bg="white", fg="#a11d33", font="Arial 20 bold")
lbl_email.place(x=200, y=320)
e_email = Entry(signup, fg="#a11d33", font="Arial 20 bold")
e_email.place(x=200, y=350)
lbl_address = Label(signup, text="Address", bg="white", fg="#a11d33", font="Arial 20 bold")
lbl_address.place(x=200, y=420)
e_address = Entry(signup, fg="#a11d33", font="Arial 20 bold")
e_address.place(x=200, y=450)


# function to validate details entered upon signing-up
def register():
    # list with values to loop through later
    fields = [e_name, e_Id, e_email, e_address]
    empty_fields = False

    # check if there are empty fields
    for field in fields:
        if field.get() == "":
            # if empty fields found, stop loop and show error
            empty_fields = True
            messagebox.showinfo("Error", 'Make sure all Fields are entered ')
            break
    # if no empty fields start validation
    if empty_fields == False:
        # checking the age of user based on ID number entered
        id = e_Id.get()
        year_id = id[0:2]
        if int(year_id[0:1]) == 0:
            century = 2000
        else:
            century = 1900
        year_of_birth = century + int(year_id)
        x = datetime.datetime.now()
        curr_year = x.year
        age = curr_year - year_of_birth

        #       Validations
        if age >= 18:  # age validation
            if len(id) == 13:  # ID validation
                if "@" and "." in e_email.get():  # email validation
                    # address validation
                    if "Street" in e_address.get() or "Road" in e_address.get() or "Close" in e_address.get()\
                            or "Avenue" in e_address.get() or "Laan" in e_address.get() or "Weg" in e_address.get():
                        # reads from the file to later check if user exists based on entered info
                        f = open("./player_details.txt", "r")
                        file = f.read()  # read from the file
                        player_details = file.split("\n")  # converting the text file into a list of rows
                        f.close()

                        g = open("./users.txt", "r")
                        file2 = g.read()
                        users = file2.split("\n")
                        g.close()
                        user_exists = False

                        # check if user exists
                        for user in users:
                            if user == "":
                                continue

                            name = user.split(",")[0]  # get name of user in users.txt

                            if e_name.get() == name:
                                user_exists = True
                                break  # stop loop because a user already exists

                        if user_exists == True:
                            messagebox.showinfo("Invalid ", "This name already exists")
                        else:
                            # if user doesn't exist
                            # variables to be called when writing to player detail files
                            player_detail_str = e_name.get() + "," + e_Id.get() + "," + e_email.get() + "," + e_address.get()
                            user_str = e_name.get() + "," + e_Id.get()

                            # append to text files, captured info
                            player_details.append(player_detail_str)
                            users.append(user_str)

                            # convert the list to a string with new lines
                            new_player_details = "\n".join(player_details)
                            new_users = "\n".join(users)

                            # open the file with write mode
                            f = open("./player_details.txt", "w")
                            f.write(new_player_details)
                            f.close()

                            g = open("./users.txt", "w")
                            g.write(new_users)
                            g.close()

                            messagebox.showinfo("Successful", "Congratulations, " + e_name.get() + " Lets begin")
                            signup.destroy()
                            draw()


                    else:
                        messagebox.showinfo("Error", "Enter valid Address")
                else:
                    messagebox.showinfo("Error", "Enter valid Email")
            else:
                messagebox.showinfo("Error", "Invalid ID length")
        else:
            messagebox.showinfo("Age Error",
                                "You are too young" + "\n" + "Please try again in " + str(18 - age) + "year/s.")
            signup.destroy()


btn_submit = Button(signup, text="Submit", bg="#a11d33", fg="white", font="Arial 20 bold", command=register)
btn_submit.place(x=300, y=550)

signup.mainloop()
