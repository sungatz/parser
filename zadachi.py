

import tkinter as tk

counter = 1

def disabler():
    button1.config(state=tk.DISABLED)
def enabler():
    button1.config(state=tk.NORMAL)
def count():
    global counter
    counter+=1
    button2.config(text=f'{counter}')
    if counter%2 == 0:
        disabler()
    else: 
        enabler()



app = tk.Tk()
app.minsize(400, 400)

app.maxsize(600, 200)

button1 = tk.Button(app, text="text",
                        state=tk.NORMAL)

button2 = tk.Button(app, text=f"{counter}",
                    command=count)



button1.pack()
button2.pack()

app.geometry("400x400")

app.title("sigma")

app.mainloop()
