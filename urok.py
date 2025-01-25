import tkinter as tk

app = tk.Tk()
app.geometry("240x270")
app['bg']='blue'
app.title('sigma')

def add_button(digit):
    return tk.Button(app, text= digit, bd='5',font=('Arial', 15), command=lambda: add_digit(digit))

def add_operation(operation):
    return tk.Button(app, text= operation, bd='5',font=('Arial', 15), fg=('red'), bg='green', activebackground='red', command=lambda: make_operation(operation))

def calculate():
    value = pole.get()
    pole.delete(0, 'end')
    pole.insert(0, eval(value))


def add_digit(digit):
    value = pole.get() 
    if value[0] == '0':
        value = value[1:]
    pole.delete(0, 'end')
    pole.insert(0, value+digit)

def make_operation(operation):
    value = pole.get() 
    if  value and value[-1] in '+-/*':
        value = value[:-1]
    pole.delete(0, 'end')
    pole.insert(0, value+operation)

def make_calc_button(operation):
    return tk.Button(app, text= operation, bd='5',font=('Arial', 15), fg=('red'), bg='green', activebackground='red', command=calculate)


add_button('1').grid(row=1,  column=0, stick='wens', padx=5, pady=5)
add_button('2').grid(row=1,  column=1, stick='wens', padx=5, pady=5)
add_button('3').grid(row=1,  column=2, stick='wens', padx=5, pady=5)
add_button('4').grid(row=2,  column=0, stick='wens', padx=5, pady=5)
add_button('5').grid(row=2,  column=1, stick='wens', padx=5, pady=5)
add_button('6').grid(row=2,  column=2, stick='wens', padx=5, pady=5)
add_button('7').grid(row=3,  column=0, stick='wens', padx=5, pady=5)
add_button('8').grid(row=3,  column=1, stick='wens', padx=5, pady=5)
add_button('9').grid(row=3,  column=2, stick='wens', padx=5, pady=5)
addbutton0= tk.Button(app, text= 0, bd='5',font=('Arial', 15), command=lambda: add_digit(0)).grid(row=4,  column=0, stick='we', padx=5, pady=5, columnspan=2)
pole = tk.Entry(app, font=('Arial', 15), width=15, bd=3)
pole.insert(0, '0')
pole.grid(row=0,column=0, columnspan=4, stick = 'we', padx=5,)

add_operation('+').grid(row=1,  column=3, stick='wens', padx=5, pady=5)
add_operation('-').grid(row=2,  column=3, stick='wens', padx=5, pady=5)
add_operation('/').grid(row=3,  column=3, stick='wens', padx=5, pady=5)
add_operation('*').grid(row=4,  column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4,  column=2, stick='wens', padx=5, pady=5)

app.columnconfigure(0, minsize=60)
app.columnconfigure(1, minsize=60)
app.columnconfigure(2, minsize=60)
app.columnconfigure(3, minsize=60)


app.rowconfigure(1, minsize=60)
app.rowconfigure(2, minsize=60)
app.rowconfigure(3, minsize=60)


app.mainloop()