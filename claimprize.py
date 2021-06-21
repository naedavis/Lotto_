# Naeemah Davis
# Claim Prize Screen - Lotto
# Imports
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image


def claim_prize_screen(prize_amount, currency_label, current_user):
    claim = Tk()
    claim.geometry("800x800")
    claim.config(bg="white")
    claim.title("Claim Prize")

    # submit function
    def submit():
        try:
            for letter in acc_holder.get():
                if not letter.isalnum() and letter not in " '-":
                    messagebox.showinfo("Invalid")
                else:
                    pass
                continue
            messagebox.showinfo("Confirmation",
                                "We've emailed you with further instructions" + "\n" + "Please Check your email")
            print("current user", current_user)
            reader = open("./player_details.txt", "r")
            file = reader.read()
            users = file.split("\n")
            print("users", users)

            for user in users:
                if user == "":
                    continue
                print("user", user)
                id_no = user.split(",")[1]
                if current_user == id_no:
                    email = user.split(",")[2]
                    address = user.split(",")[3]
                    sender_email_id = 'lottogirl92@gmail.com'
                    receiver_email_id = [email]
                    password = "loahdtTvc473!&"
                    subject = "Confirmation"
                    msg = MIMEMultipart()
                    msg['From'] = sender_email_id
                    msg['To'] = ', '.join(receiver_email_id)
                    msg['Subject'] = subject
                    body = "Congratulations on your win! \n" \
                           "Your Winnings: {} {}  \n" \
                           " ...Your details... \n" \
                           "Account Holder: {} \n" \
                           "Account Number: {} \n" \
                           "Bank: \n" \
                           "Player ID: {} \n" \
                           "Address: {} \n".format(currency_label[3], prize_amount, acc_holder.get(), acc_num.get(),
                                                   current_user, address)
                    body = body + "Thank you"
                    msg.attach(MIMEText(body, 'plain'))
                    text = msg.as_string()
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    # start TLS for security
                    s.starttls()
                    # Authentication
                    s.login(sender_email_id, password)
                    # sending the mail
                    s.sendmail(sender_email_id, receiver_email_id, text)
                    # terminating the session
                    s.quit()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid Details")
        except TypeError:
            messagebox.showerror("Error", "Please enter valid Details")
        except ConnectionError:
            messagebox.showerror("Error", "Please connect to wifi")

    strv = StringVar(claim)
    strVar = StringVar()
    intVar = IntVar()
    labelframe = LabelFrame(claim, bg="#a11d33")
    labelframe.place(x=0, y=0, width=800, height=70)
    lbl = Label(claim, text="Enter you Banking Details", font="Arial 25 bold", bg="#a11d33", fg="white")
    lbl.place(x=200, y=10)
    l_acc_holder = Label(claim, text="Account Holder Name:", font="Arial 20 bold", fg="#a11d33", bg="white")
    l_acc_holder.place(x=200, y=160)
    acc_holder = Entry(claim, font="Arial 25 bold", fg="#a11d33", bg="white", textvariable=strVar)
    acc_holder.place(x=200, y=200)
    l_acc_holder = Label(claim, text="Account Number:", font="Arial 20 bold", fg="#a11d33", bg="white")
    l_acc_holder.place(x=200, y=260)
    acc_num = Entry(claim, font="Arial 25 bold", fg="#a11d33", bg="white", textvariable=intVar)
    acc_num.place(x=200, y=300)
    l_acc_hol = Label(claim, text="Choose your Bank:", font="Arial 20 bold", fg="#a11d33", bg="white")
    l_acc_hol.place(x=200, y=360)

    banks = {"ABSA", "NedBank", "FNB", "Standard Bank", "Capitec"}
    strv.set("Choose a bank")  # set the default option
    bank_menu = OptionMenu(claim, strv, *banks)
    bank_menu.config(bg="white", fg="#a11d33", font="Arial 20 bold")
    bank_menu["menu"].config(bg="#a11d33", fg="white", font="Arial 20 bold")
    bank_menu.place(x=200, y=400, width=390, height=50)
    btn_submit = Button(claim, text="Submit", font="Arial 25 bold", bg="white", fg="#a11d33", command=submit)
    btn_submit.place(x=310, y=550)

    def play_again():
        from lottochoose import draw_lotto_screen
        claim.destroy()
        draw_lotto_screen(current_user)

    btn_play = Button(claim, text="Play Again", font="Arial 25 bold", bg="white", fg="#a11d33", command=play_again)
    btn_play.place(x=270, y=650)

    def clear():
        strv.set("Choose a bank")
        acc_num.delete(0, END)
        acc_holder.delete(0, END)

    btn_clear = Button(claim, text="Clear", font="Arial 25 bold", bg="white", fg="#a11d33", command=clear)
    btn_clear.place(x=100, y=650, width=140)

    def exit_app():
        msg = messagebox.askquestion("Exit Application?", "Are you sure you want to Exit")
        if msg == "yes":
            claim.destroy()
        else:
            pass

    btn_exit = Button(claim, text="Exit", font="Arial 25 bold", bg="white", fg="#a11d33", command=exit_app)
    btn_exit.place(x=500, y=650, width=140)

    claim.mainloop()


if __name__ == '__main__':
    claim_prize_screen("", "", "")
