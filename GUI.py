from Tkinter import *


class Application(Frame):
    def __init__(self, master):

        Frame.__init__(self, master)

        self.grid()

        self.score = 0

        self.res = 0

        self.create_widgets()

    def create_widgets(self):

        self.label = Label(self, text="   Stock Market Prediction ")

        self.label.grid(row=0, column=0, sticky=W)

        self.que1()

        self.que2()



    def que1(self):

        self.label1 = Label(self, text="Select a company")

        self.label1.grid(row=1, column=0, columnspan=2, sticky=W)

        self.op11 = BooleanVar()

        Checkbutton(self, text="LTITL", variable=self.op11).grid(row=2, column=0, sticky=W)

        self.op21 = BooleanVar()

        Checkbutton(self, text="TCS", variable=self.op21).grid(row=3, column=0, sticky=W)

        self.op31 = BooleanVar()

        Checkbutton(self, text="SBI", variable=self.op31).grid(row=4, column=0, sticky=W)

        self.op41 = BooleanVar()

        Checkbutton(self, text="ONGC", variable=self.op41).grid(row=5, column=0, sticky=W)

        self.op51 = BooleanVar()

        Checkbutton(self, text="BHEL", variable=self.op41).grid(row=5, column=0, sticky=W)

        self.button1 = Button(self, text="Submit")

        self.button1["command"] = self.result_que1

        self.button1.grid()

        # output text box

        self.text1 = Text(self, width=35, height=1, wrap=WORD)

        self.text1.grid(row=7, column=0, columnspan=3)

    def result_que1(self):

        res1 = ""

        if self.op11.get():

            res1 = "Company Selected is LTITL"

        elif self.op21.get():

            res1 = "Company Selected is TCS"

        elif self.op31.get():

            res1 = "Company Selected is SBI"

        elif self.op51.get():

            res1 = "Company Selected is ONGC"

        elif self.op41.get():

            res1 = "Company Selected is BHEL"

        self.text1.delete(0.0, END)

        self.text1.insert(0.0, res1)


    def que2(self):

        self.label2 = Label(self, text="Select a time period ?")

        self.label2.grid(row=8, column=0, columnspan=2, sticky=W)

        self.op12 = BooleanVar()

        Checkbutton(self, text="Jan'15-Dec'15", variable=self.op12).grid(row=9, column=0, sticky=W)

        self.op22 = BooleanVar()

        Checkbutton(self, text="Jan'16-Dec'16", variable=self.op22).grid(row=10, column=0, sticky=W)

        self.button2 = Button(self, text="Submit")

        self.button2["command"] = self.result_que2

        self.button2.grid()

        # output text box

        self.text2 = Text(self, width=35, height=1, wrap=WORD)

        self.text2.grid(row=14, column=0, columnspan=3)

    def result_que2(self):

        res2 = ""

        if self.op12.get():

            res2 = "Time period selected is 2015"

        elif self.op22.get():

            res2 = "Time period selected is 2016"

        self.text2.delete(0.0, END)

        self.text2.insert(0.0, res2)




# create window

root = Tk()

# modify the window

root.title("GUI Task")

root.geometry("400x400")

app = Application(root)

root.mainloop()