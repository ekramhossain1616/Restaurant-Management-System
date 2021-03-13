import tkinter as tk
import datetime
from tkinter import messagebox


date1 = datetime.date.today()


win = tk.Tk()
win.title('Restaurant Management System')
win.geometry('850x700+300+5')
win.resizable(0,0)

# ------------------ food functions ------------------


def count_price():
    biriyani_number = biriyani_entry.get()
    kacchi_number= kacchi_entry.get()
    burger_number = burger_entry.get()
    coffee_number = coffee_entry.get()
    cold_coffee_number = cold_coffee_entry.get()
    tea_number = tea_entry.get()
    mineral_water_number = mineral_water_entry.get()

    try:
        price_number = (int(biriyani_number)*230)+(int(kacchi_number)*260)+(int(burger_number)*190)+(int(coffee_number)*60)+(int(cold_coffee_number)*130)+(int(tea_number)*20)+(int(mineral_water_number)*15)
        price_entry.delete(0,'end')
        price_entry.insert(0, (str(price_number)+' '+'TAKA'))
        vat_entry.delete(0,'end')
        vat_entry.insert(0,'00 TAKA')
        discount_entry.delete(0,'end')
        discount_entry.insert(0,'00 TAKA')
        total_price_entry.delete(0,'end')
        total_price_entry.insert(0,(str(price_number)+' '+ 'TAKA'))


    except:
        tk.messagebox.showerror('Error', 'Please enter valid numbers in all the fields.')


# -------------------- frames -----------------


top = tk.Frame(win,height=150 ,bg='light blue')
top.pack(fill=tk.BOTH)

bottom = tk.Frame(win, height=500, bg='white')
bottom.pack(fill=tk.BOTH, expand=True)

# ------------------ heading ------------------
heading = tk.Label(top, text='Jashim Tea Stall and Restaurant', bg='light blue', font='arial 17 bold')
heading.pack()

today_date = tk.Label(top, text=f'Date: {date1}', bg='light blue', font='arial 14 bold')
today_date.pack()

# ------------------ labels --------------------
biriyani_label = tk.Label(bottom, text='Biriyani: ', font='arial 14 bold', bg='white')
biriyani_label.place(x=30, y=20)

kacchi_label = tk.Label(bottom, text='Kacchi: ', font='arial 14 bold', bg='white')
kacchi_label.place(x=30, y=100)

burger_label = tk.Label(bottom, text='Burger: ', font='arial 14 bold', bg='white')
burger_label.place(x=30, y=180)

coffee_label = tk.Label(bottom, text='Coffee: ', font='arial 14 bold', bg='white')
coffee_label.place(x=30, y=260)

Cold_coffee_label = tk.Label(bottom, text='Cold Coffee: ', font='arial 14 bold', bg='white')
Cold_coffee_label.place(x=30, y=340)

Tea_label = tk.Label(bottom, text='Tea: ', font='arial 14 bold', bg='white')
Tea_label.place(x=30, y=420)

Mineral_Water_label = tk.Label(bottom, text='Mineral Water: ', font='arial 14 bold', bg='white')
Mineral_Water_label.place(x=30, y=500)

Price_label = tk.Label(bottom, text='Price: ', font='arial 14 bold', bg='white')
Price_label.place(x=380, y=20)

vat_label = tk.Label(bottom, text='VAT: ', font='arial 14 bold', bg='white')
vat_label.place(x=380, y=100)

discount_label = tk.Label(bottom, text='Discount: ', font='arial 14 bold', bg='white')
discount_label.place(x=380, y=180)

total_price_label = tk.Label(bottom, text='Total Price: ', font='arial 14 bold', bg='white')
total_price_label.place(x=380, y=260)


# --------------------- btn ---------------

btn = tk.Button(bottom, text='Count', font='arial 14 bold',bd=3, command=count_price)
btn.place(x= 130, y=580)

# ----------------------- entry boxes--------------------

biriyani_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
biriyani_entry.insert(0,'0')
biriyani_entry.place(x=180, y=20)

kacchi_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
kacchi_entry.insert(0,'0')
kacchi_entry.place(x=180, y=100)

burger_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
burger_entry.insert(0,'0')
burger_entry.place(x=180, y=180)

coffee_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
coffee_entry.insert(0,'0')
coffee_entry.place(x=180, y=260)

cold_coffee_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
cold_coffee_entry.insert(0,'0')
cold_coffee_entry.place(x=180, y=340)

tea_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
tea_entry.insert(0,'0')
tea_entry.place(x=180, y=420)

mineral_water_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
mineral_water_entry.insert(0,'0')
mineral_water_entry.place(x=180, y=500)

price_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
price_entry.insert(0,'00 TAKA')
price_entry.place(x=500, y=20)

vat_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
vat_entry.insert(0,'00 TAKA')
vat_entry.place(x=500, y=100)

discount_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
discount_entry.insert(0,'00 TAKA')
discount_entry.place(x=500, y=180)

total_price_entry = tk.Entry(bottom, width=25, bd=5, font='arial 8 bold')
total_price_entry.insert(0,'00 TAKA')
total_price_entry.place(x=500, y=260)

# --------------------- calc functions --------------------

