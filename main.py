from tkinter import *

mw = Tk()
mw.title('Order Form')
mw.geometry('900x720')

#creating frame
frame1 = LabelFrame(mw, text='This is Frame1', width=400 padx=10, padx=10), front=('',14)
frame1.grid(row=0, column=0, padx=20,pady=10)

exit_btn = button(frame1, text='Exit!', padx=60, pady=12, front=('', 14), command=mw.quit)
exit_btn.pack()

#creating Radio Buttons

def cv_res():
    cv_lbl.config(text=cv.get())

rv = StringVar()
rv.set(Add Item)
Radiobutton(frame1, text='option 1', value='Add Item', variable=rv, font=('', 14), command=rv_res).pack(pady=(30, 10))
Radiobutton(frame1, text='option 2', value='Cancle', variable=rv, font=('', 14), command=rv_res).pack(pady=(0, 20))

rv_lbl = Lable(frame1, text=rv.get(), font=('', 14))
rv_lbl.pack()

#Creating Check Buttons/Boxes
def cv_res()
    cv_lbl.config(text=cv.get())

cv = StringVar()
cb = Checkbutton(frame1, text='Do you want parcel?', variable=cv , font=('',14), onvalue='YES', offvalue='NO',command=cv_res)

cb.deselect()
cb.pack(pady=(30, 10))

cv1 = StringVar()
cb1 = Checkbutton(frame1, text='Do you want eat?', variable=cv , font=('',14), onvalue='YES', offvalue='NO',command=cv_res)

cb1.deselect()
cb1.pack(pady=(30, 10))

cv_lbl = Lable(frame1, text=rv.get(), front=('', 14))
cv_lbl.pack(pady=(0, 30))

#creating Drop down menus

months = ['Veg Birayani','Chicken Birayani','Dum Birayani','lolly pops','wings']
selected = StringVar()
selected.set('Dum Biryani')
opts = OptionMenu(frame1, selected *Items)
opts.config(font=('', 14))
opts.pack(pady=(0, 30))

opts_menu = frame1.nametowidget(opts.menuname)
opts_menu.config(font=('', 12))

