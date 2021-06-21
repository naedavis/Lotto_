# Naeemah Davis
# Displays Lotto Numbers Winnings - Lotto
# Imports
from random import random
from tkinter import *
from tkinter import messagebox
import random
import requests

from claimprize import claim_prize_screen

# Two empty strings to store future data that will be used on the Claim Prize Screen
prize_amount = ""
currency_label = ""


# Function that holds all the styles and functions of this screen
# parameter of current user, got from login screen
def create_lotto_screen(current_user):
    display = Tk()
    display.geometry("800x800")
    display.config(bg="white")
    display.title("Lucky Lotto Numbers")

    # Dictionary that holds the prize amounts
    prize_dict = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
    labelframe = LabelFrame(display, bg="#a11d33")
    labelframe.place(x=0, y=0, width=800, height=70)
    lbl_numbers = Label(display, text="Your Numbers", font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl_numbers.place(x=270, y=230)
    lbl1 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl1.place(x=100, y=300)
    lbl2 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl2.place(x=200, y=300)
    lbl3 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl3.place(x=300, y=300)
    lbl4 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl4.place(x=400, y=300)
    lbl5 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl5.place(x=500, y=300)
    lbl6 = Label(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl6.place(x=600, y=300)

    lbl_lotto = Label(display, text="Lotto Numbers", font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl_lotto.place(x=270, y=100)
    lbl_congrats = Label(display, text="Congratulations, you win:", font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl_congrats.place(x=200, y=400)
    lbl_currency = Label(display, text="R", font="Arial 25 bold", fg="#a11d33", bg="white")
    lbl_currency.place(x=210, y=520)
    e_prize = Entry(display, font="Arial 25 bold", fg="#a11d33", bg="white")
    e_prize.place(x=270, y=490, width=250, height=100)

    # checks the Internet Connection for the Exchange Rate API
    try:
        url = 'https://v6.exchangerate-api.com/v6/cd7eab3c2969e0278d18a265/latest/ZAR'
        response = requests.get(url)
        data = response.json()
        conversions = data['conversion_rates']
        # stores the updated values for each currency in variables
        usd = conversions["USD"]
        zar = conversions["ZAR"]
        aud = conversions["AUD"]
        nzd = conversions["NZD"]
        eur = conversions["EUR"]
        kwd = conversions["KWD"]
        omr = conversions["OMR"]
    # to make sure that if there is no internet it will show an error and not break
    except requests.exceptions.ConnectionError as x:
        messagebox.showinfo("error", "Connection Error")

    # Function that checks the selected option from the menu and converts the value in the entry accordingly
    def currency(item):
        strv.set(item)
        # if user chooses a value in Option menu
        # Prize will be converted to that values currency based on exchange rate API
        if item == "AUD":
            # Take the initial ZAR amount and multiply it by AUD rate
            convert = float(e_prize.get()) * aud
            # clear prize entry to avoid double numbers
            e_prize.delete(0, END)
            # round off value to two decimal places
            convert = round(convert, 2)
            # insert variable in prize entry
            e_prize.insert(0, convert)
            # change the label next to the entry to its currency symbol
            lbl_currency.config(text="$")
        elif item == "NZD":
            convert = float(e_prize.get()) * nzd
            e_prize.delete(0, END)
            convert = round(convert, 2)
            e_prize.insert(0, convert)
            lbl_currency.config(text="$")
        elif item == "EUR":
            convert = float(e_prize.get()) * eur
            e_prize.delete(0, END)
            convert = round(convert, 2)
            e_prize.insert(0, convert)
            lbl_currency.config(text="€")
        elif item == "KWD":
            convert = float(e_prize.get()) * kwd
            e_prize.delete(0, END)
            convert = round(convert, 2)
            e_prize.insert(0, convert)
            lbl_currency.config(text="د.ك")
        elif item == "OMR":
            convert = float(e_prize.get()) * omr
            e_prize.delete(0, END)
            convert = round(convert, 2)
            e_prize.insert(0, convert)
            lbl_currency.config(text="ر.ع.")
        elif item == "USD":
            convert = float(e_prize.get()) * round(usd, 2)
            e_prize.delete(0, END)
            convert = round(convert, 2)
            e_prize.insert(0, convert)
            lbl_currency.config(text="$")

    strv = StringVar(display)
    banks = {"USD", "AUD", "NZD", "EUR", "KWD", "OMR"}
    strv.set(["ZAR"])  # set the default option
    bank_menu = OptionMenu(display, strv, *banks, command=currency)
    bank_menu.config(bg="white", fg="#a11d33", font="Arial 20 bold")
    bank_menu["menu"].config(bg="#a11d33", fg="white", font="Arial 20 bold")
    bank_menu.place(x=550, y=510, width=140)

    # reading file because the numbers the person chose is still in there
    # and needs to be read so i can take them out and print them on this screen
    reader = open("./player_lotto.txt", "r")
    file = reader.read()
    users = file.split("\n")
    # getting the last line in that file
    last_line = users[-1]
    split_line = last_line.split("|")
    your_numbers = []
    raw_numbers = split_line[2].split(",")
    # loop through the numbers and add each on to the empty list created above

    for num in raw_numbers:
        your_numbers.append(int(num))

    # setting each index of each number in the now not empty list to a variable
    num1 = your_numbers[0]
    num2 = your_numbers[1]
    num3 = your_numbers[2]
    num4 = your_numbers[3]
    num5 = your_numbers[4]
    num6 = your_numbers[5]

    # placing the numbers extracted on the new screen to be displayed along with Lotto numbers
    lbl1.config(text=num1)
    lbl2.config(text=num2)
    lbl3.config(text=num3)
    lbl4.config(text=num4)
    lbl5.config(text=num5)
    lbl6.config(text=num6)

    # function for when you click the claim button
    def claim():
        # takes the value in the entry
        prize_amount = e_prize.get()
        # along with the label so we know which currency it's in
        currency_label = lbl_currency.config("text")
        msg = messagebox.askquestion("Claim prize", "Are you sure you want to claim ?")
        if msg == "yes":
            display.destroy()
            # imports the claim prize screen with the parameters so they can be accessed in that screen as well
            claim_prize_screen(prize_amount, currency_label, current_user)
        else:
            pass

    # play again function
    def play_again():
        from lottochoose import draw_lotto_screen
        display.destroy()

        draw_lotto_screen(current_user)

    # exit function
    def exit_app():
        msg = messagebox.askquestion("Exit Application?", "Are you sure you want to Exit")
        if msg == "yes":
            display.destroy()
        else:
            pass

    btn_claim = Button(display, text="Claim", font="Arial 25 bold", bg="white", fg="#a11d33", command=claim)
    btn_claim.place(x=100, y=650, width=140)
    btn_play = Button(display, text="Play Again", font="Arial 25 bold", bg="white", fg="#a11d33", command=play_again)
    btn_play.place(x=270, y=650)
    btn_exit = Button(display, text="Exit", font="Arial 25 bold", bg="white", fg="#a11d33", command=exit_app)
    btn_exit.place(x=500, y=650, width=140)

    test_r = PhotoImage(file="red.png")
    img_r = Label(display, text="1", fg="white", bg="white", border="0", image=test_r)
    img_r.image = test_r
    img_r.place(x=100, y=150, width=50, height=50)

    test_b = PhotoImage(file="blue.png")
    img_b = Label(bg="white", border="0", image=test_b)
    img_b.image = test_b
    img_b.place(x=200, y=150, width=50, height=50)

    test_g = PhotoImage(file="green.png")
    img_g = Label(bg="white", border="0", image=test_g)
    img_g.image = test_g
    img_g.place(x=300, y=150, width=50, height=50)

    test_o = PhotoImage(file="orange.png")
    img_o = Label(bg="white", border="0", image=test_o)
    img_o.image = test_o
    img_o.place(x=400, y=150, width=50, height=50)

    test_p = PhotoImage(file="pink.png")
    img_p = Label(bg="white", border="0", image=test_p)
    img_p.image = test_p
    img_p.place(x=500, y=150, width=50, height=50)

    test_pur = PhotoImage(file="purple.png")
    img_pur = Label(bg="white", border="0", image=test_pur)
    img_pur.image = test_pur
    img_pur.place(x=600, y=150, width=50, height=50)

    # empty list
    random_list = []

    # loop to get random numbers
    while len(random_list) < 6:
        n = random.randint(1, 49)
        if n not in random_list:  # to make sure that there are no duplicates when getting the random numbers
            random_list.append(n)


    random_list.sort()
    your_numbers.sort()
    # empty list
    same_list = []
    # if numbers are same in both then add them to the empty list
    for num in your_numbers:
        if num in random_list:
            same_list.append(num)
    # holds the length of list
    # so we know how many are the same
    length = len(same_list)
    # loop through the dictionary that holds prize amounts
    for key in prize_dict:
        if key == length:
            # if length is simialr to a key in prize dictionary,
            # set the value of that dictionary to prize_amount variable
            prize_amount = prize_dict[key]

    e_prize.insert(0, prize_amount)

    lbl_r = Button(display, highlightthickness=0, text=random_list[0], fg="white", bd="0", font="Arial 17 bold",
                   bg="#e84404")
    lbl_r.place(x=110, y=160, width=30, height=30)
    lbl_b = Button(display, highlightthickness=0, text=random_list[1], fg="white", bd="0", font="Arial 17 bold",
                   bg="#48c4fc")
    lbl_b.place(x=210, y=160, width=30, height=30)
    lbl_g = Button(display, highlightthickness=0, text=random_list[2], fg="white", bd="0", font="Arial 17 bold",
                   bg="#a8d484")
    lbl_g.place(x=310, y=160, width=30, height=30)
    lbl_o = Button(display, highlightthickness=0, text=random_list[3], fg="white", bd="0", font="Arial 17 bold",
                   bg="#ffa404")
    lbl_o.place(x=410, y=160, width=30, height=30)
    lbl_p = Button(display, highlightthickness=0, text=random_list[4], fg="white", bd="0", font="Arial 17 bold",
                   bg="#e8248c")
    lbl_p.place(x=510, y=160, width=30, height=30)
    lbl_pur = Button(display, highlightthickness=0, text=random_list[5], fg="white", bd="0", font="Arial 17 bold",
                     bg="#446ce8")
    lbl_pur.place(x=610, y=160, width=30, height=30)

    display.mainloop()


if __name__ == '__main__':
    create_lotto_screen("")
