import tkinter as tk
from tkinter import ttk
import pyautogui as gui
import time
import pymsgbox as pmb

class App():
    def __init__(self):
        self.msmsg = ""
        self.msnumb = ""
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("Message Sender")
        self.root.wm_iconbitmap("C:/Users/alsha/OneDrive/Documents/Projects/Message Sender/msgsndr.ico")
        self.mainframe = tk.Frame(self.root, background="#2f2f35")
        self.mainframe.pack(fill="both", expand=True)
        self.logo = tk.PhotoImage(file="C:/Users/alsha/OneDrive/Documents/Projects/Message Sender/mrz.png")
        self.lgo = tk.Label(self.mainframe, image=self.logo, background="#2f2f35")
        self.lgo.grid(row=0, column=1)
        self.messagesendertext = tk.Label(self.mainframe, text="Msg Info", font=("Brass Mono", 24), background="#2f2f35")
        self.messagesendertext.grid(row=0, column=0, padx=10, pady=10)
        self.messagesendertext.config(foreground="white")
        self.set_message_field = ttk.Entry(self.mainframe, background="#35352f")
        self.set_message_field.grid(row=1, column=0, pady=5, padx=6, sticky="Nwes")
        self.set_message = tk.Button(self.mainframe, text="Set Message", command=self.message, bg="#32a8bd")
        self.set_message.grid(row=1, column=1, pady=5, sticky="Nwes")
        self.set_numb_field = ttk.Entry(self.mainframe, background="#35352f")
        self.set_numb_field.grid(row=2, column=0, pady=3, padx=6, sticky="Nwes")
        self.set_numb = tk.Button(self.mainframe, text="Set Numb of msgs", command=self.numb, bg="#32a8bd")
        self.set_numb.grid(row=2, column=1, pady=3)
        self.send = tk.Button(self.mainframe, text="Send", bg="#32a8bd", command=self.Sending)
        self.send.grid(row=3, column=1, pady=3, sticky="Nwes")
        self.send.config()
        self.root.mainloop()
        return
    def message(self):
        self.msg = self.set_message_field.get()
        self.msmsg = self.msg
    def numb(self):
        numb = self.set_numb_field.get()
        self.msnumb = numb
    def Sending(self):
        pmb.alert(text="Please wait 5 seconds for you message to send after you close this pop up.", title="Message Sender")

        time.sleep(5)

        for i in range(int(self.msnumb)):
            gui.typewrite(self.msmsg)
            gui.press('Enter')




if __name__ == "__main__":
    App()

