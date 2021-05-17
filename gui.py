from tkinter import *
import time
import datetime
from random import choice
# creating root object
root = Tk()
# defining size of window
root.geometry("1200x6000")
root.config(bg='orange')
photo = PhotoImage(file="BIT-Mesra.png")
label = Label(root, image=photo).pack(fill=X)
user = StringVar()
bot = StringVar()
# setting up the title of window
root.title("BIT CHATBOT")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700,
           relief=SUNKEN)
f1.pack(side=LEFT)

#TIME

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="BIT CHATBOT",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Blue",
                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)


# exit function
def qExit():
    root.destroy()
# Function to reset the window
def Reset():
    user.set("")
    bot.set("")


# reference
lblReference = Label(f1, font=('arial', 16, 'bold'),
                     text="you", bd=16, anchor="w")

lblReference.grid(row=0, column=0)

txtReference = Entry(f1, font=('arial', 16, 'bold'),
                     textvariable=user, bd=10, insertwidth=4,
                     bg="pink", justify=RIGHT)

txtReference.grid(row=0, column=1)

# labels
lblMsg = Label(f1, font=('arial', 16, 'bold'),
               text="bot", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=bot, bd=10, insertwidth=4,
               bg="pink", justify='right')

txtMsg.grid(row=1, column=1)



error = ["sorry, i don't know what u said?"]
bot_talk = {'hi': ['hello'], 'hello': ['hey'], 'faculty': ['PHD qualified'], 'courses offer': ['ug/pg/phd'], 'college ranking': ['among top 50'], 'hostel facilities': ['No'], 'canteen':['yes'],
            'placement scope': ['yes if you are capable'], 'admission criteria': ['merit base'], 'classes held': ['regular'], 'seat': ['60 for each courses'], 'library': ['yes, time 10-5'],
            'bca fees': ['approx 3.5L']}


def main():
    question = user.get()
    if question in bot_talk:
        bot.set(choice(bot_talk[question]))
    else:
        bot.set(choice(error))

    # Show message button


btnSend = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Send", bg="maroon",
                  command=main).grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="purple",
                  command=Reset).grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="yellow",
                 command=qExit).grid(row=7, column=3)

# keeps window alive
root.mainloop()