def calc_numbers(x):
    # calc_entry.delete(0,'end')
    calc_entry_number = calc_entry.get()
    if calc_entry_number == '0' or calc_entry_number == 'Syntax Error':
        calc_entry.delete(0, 'end')
        calc_entry.insert('end' , str(x))
    else:
        calc_entry.insert('end', str(x))

def calc_operators(x):
    length = len(calc_entry.get())
    last_char = calc_entry.get()[-1]
    # last_char1 = calc_entry.get()[-2]
    # print(last_char)

    if length>=2:
        if last_char == '+' or last_char == '-' or last_char =='/' or last_char == '*':
            pass

        else:
            calc_entry.insert('end',str(x))
    else:
        calc_entry.insert('end', str(x))


def equal():
    try:
        calc_entry_number = calc_entry.get()
        calc_equal = eval(calc_entry_number)
        calc_entry.delete(0,'end')
        calc_entry.insert(0,calc_equal)
    except:
        calc_entry.delete(0,'end')
        calc_entry.insert(0,'Syntax Error')

def c_func():
    calc_entry.delete(0,'end')
    calc_entry.insert(0,'0')

def del_func():
    length = len(calc_entry.get())
    calc_entry_number = calc_entry.get()
    if calc_entry_number == '0':
        pass
    elif calc_entry_number == 'Syntax Error':
        calc_entry.delete(0,'end')
        calc_entry.insert(0,'0')
    else:
        calc_entry.delete(length-1, 'end')
        if length == 1:
            calc_entry.insert(0,'0')

def dot_func():
    last_char = calc_entry.get()[-1]
    if last_char == '.':
        pass
    else:
        calc_entry.insert('end', '.')

# -------------------------- Calculator ------------------------


calc_entry = tk.Entry(bottom, width=25, bd=4, justify=tk.RIGHT, font='verdana 12 bold')
calc_entry.insert(0, '0')
calc_entry.place(x=440, y=340)

# buttons
one_btn = tk.Button(bottom, text='1', bd=5,font='verdana 12 bold', width=3, command= lambda x='1':calc_numbers(x))
one_btn.place(x=440, y=380)

two_btn = tk.Button(bottom, text='2', bd=5,font='verdana 12 bold', width=3, command= lambda x='2':calc_numbers(x))
two_btn.place(x=520, y=380)

three_btn = tk.Button(bottom, text='3', bd=5,font='verdana 12 bold',width=3, command= lambda x='3':calc_numbers(x))
three_btn.place(x=600, y=380)

four_btn = tk.Button(bottom, text='4', bd=5,font='verdana 12 bold', width=3, command= lambda x='4':calc_numbers(x))
four_btn.place(x=440, y=430)

five_btn = tk.Button(bottom, text='5', width=3,bd=5,font='verdana 12 bold', command= lambda x='5':calc_numbers(x))
five_btn.place(x=520, y=430)

six_btn = tk.Button(bottom, text='6',width=3, bd=5,font='verdana 12 bold', command= lambda x='6':calc_numbers(x))
six_btn.place(x=600, y=430)

seven_btn = tk.Button(bottom, text='7',width=3, bd=5,font='verdana 12 bold', command= lambda x='7':calc_numbers(x))
seven_btn.place(x=440, y=480)

eight_btn = tk.Button(bottom, text='8',width=3, bd=5,font='verdana 12 bold', command= lambda x='8':calc_numbers(x))
eight_btn.place(x=520, y=480)

nine_btn = tk.Button(bottom, text='9',width=3, bd=5,font='verdana 12 bold', command= lambda x='9':calc_numbers(x))
nine_btn.place(x=600, y=480)

plus_btn = tk.Button(bottom, text='+',width=3, bd=5,font='verdana 12 bold', command= lambda x='+':calc_operators(x))
plus_btn.place(x=670, y=380)

minus_btn = tk.Button(bottom, text='-',width=3, bd=5,font='verdana 12 bold', command= lambda x='-':calc_operators(x))
minus_btn.place(x=670, y=430)

multiply_btn = tk.Button(bottom, text='*',width=3, bd=5,font='verdana 12 bold', command= lambda x='*':calc_operators(x))
multiply_btn.place(x=670, y=480)

divide_btn = tk.Button(bottom, text='/',width=3, bd=5,font='verdana 12 bold', command= lambda x='/':calc_operators(x))
divide_btn.place(x=670, y=530)

zero_btn = tk.Button(bottom, text='0',width=3, bd=5,font='verdana 12 bold', command= lambda x='0':calc_numbers(x))
zero_btn.place(x=440, y=530)

del_btn = tk.Button(bottom, text='Del',width=3, bd=5,font='verdana 12 bold', command = del_func)
del_btn.place(x=520, y=530)

dot_btn = tk.Button(bottom, text='.',width=3, bd=5,font='verdana 12 bold', command = dot_func)
dot_btn.place(x=600, y=530)

equal_btn = tk.Button(bottom, text='=',width=10, bd=5,font='verdana 12 bold', command = equal)
equal_btn.place(x=440, y=580)

c_btn = tk.Button(bottom, text='C',width=10, bd=5,font='verdana 12 bold', command = c_func)
c_btn.place(x=600, y=580)




win.mainloop()