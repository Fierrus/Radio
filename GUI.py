from tkinter import *
import LoadMAC
import main


mac_list_list = []
# Функция кнопки Add
def insert():
    data = gui_com.get()
    if data == '':
        print("Not valid")
    else:
        mac_list.insert(END, data)
        mac_list_list.append(data)
    gui_com.delete(0, END)


def start():
    # save_macs()
    main.exchange()


# def save_macs():
#    data = open('macs.txt', 'w')
#    for item in mac_list.get(0, END):
#        data.write(f'{item}\n')
#    data.close()


def del_mac():
    selected_macs = list(mac_list.curselection())
    selected_macs.reverse()
    for item in selected_macs:
        mac_list.delete(item)
        item = str(item)
        print(mac_list_list)
        mac_list_list.remove(item)


def on_closing():
    data = open('macs.txt', 'w')
    for item in mac_list.get(0, END):
        data.write(f'{item}\n')
    data.close()
    root.destroy()


# Инициализация виджетов и их расположение
root = Tk()
Label(text="МАС адреса:") \
    .grid(row=0, column=0)
mac_list = Listbox(selectmode=EXTENDED)
mac_list.grid(row=0, column=1)

gui_com = Entry()
gui_com.grid(row=1, column=1)

Button(text="Add", command=insert) \
    .grid(row=2, column=1,
          sticky=(W + E))
Button(text="Del", command=del_mac) \
    .grid(row=2, column=0,
          sticky=(W + E))
Button(text="Start", command=start) \
    .grid(row=3, column=1,
          sticky=(W + E))

# Загрузка MAC'ов в виджет списка
for mac in LoadMAC.read_mac():
    mac_list.insert(END, mac)
    mac_list_list.append(mac)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
