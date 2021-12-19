import tkinter
import math
from tkinter import *
from tkinter import messagebox
def determine():
    if cur_value.get() != '' or res_value.get() != '' or pow_value.get() != '':
        if isinstance(int(cur_value.get()),int) and isinstance(int(res_value.get()),int) and isinstance(int(pow_value.get()),int):
            pow_sq = int(pow_value.get()) / int(res_value.get())
            cur = round(math.sqrt(pow_sq))
            if int(cur_value.get()) > cur:
                #Fuse rating okay
                val = Label(app,text="Fuse is usable", font=("italic",16),foreground="orange",padx=0,pady=15)
                val.grid(row=11,column=2,sticky=W)
            else:
                strcur = str(cur)
                val = Label(app,text="Fuse is not usable, Use "+ strcur +" Amps or above", font=("italic",16),foreground="orange",padx=0,pady=15)
                val.grid(row=11,column=2,sticky=W)
                cur_input.delete(0,END)
                pow_input.delete(0,END)
                res_input.delete(0,END)            

        else:
            messagebox.showerror("Invalid values","Values must be numbers")
                 
    else:
        messagebox.showerror("Missing values","Fill in all fields")
    

app = Tk()
app.geometry("800x400")
app.title("Fuse Viability")
app.resizable(False,False)
intro = Label(app, text="Feasibility Analysis", font=("bold",14),foreground="#000",padx=10,pady=5)
intro.grid(row=1,column=1,sticky=W)

cur_value = StringVar()
cur = Label(app, text="Fuse Rating (A)", font=("bold",12),foreground="red", padx=5,pady=2)
cur.grid(row=2,column=1,sticky=W)
cur_input = Entry(app,textvariable=cur_value,border=1,width=35,background="#083a56",borderwidth=0)
cur_input.grid(row=3,column=3,sticky=W)
cur_input.place(x=138,y=40,height=30)

res_value = StringVar()
res = Label(app, text="Resistance (Ω)", font=("bold",12),foreground="red", padx=5,pady=2)
res.grid(row=3,column=1,sticky=W,pady=10)
res_input = Entry(app,textvariable=res_value,border=1,width=35,background="#083a56",borderwidth=0)
res_input.grid(row=5,column=3,sticky=W)
res_input.place(x=138,y=74,height=30)

pow_value = StringVar()
pow = Label(app, text="Power rating (W)", font=("bold",12),foreground="red", padx=5,pady=2)
pow.grid(row=4,column=1,sticky=W,pady=10)
pow_input = Entry(app,textvariable=pow_value,border=1,width=35,background="#083a56",borderwidth=0)
pow_input.grid(row=7,column=3,sticky=W)
pow_input.place(x=138,y=120,height=30)

button = Button(app,text="  Determine Feasibility",width=17,command=determine,background="#09e058",activebackground="#09e058",border=0,height=2)
button.grid(row=9,column=2,sticky=W)

app.mainloop()