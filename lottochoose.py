# Naeemah Davis
# Choosing your numbers Screen - Lotto
# Imports
from datetime import datetime
from tkinter import *
from playsound import playsound
from tkinter import messagebox

from lottodisplay import create_lotto_screen




# function with this screens styles and functions
def draw_lotto_screen(current_user):
    window = Tk()
    window.geometry("800x800")
    window.config(bg="white")
    window.resizable(width="false", height="false")

    labelframe = LabelFrame(window, bg="#a11d33")
    labelframe.place(x=0, y=0, width=800, height=70)

    lbl_choose = Label(window, text="Choose your numbers", font="Arial 25 bold", bg="#a11d33", fg="white")
    lbl_choose.place(x=180, y=15)

    # 6 entries
    e_1 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_1.place(x=80, y=100, width=50, height=50)
    e_2 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_2.place(x=180, y=100, width=50, height=50)
    e_3 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_3.place(x=280, y=100, width=50, height=50)
    e_4 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_4.place(x=380, y=100, width=50, height=50)
    e_5 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_5.place(x=480, y=100, width=50, height=50)
    e_6 = Entry(window, font="Arial 25 bold", bg="white", fg="#a11d33")
    e_6.place(x=580, y=100, width=50, height=50)

    # functions (line 42 - 1188)
    # when number is clicked it will check if there is a value in the entry
    # and if not it will insert that chosen number in the open entry
    def num1():
        # variable that holds the text of the button
        n1 = lbl1.config("text")
        # if entry 1 is empty
        # insert text above in empty entry
        # buttons are disabled after clicking to prevent duplicate numbers
        if e_1.get() == "":
            e_1.insert(0, n1[4])
            lbl1.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n1[4])
            lbl1.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n1[4])
            lbl1.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n1[4])
            lbl1.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n1[4])
            lbl1.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n1[4])
            lbl1.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num2():
        n2 = lbl2.config("text")
        if e_1.get() == "":
            e_1.insert(0, n2[4])
            lbl2.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n2[4])
            lbl2.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n2[4])
            lbl2.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n2[4])
            lbl2.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n2[4])
            lbl2.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n2[4])
            lbl2.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num3():
        n3 = lbl3.config("text")
        if e_1.get() == "":
            e_1.insert(0, n3[4])
            lbl3.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n3[4])
            lbl3.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n3[4])
            lbl3.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n3[4])
            lbl3.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n3[4])
            lbl3.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n3[4])
            lbl3.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num4():
        n4 = lbl4.config("text")
        if e_1.get() == "":
            e_1.insert(0, n4[4])
            lbl4.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n4[4])
            lbl4.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n4[4])
            lbl4.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n4[4])
            lbl4.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n4[4])
            lbl4.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n4[4])
            lbl4.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num5():
        n5 = lbl5.config("text")
        if e_1.get() == "":
            e_1.insert(0, n5[4])
            lbl5.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n5[4])
            lbl5.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n5[4])
            lbl5.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n5[4])
            lbl5.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n5[4])
            lbl5.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n5[4])
            lbl5.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num6():
        n6 = lbl6.config("text")
        if e_1.get() == "":
            e_1.insert(0, n6[4])
            lbl6.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n6[4])
            lbl6.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n6[4])
            lbl6.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n6[4])
            lbl6.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n6[4])
            lbl6.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n6[4])
            lbl6.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num7():
        n7 = lbl7.config("text")
        if e_1.get() == "":
            e_1.insert(0, n7[4])
            lbl7.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n7[4])
            lbl7.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n7[4])
            lbl7.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n7[4])
            lbl7.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n7[4])
            lbl7.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n7[4])
            lbl7.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num8():
        n8 = lbl8.config("text")
        if e_1.get() == "":
            e_1.insert(0, n8[4])
            lbl8.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n8[4])
            lbl8.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n8[4])
            lbl8.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n8[4])
            lbl8.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n8[4])
            lbl8.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n8[4])
            lbl8.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num9():
        n9 = lbl9.config("text")
        if e_1.get() == "":
            e_1.insert(0, n9[4])
            lbl9.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n9[4])
            lbl9.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n9[4])
            lbl9.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n9[4])
            lbl9.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n9[4])
            lbl9.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n9[4])
            lbl9.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num10():
        n10 = lbl10.config("text")
        if e_1.get() == "":
            e_1.insert(0, n10[4])
            lbl10.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n10[4])
            lbl10.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n10[4])
            lbl10.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n10[4])
            lbl10.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n10[4])
            lbl10.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n10[4])
            lbl10.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num11():
        n11 = lbl11.config("text")
        if e_1.get() == "":
            e_1.insert(0, n11[4])
            lbl11.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n11[4])
            lbl11.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n11[4])
            lbl11.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n11[4])
            lbl11.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n11[4])
            lbl11.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n11[4])
            lbl11.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num12():
        n12 = lbl12.config("text")
        if e_1.get() == "":
            e_1.insert(0, n12[4])
            lbl12.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n12[4])
            lbl12.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n12[4])
            lbl12.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n12[4])
            lbl12.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n12[4])
            lbl12.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n12[4])
            lbl12.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num13():
        n13 = lbl13.config("text")
        if e_1.get() == "":
            e_1.insert(0, n13[4])
            lbl13.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n13[4])
            lbl13.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n13[4])
            lbl13.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n13[4])
            lbl13.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n13[4])
            lbl13.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n13[4])
            lbl13.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num14():
        n14 = lbl14.config("text")
        if e_1.get() == "":
            e_1.insert(0, n14[4])
            lbl14.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n14[4])
            lbl14.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n14[4])
            lbl14.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n14[4])
            lbl14.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n14[4])
            lbl14.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n14[4])
            lbl14.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num15():
        n15 = lbl15.config("text")
        if e_1.get() == "":
            e_1.insert(0, n15[4])
            lbl15.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n15[4])
            lbl15.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n15[4])
            lbl15.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n15[4])
            lbl15.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n15[4])
            lbl15.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n15[4])
            lbl15.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num16():
        n16 = lbl16.config("text")
        if e_1.get() == "":
            e_1.insert(0, n16[4])
            lbl16.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n16[4])
            lbl16.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n16[4])
            lbl16.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n16[4])
            lbl16.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n16[4])
            lbl16.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n16[4])
            lbl16.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num17():
        n17 = lbl17.config("text")
        if e_1.get() == "":
            e_1.insert(0, n17[4])
            lbl17.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n17[4])
            lbl17.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n17[4])
            lbl17.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n17[4])
            lbl17.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n17[4])
            lbl17.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n17[4])
            lbl17.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num18():
        n18 = lbl18.config("text")
        if e_1.get() == "":
            e_1.insert(0, n18[4])
            lbl18.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n18[4])
            lbl18.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n18[4])
            lbl18.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n18[4])
            lbl18.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n18[4])
            lbl18.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n18[4])
            lbl18.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num19():
        n19 = lbl19.config("text")
        if e_1.get() == "":
            e_1.insert(0, n19[4])
            lbl19.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n19[4])
            lbl19.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n19[4])
            lbl19.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n19[4])
            lbl19.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n19[4])
            lbl19.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n19[4])
            lbl19.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num20():
        n20 = lbl20.config("text")
        if e_1.get() == "":
            e_1.insert(0, n20[4])
            lbl20.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n20[4])
            lbl20.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n20[4])
            lbl20.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n20[4])
            lbl20.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n20[4])
            lbl20.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n20[4])
            lbl20.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num21():
        n21 = lbl21.config("text")
        if e_1.get() == "":
            e_1.insert(0, n21[4])
            lbl21.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n21[4])
            lbl21.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n21[4])
            lbl21.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n21[4])
            lbl21.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n21[4])
            lbl21.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n21[4])
            lbl21.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num22():
        n22 = lbl22.config("text")
        if e_1.get() == "":
            e_1.insert(0, n22[4])
            lbl22.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n22[4])
            lbl22.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n22[4])
            lbl22.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n22[4])
            lbl22.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n22[4])
            lbl22.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n22[4])
            lbl22.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num23():
        n23 = lbl23.config("text")
        if e_1.get() == "":
            e_1.insert(0, n23[4])
            lbl23.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n23[4])
            lbl23.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n23[4])
            lbl23.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n23[4])
            lbl23.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n23[4])
            lbl23.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n23[4])
            lbl23.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num24():
        n24 = lbl24.config("text")
        if e_1.get() == "":
            e_1.insert(0, n24[4])
            lbl24.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n24[4])
            lbl24.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n24[4])
            lbl24.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n24[4])
            lbl24.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n24[4])
            lbl24.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n24[4])
            lbl24.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num25():
        n25 = lbl25.config("text")
        if e_1.get() == "":
            e_1.insert(0, n25[4])
            lbl25.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n25[4])
            lbl25.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n25[4])
            lbl25.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n25[4])
            lbl25.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n25[4])
            lbl25.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n25[4])
            lbl25.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num26():
        n26 = lbl26.config("text")
        if e_1.get() == "":
            e_1.insert(0, n26[4])
            lbl26.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n26[4])
            lbl26.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n26[4])
            lbl26.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n26[4])
            lbl26.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n26[4])
            lbl26.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n26[4])
            lbl26.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num27():
        n27 = lbl27.config("text")
        if e_1.get() == "":
            e_1.insert(0, n27[4])
            lbl27.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n27[4])
            lbl27.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n27[4])
            lbl27.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n27[4])
            lbl27.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n27[4])
            lbl27.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n27[4])
            lbl27.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num28():
        n28 = lbl28.config("text")
        if e_1.get() == "":
            e_1.insert(0, n28[4])
            lbl28.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n28[4])
            lbl28.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n28[4])
            lbl28.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n28[4])
            lbl28.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n28[4])
            lbl28.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n28[4])
            lbl28.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num29():
        n29 = lbl29.config("text")
        if e_1.get() == "":
            e_1.insert(0, n29[4])
            lbl29.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n29[4])
            lbl29.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n29[4])
            lbl29.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n29[4])
            lbl29.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n29[4])
            lbl29.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n29[4])
            lbl29.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num30():
        n30 = lbl30.config("text")
        if e_1.get() == "":
            e_1.insert(0, n30[4])
            lbl30.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n30[4])
            lbl30.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n30[4])
            lbl30.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n30[4])
            lbl30.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n30[4])
            lbl30.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n30[4])
            lbl30.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num31():
        n31 = lbl31.config("text")
        if e_1.get() == "":
            e_1.insert(0, n31[4])
            lbl31.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n31[4])
            lbl31.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n31[4])
            lbl31.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n31[4])
            lbl31.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n31[4])
            lbl31.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n31[4])
            lbl31.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num32():
        n32 = lbl32.config("text")
        if e_1.get() == "":
            e_1.insert(0, n32[4])
            lbl32.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n32[4])
            lbl32.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n32[4])
            lbl32.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n32[4])
            lbl32.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n32[4])
            lbl32.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n32[4])
            lbl32.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num33():
        n33 = lbl33.config("text")
        if e_1.get() == "":
            e_1.insert(0, n33[4])
            lbl33.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n33[4])
            lbl33.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n33[4])
            lbl33.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n33[4])
            lbl33.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n33[4])
            lbl33.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n33[4])
            lbl33.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num34():
        n34 = lbl34.config("text")
        if e_1.get() == "":
            e_1.insert(0, n34[4])
            lbl34.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n34[4])
            lbl34.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n34[4])
            lbl34.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n34[4])
            lbl34.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n34[4])
            lbl34.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n34[4])
            lbl34.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num35():
        n35 = lbl35.config("text")
        if e_1.get() == "":
            e_1.insert(0, n35[4])
            lbl35.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n35[4])
            lbl35.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n35[4])
            lbl35.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n35[4])
            lbl35.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n35[4])
            lbl35.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n35[4])
            lbl35.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num36():
        n36 = lbl36.config("text")
        if e_1.get() == "":
            e_1.insert(0, n36[4])
            lbl36.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n36[4])
            lbl36.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n36[4])
            lbl36.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n36[4])
            lbl36.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n36[4])
            lbl36.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n36[4])
            lbl36.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num37():
        n37 = lbl37.config("text")
        if e_1.get() == "":
            e_1.insert(0, n37[4])
            lbl37.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n37[4])
            lbl37.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n37[4])
            lbl37.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n37[4])
            lbl37.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n37[4])
            lbl37.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n37[4])
            lbl37.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num38():
        n38 = lbl38.config("text")
        if e_1.get() == "":
            e_1.insert(0, n38[4])
            lbl38.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n38[4])
            lbl38.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n38[4])
            lbl38.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n38[4])
            lbl38.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n38[4])
            lbl38.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n38[4])
            lbl38.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num39():
        n39 = lbl39.config("text")
        if e_1.get() == "":
            e_1.insert(0, n39[4])
            lbl39.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n39[4])
            lbl39.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n39[4])
            lbl39.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n39[4])
            lbl39.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n39[4])
            lbl39.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n39[4])
            lbl39.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num40():
        n40 = lbl40.config("text")
        if e_1.get() == "":
            e_1.insert(0, n40[4])
            lbl40.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n40[4])
            lbl40.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n40[4])
            lbl40.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n40[4])
            lbl40.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n40[4])
            lbl40.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n40[4])
            lbl40.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num41():
        n41 = lbl41.config("text")
        if e_1.get() == "":
            e_1.insert(0, n41[4])
            lbl41.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n41[4])
            lbl41.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n41[4])
            lbl41.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n41[4])
            lbl41.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n41[4])
            lbl41.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n41[4])
            lbl41.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num42():
        n42 = lbl42.config("text")
        if e_1.get() == "":
            e_1.insert(0, n42[4])
            lbl42.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n42[4])
            lbl42.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n42[4])
            lbl42.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n42[4])
            lbl42.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n42[4])
            lbl42.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n42[4])
            lbl42.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num43():
        n43 = lbl43.config("text")
        if e_1.get() == "":
            e_1.insert(0, n43[4])
            lbl43.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n43[4])
            lbl43.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n43[4])
            lbl43.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n43[4])
            lbl43.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n43[4])
            lbl43.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n43[4])
            lbl43.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num44():
        n44 = lbl44.config("text")
        if e_1.get() == "":
            e_1.insert(0, n44[4])
            lbl44.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n44[4])
            lbl44.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n44[4])
            lbl44.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n44[4])
            lbl44.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n44[4])
            lbl44.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n44[4])
            lbl44.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num45():
        n45 = lbl45.config("text")
        if e_1.get() == "":
            e_1.insert(0, n45[4])
            lbl45.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n45[4])
            lbl45.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n45[4])
            lbl45.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n45[4])
            lbl45.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n45[4])
            lbl45.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n45[4])
            lbl45.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num46():
        n46 = lbl46.config("text")
        if e_1.get() == "":
            e_1.insert(0, n46[4])
            lbl46.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n46[4])
            lbl46.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n46[4])
            lbl46.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n46[4])
            lbl46.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n46[4])
            lbl46.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n46[4])
            lbl46.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num47():
        n47 = lbl47.config("text")
        if e_1.get() == "":
            e_1.insert(0, n47[4])
            lbl47.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n47[4])
            lbl47.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n47[4])
            lbl47.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n47[4])
            lbl47.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n47[4])
            lbl47.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n47[4])
            lbl47.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num48():
        n48 = lbl48.config("text")
        if e_1.get() == "":
            e_1.insert(0, n48[4])
            lbl48.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n48[4])
            lbl48.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n48[4])
            lbl48.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n48[4])
            lbl48.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n48[4])
            lbl48.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n48[4])
            lbl48.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    def num49():
        n49 = lbl49.config("text")
        if e_1.get() == "":
            e_1.insert(0, n49[4])
            lbl49.config(state="disabled")
        elif e_2.get() == "":
            e_2.insert(0, n49[4])
            lbl49.config(state="disabled")
        elif e_3.get() == "":
            e_3.insert(0, n49[4])
            lbl49.config(state="disabled")
        elif e_4.get() == "":
            e_4.insert(0, n49[4])
            lbl49.config(state="disabled")
        elif e_5.get() == "":
            e_5.insert(0, n49[4])
            lbl49.config(state="disabled")
        elif e_6.get() == "":
            e_6.insert(0, n49[4])
            lbl49.config(state="disabled")
        else:
            messagebox.showinfo("Enough Entries Filled", "All Entries are full")

    # functions
    # function to append numbers chosen to text file so can be reached in the next screen
    # also still holding the current user variable to assign the chosen 6 numbers to this user based on their id number
    def submit():
        submit_now = messagebox.askquestion("Submit Now?", "Are you sure about your number?")
        if submit_now == "yes":
            player_lotto_list = [e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get()]
            # open file in append mode
            lotto_nums = open("./player_lotto.txt", "a+")
            # formatting the date to only show the date in dd/mm/yy
            date = datetime.now()
            today = "%d/%m/%y"
            lotto_nums.write("\n" + str(date.strftime(today)) + "|" + str(current_user) + "|" + str(
                ",".join(player_lotto_list)))  # read from the file

            lotto_nums.close()
            window.destroy()
            create_lotto_screen(current_user)
        # if user clicks no then clear all entries and enable buttons that were disabled after clicking
        else:
            e_1.delete(0, END)
            e_2.delete(0, END)
            e_3.delete(0, END)
            e_4.delete(0, END)
            e_5.delete(0, END)
            e_6.delete(0, END)
            lbl1.config(state="normal")
            lbl2.config(state="normal")
            lbl3.config(state="normal")
            lbl4.config(state="normal")
            lbl5.config(state="normal")
            lbl6.config(state="normal")
            lbl7.config(state="normal")
            lbl8.config(state="normal")
            lbl9.config(state="normal")
            lbl10.config(state="normal")
            lbl11.config(state="normal")
            lbl12.config(state="normal")
            lbl13.config(state="normal")
            lbl14.config(state="normal")
            lbl15.config(state="normal")
            lbl16.config(state="normal")
            lbl17.config(state="normal")
            lbl18.config(state="normal")
            lbl19.config(state="normal")
            lbl20.config(state="normal")
            lbl21.config(state="normal")
            lbl22.config(state="normal")
            lbl23.config(state="normal")
            lbl24.config(state="normal")
            lbl25.config(state="normal")
            lbl26.config(state="normal")
            lbl27.config(state="normal")
            lbl28.config(state="normal")
            lbl29.config(state="normal")
            lbl30.config(state="normal")
            lbl31.config(state="normal")
            lbl32.config(state="normal")
            lbl33.config(state="normal")
            lbl34.config(state="normal")
            lbl35.config(state="normal")
            lbl36.config(state="normal")
            lbl37.config(state="normal")
            lbl38.config(state="normal")
            lbl39.config(state="normal")
            lbl40.config(state="normal")
            lbl41.config(state="normal")
            lbl42.config(state="normal")
            lbl43.config(state="normal")
            lbl44.config(state="normal")
            lbl45.config(state="normal")
            lbl46.config(state="normal")
            lbl47.config(state="normal")
            lbl48.config(state="normal")
            lbl49.config(state="normal")
    # clear function to clear entries and enable disabled buttons that have been clicked
    def clear():
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)
        e_4.delete(0, END)
        e_5.delete(0, END)
        e_6.delete(0, END)
        lbl1.config(state="normal")
        lbl2.config(state="normal")
        lbl3.config(state="normal")
        lbl4.config(state="normal")
        lbl5.config(state="normal")
        lbl6.config(state="normal")
        lbl7.config(state="normal")
        lbl8.config(state="normal")
        lbl9.config(state="normal")
        lbl10.config(state="normal")
        lbl11.config(state="normal")
        lbl12.config(state="normal")
        lbl13.config(state="normal")
        lbl14.config(state="normal")
        lbl15.config(state="normal")
        lbl16.config(state="normal")
        lbl17.config(state="normal")
        lbl18.config(state="normal")
        lbl19.config(state="normal")
        lbl20.config(state="normal")
        lbl21.config(state="normal")
        lbl22.config(state="normal")
        lbl23.config(state="normal")
        lbl24.config(state="normal")
        lbl25.config(state="normal")
        lbl26.config(state="normal")
        lbl27.config(state="normal")
        lbl28.config(state="normal")
        lbl29.config(state="normal")
        lbl30.config(state="normal")
        lbl31.config(state="normal")
        lbl32.config(state="normal")
        lbl33.config(state="normal")
        lbl34.config(state="normal")
        lbl35.config(state="normal")
        lbl36.config(state="normal")
        lbl37.config(state="normal")
        lbl38.config(state="normal")
        lbl39.config(state="normal")
        lbl40.config(state="normal")
        lbl41.config(state="normal")
        lbl42.config(state="normal")
        lbl43.config(state="normal")
        lbl44.config(state="normal")
        lbl45.config(state="normal")
        lbl46.config(state="normal")
        lbl47.config(state="normal")
        lbl48.config(state="normal")
        lbl49.config(state="normal")
    # exit app function
    def exit_app():
        msg = messagebox.askquestion("Exit Application?", "Are you sure you want to Exit ?")
        if msg == "yes":
            window.destroy()
        else:
            pass

    # Buttons
    # functions as commands
    btn_clear = Button(window, text="Clear", font="Arial 25 bold", bg="white", fg="#a11d33", command=clear)
    btn_clear.place(x=600, y=600, width=140)
    btn_submit = Button(window, text="Submit", font="Arial 25 bold", bg="white", fg="#a11d33", command=submit)
    btn_submit.place(x=600, y=500)
    btn_exit = Button(window, text="Exit", font="Arial 25 bold", bg="white", fg="#a11d33", command=exit_app)
    btn_exit.place(x=600, y=700, width=140)

    # IMAGES FOR COLOURFUL BUTTONS (lines 1340 -1719)
    # To give the numbers a round effect images and labels are used
    # Images are used and stored in labels for a colourful style
    # Images are styled before buttons so that the buttons can appear on top of them to give it the effect of a ROUND BUTTON
    # RED DOTS
    test1 = PhotoImage(file="red.png")
    lbl_img1 = Label(window, text="1", fg="white", bg="white", border="0", image=test1)
    lbl_img1.image = test1
    lbl_img1.place(x=100, y=200, width=50, height=50)
    test2 = PhotoImage(file="red.png")
    lbl_img2 = Label(bg="white", border="0", image=test2)
    lbl_img2.image = test2
    lbl_img2.place(x=170, y=200, width=50, height=50)
    test3 = PhotoImage(file="red.png")
    lbl_img3 = Label(bg="white", border="0", image=test3)
    lbl_img3.image = test3
    lbl_img3.place(x=240, y=200, width=50, height=50)
    test4 = PhotoImage(file="red.png")
    lbl_img4 = Label(bg="white", border="0", image=test4)
    lbl_img4.image = test4
    lbl_img4.place(x=310, y=200, width=50, height=50)
    test5 = PhotoImage(file="red.png")
    lbl_img5 = Label(bg="white", border="0", image=test5)
    lbl_img5.image = test5
    lbl_img5.place(x=380, y=200, width=50, height=50)
    test6 = PhotoImage(file="red.png")
    lbl_img6 = Label(bg="white", border="0", image=test6)
    lbl_img6.image = test6
    lbl_img6.place(x=520, y=200, width=50, height=50)
    test7 = PhotoImage(file="red.png")
    lbl_img7 = Label(bg="white", border="0", image=test7)
    lbl_img7.image = test5
    lbl_img7.place(x=450, y=200, width=50, height=50)

    # NUMBERS
    # RED
    lbl1 = Button(window, highlightthickness=0, text="1", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num1)
    lbl1.place(x=110, y=210, width=30, height=30)
    lbl2 = Button(window, highlightthickness=0, text="2", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num2)
    lbl2.place(x=180, y=210, width=30, height=30)
    lbl3 = Button(window, highlightthickness=0, text="3", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num3)
    lbl3.place(x=250, y=210, width=30, height=30)
    lbl4 = Button(window, highlightthickness=0, text="4", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num4)
    lbl4.place(x=320, y=210, width=30, height=30)
    lbl5 = Button(window, highlightthickness=0, text="5", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num5)
    lbl5.place(x=390, y=210, width=30, height=30)
    lbl6 = Button(window, highlightthickness=0, text="6", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num6)
    lbl6.place(x=460, y=210, width=30, height=30)
    lbl7 = Button(window, highlightthickness=0, text="7", fg="white", bd="0", font="Arial 17 bold", bg="#e84404",
                  command=num7)
    lbl7.place(x=530, y=210, width=30, height=30)

    # BLUE DOTS
    test8 = PhotoImage(file="blue.png")
    lbl_img8 = Label(bg="white", border="0", image=test8)
    lbl_img8.image = test8
    lbl_img8.place(x=100, y=270, width=50, height=50)
    test9 = PhotoImage(file="blue.png")
    lbl_img9 = Label(bg="white", border="0", image=test9)
    lbl_img9.image = test9
    lbl_img9.place(x=170, y=270, width=50, height=50)
    test10 = PhotoImage(file="blue.png")
    lbl_img10 = Label(bg="white", border="0", image=test10)
    lbl_img10.image = test10
    lbl_img10.place(x=240, y=270, width=50, height=50)
    test11 = PhotoImage(file="blue.png")
    lbl_img11 = Label(bg="white", border="0", image=test11)
    lbl_img11.image = test11
    lbl_img11.place(x=310, y=270, width=50, height=50)
    test12 = PhotoImage(file="blue.png")
    lbl_img12 = Label(bg="white", border="0", image=test12)
    lbl_img12.image = test12
    lbl_img12.place(x=380, y=270, width=50, height=50)
    test13 = PhotoImage(file="blue.png")
    lbl_img13 = Label(bg="white", border="0", image=test13)
    lbl_img13.image = test13
    lbl_img13.place(x=450, y=270, width=50, height=50)
    test14 = PhotoImage(file="blue.png")
    lbl_img14 = Label(bg="white", border="0", image=test14)
    lbl_img14.image = test14
    lbl_img14.place(x=520, y=270, width=50, height=50)

    # NUMBERS
    # BLUE
    lbl8 = Button(window, highlightthickness=0, text="8", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                  command=num8)
    lbl8.place(x=110, y=280, width=30, height=30)
    lbl9 = Button(window, highlightthickness=0, text="9", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                  command=num9)
    lbl9.place(x=180, y=280, width=30, height=30)
    lbl10 = Button(window, highlightthickness=0, text="10", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                   command=num10)
    lbl10.place(x=250, y=280, width=30, height=30)
    lbl11 = Button(window, highlightthickness=0, text="11", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                   command=num11)
    lbl11.place(x=320, y=280, width=30, height=30)
    lbl12 = Button(window, highlightthickness=0, text="12", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                   command=num12)
    lbl12.place(x=390, y=280, width=30, height=30)
    lbl13 = Button(window, highlightthickness=0, text="13", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                   command=num13)
    lbl13.place(x=460, y=280, width=30, height=30)
    lbl14 = Button(window, highlightthickness=0, text="14", fg="black", bd="0", font="Arial 17 bold", bg="#48c4fc",
                   command=num14)
    lbl14.place(x=530, y=280, width=30, height=30)

    # GREEN DOTS
    test15 = PhotoImage(file="green.png")
    lbl_img15 = Label(bg="white", border="0", image=test15)
    lbl_img15.image = test15
    lbl_img15.place(x=100, y=340, width=50, height=50)
    test16 = PhotoImage(file="green.png")
    lbl_img16 = Label(bg="white", border="0", image=test16)
    lbl_img16.image = test16
    lbl_img16.place(x=170, y=340, width=50, height=50)
    test17 = PhotoImage(file="green.png")
    lbl_img17 = Label(bg="white", border="0", image=test17)
    lbl_img17.image = test17
    lbl_img17.place(x=240, y=340, width=50, height=50)
    test18 = PhotoImage(file="green.png")
    lbl_img18 = Label(bg="white", border="0", image=test18)
    lbl_img18.image = test18
    lbl_img18.place(x=310, y=340, width=50, height=50)
    test19 = PhotoImage(file="green.png")
    lbl_img19 = Label(bg="white", border="0", image=test19)
    lbl_img19.image = test19
    lbl_img19.place(x=380, y=340, width=50, height=50)
    test20 = PhotoImage(file="green.png")
    lbl_img20 = Label(bg="white", border="0", image=test20)
    lbl_img20.image = test20
    lbl_img20.place(x=450, y=340, width=50, height=50)
    test21 = PhotoImage(file="green.png")
    lbl_img21 = Label(bg="white", border="0", image=test21)
    lbl_img21.image = test21
    lbl_img21.place(x=520, y=340, width=50, height=50)

    # NUMBERS
    # GREEN
    lbl15 = Button(window, highlightthickness=0, text="15", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num15)
    lbl15.place(x=110, y=350, width=30, height=30)
    lbl16 = Button(window, highlightthickness=0, text="16", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num16)
    lbl16.place(x=180, y=350, width=30, height=30)
    lbl17 = Button(window, highlightthickness=0, text="17", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num17)
    lbl17.place(x=250, y=350, width=30, height=30)
    lbl18 = Button(window, highlightthickness=0, text="18", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num18)
    lbl18.place(x=320, y=350, width=30, height=30)
    lbl19 = Button(window, highlightthickness=0, text="19", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num19)
    lbl19.place(x=390, y=350, width=30, height=30)
    lbl20 = Button(window, highlightthickness=0, text="20", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num20)
    lbl20.place(x=460, y=350, width=30, height=30)
    lbl21 = Button(window, highlightthickness=0, text="21", fg="black", bd="0", font="Arial 17 bold", bg="#a8d484",
                   command=num21)
    lbl21.place(x=530, y=350, width=30, height=30)

    # ORANGE DOTS
    test22 = PhotoImage(file="orange.png")
    lbl_img22 = Label(bg="white", border="0", image=test22)
    lbl_img22.image = test22
    lbl_img22.place(x=100, y=410, width=50, height=50)
    test23 = PhotoImage(file="orange.png")
    lbl_img23 = Label(bg="white", border="0", image=test23)
    lbl_img23.image = test23
    lbl_img23.place(x=170, y=410, width=50, height=50)
    test24 = PhotoImage(file="orange.png")
    lbl_img24 = Label(bg="white", border="0", image=test24)
    lbl_img24.image = test24
    lbl_img24.place(x=240, y=410, width=50, height=50)
    test25 = PhotoImage(file="orange.png")
    lbl_img25 = Label(bg="white", border="0", image=test25)
    lbl_img25.image = test25
    lbl_img25.place(x=310, y=410, width=50, height=50)
    test26 = PhotoImage(file="orange.png")
    lbl_img26 = Label(bg="white", border="0", image=test26)
    lbl_img26.image = test26
    lbl_img26.place(x=380, y=410, width=50, height=50)
    test27 = PhotoImage(file="orange.png")
    lbl_img27 = Label(bg="white", border="0", image=test27)
    lbl_img27.image = test27
    lbl_img27.place(x=450, y=410, width=50, height=50)
    test28 = PhotoImage(file="orange.png")
    lbl_img28 = Label(bg="white", border="0", image=test28)
    lbl_img28.image = test28
    lbl_img28.place(x=520, y=410, width=50, height=50)

    # NUMBERS
    # ORANGE
    lbl22 = Button(window, highlightthickness=0, text="22", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num22)
    lbl22.place(x=110, y=420, width=30, height=30)
    lbl23 = Button(window, highlightthickness=0, text="23", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num23)
    lbl23.place(x=180, y=420, width=30, height=30)
    lbl24 = Button(window, highlightthickness=0, text="24", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num24)
    lbl24.place(x=250, y=420, width=30, height=30)
    lbl25 = Button(window, highlightthickness=0, text="25", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num25)
    lbl25.place(x=320, y=420, width=30, height=30)
    lbl26 = Button(window, highlightthickness=0, text="26", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num26)
    lbl26.place(x=390, y=420, width=30, height=30)
    lbl27 = Button(window, highlightthickness=0, text="27", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num27)
    lbl27.place(x=460, y=420, width=30, height=30)
    lbl28 = Button(window, highlightthickness=0, text="28", fg="black", bd="0", font="Arial 17 bold", bg="#ffa404",
                   command=num28)
    lbl28.place(x=530, y=420, width=30, height=30)

    # PINK DOTS
    test29 = PhotoImage(file="pink.png")
    lbl_img29 = Label(bg="white", border="0", image=test29)
    lbl_img29.image = test29
    lbl_img29.place(x=100, y=480, width=50, height=50)
    test30 = PhotoImage(file="pink.png")
    lbl_img30 = Label(bg="white", border="0", image=test30)
    lbl_img30.image = test30
    lbl_img30.place(x=170, y=480, width=50, height=50)
    test31 = PhotoImage(file="pink.png")
    lbl_img31 = Label(bg="white", border="0", image=test31)
    lbl_img31.image = test31
    lbl_img31.place(x=240, y=480, width=50, height=50)
    test32 = PhotoImage(file="pink.png")
    lbl_img32 = Label(bg="white", border="0", image=test32)
    lbl_img32.image = test32
    lbl_img32.place(x=310, y=480, width=50, height=50)
    test33 = PhotoImage(file="pink.png")
    lbl_img33 = Label(bg="white", border="0", image=test33)
    lbl_img33.image = test33
    lbl_img33.place(x=380, y=480, width=50, height=50)
    test34 = PhotoImage(file="pink.png")
    lbl_img34 = Label(bg="white", border="0", image=test34)
    lbl_img34.image = test34
    lbl_img34.place(x=450, y=480, width=50, height=50)
    test35 = PhotoImage(file="pink.png")
    lbl_img35 = Label(bg="white", border="0", image=test35)
    lbl_img35.image = test35
    lbl_img35.place(x=520, y=480, width=50, height=50)

    # NUMBERS
    # PINK
    lbl29 = Button(window, highlightthickness=0, text="29", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num29)
    lbl29.place(x=110, y=490, width=30, height=30)
    lbl30 = Button(window, highlightthickness=0, text="30", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num30)
    lbl30.place(x=180, y=490, width=30, height=30)
    lbl31 = Button(window, highlightthickness=0, text="31", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num31)
    lbl31.place(x=250, y=490, width=30, height=30)
    lbl32 = Button(window, highlightthickness=0, text="32", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num32)
    lbl32.place(x=320, y=490, width=30, height=30)
    lbl33 = Button(window, highlightthickness=0, text="33", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num33)
    lbl33.place(x=390, y=490, width=30, height=30)
    lbl34 = Button(window, highlightthickness=0, text="34", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num34)
    lbl34.place(x=460, y=490, width=30, height=30)
    lbl35 = Button(window, highlightthickness=0, text="35", fg="black", bd="0", font="Arial 17 bold", bg="#e8248c",
                   command=num35)
    lbl35.place(x=530, y=490, width=30, height=30)

    # PURPLE DOTS
    test36 = PhotoImage(file="purple.png")
    lbl_img36 = Label(bg="white", border="0", image=test36)
    lbl_img36.image = test36
    lbl_img36.place(x=100, y=550, width=50, height=50)
    test37 = PhotoImage(file="purple.png")
    lbl_img37 = Label(bg="white", border="0", image=test37)
    lbl_img37.image = test37
    lbl_img37.place(x=170, y=550, width=50, height=50)
    test38 = PhotoImage(file="purple.png")
    lbl_img38 = Label(bg="white", border="0", image=test38)
    lbl_img38.image = test38
    lbl_img38.place(x=240, y=550, width=50, height=50)
    test39 = PhotoImage(file="purple.png")
    lbl_img39 = Label(bg="white", border="0", image=test39)
    lbl_img39.image = test39
    lbl_img39.place(x=310, y=550, width=50, height=50)
    test40 = PhotoImage(file="purple.png")
    lbl_img40 = Label(bg="white", border="0", image=test40)
    lbl_img40.image = test40
    lbl_img40.place(x=380, y=550, width=50, height=50)
    test41 = PhotoImage(file="purple.png")
    lbl_img41 = Label(bg="white", border="0", image=test41)
    lbl_img41.image = test41
    lbl_img41.place(x=450, y=550, width=50, height=50)
    test42 = PhotoImage(file="purple.png")
    lbl_img42 = Label(bg="white", border="0", image=test42)
    lbl_img42.image = test42
    lbl_img42.place(x=520, y=550, width=50, height=50)

    # NUMBERS
    # PURPLE
    lbl36 = Button(window, highlightthickness=0, text="36", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num36)
    lbl36.place(x=110, y=560, width=30, height=30)
    lbl37 = Button(window, highlightthickness=0, text="37", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num37)
    lbl37.place(x=180, y=560, width=30, height=30)
    lbl38 = Button(window, highlightthickness=0, text="38", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num38)
    lbl38.place(x=250, y=560, width=30, height=30)
    lbl39 = Button(window, highlightthickness=0, text="39", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num39)
    lbl39.place(x=320, y=560, width=30, height=30)
    lbl40 = Button(window, highlightthickness=0, text="40", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num40)
    lbl40.place(x=390, y=560, width=30, height=30)
    lbl41 = Button(window, highlightthickness=0, text="41", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num41)
    lbl41.place(x=460, y=560, width=30, height=30)
    lbl42 = Button(window, highlightthickness=0, text="42", fg="black", bd="0", font="Arial 17 bold", bg="#446ce8",
                   command=num42)
    lbl42.place(x=530, y=560, width=30, height=30)

    # ANOTHER SET OF RED DOTS
    test43 = PhotoImage(file="red.png")
    lbl_img43 = Label(bg="white", border="0", image=test43)
    lbl_img43.image = test43
    lbl_img43.place(x=100, y=620, width=50, height=50)
    test44 = PhotoImage(file="red.png")
    lbl_img44 = Label(bg="white", border="0", image=test44)
    lbl_img44.image = test44
    lbl_img44.place(x=170, y=620, width=50, height=50)
    test45 = PhotoImage(file="red.png")
    lbl_img45 = Label(bg="white", border="0", image=test45)
    lbl_img45.image = test45
    lbl_img45.place(x=240, y=620, width=50, height=50)
    test46 = PhotoImage(file="red.png")
    lbl_img46 = Label(bg="white", border="0", image=test46)
    lbl_img46.image = test46
    lbl_img46.place(x=310, y=620, width=50, height=50)
    test47 = PhotoImage(file="red.png")
    lbl_img47 = Label(bg="white", border="0", image=test47)
    lbl_img47.image = test47
    lbl_img47.place(x=380, y=620, width=50, height=50)
    test48 = PhotoImage(file="red.png")
    lbl_img48 = Label(bg="white", border="0", image=test48)
    lbl_img48.image = test48
    lbl_img48.place(x=450, y=620, width=50, height=50)
    test49 = PhotoImage(file="red.png")
    lbl_img49 = Label(bg="white", border="0", image=test49)
    lbl_img49.image = test49
    lbl_img49.place(x=520, y=620, width=50, height=50)

    # NUMBERS
    # RED AGAIN
    lbl43 = Button(window, highlightthickness=0, text="43", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num43)
    lbl43.place(x=110, y=630, width=30, height=30)
    lbl44 = Button(window, highlightthickness=0, text="44", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num44)
    lbl44.place(x=180, y=630, width=30, height=30)
    lbl45 = Button(window, highlightthickness=0, text="45", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num45)
    lbl45.place(x=250, y=630, width=30, height=30)
    lbl46 = Button(window, highlightthickness=0, text="46", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num46)
    lbl46.place(x=320, y=630, width=30, height=30)
    lbl47 = Button(window, highlightthickness=0, text="47", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num47)
    lbl47.place(x=390, y=630, width=30, height=30)
    lbl48 = Button(window, highlightthickness=0, text="48", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num48)
    lbl48.place(x=460, y=630, width=30, height=30)
    lbl49 = Button(window, highlightthickness=0, text="49", fg="black", bd="0", font="Arial 17 bold", bg="#e84404",
                   command=num49)
    lbl49.place(x=530, y=630, width=30, height=30)

    window.mainloop()


if __name__ == '__main__':
    draw_lotto_screen("")
