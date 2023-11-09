import tkinter as tk
from tktimepicker import AnalogPicker, AnalogThemes
from api import *
from tkinter import filedialog,ttk,messagebox
from tktooltip import ToolTip
import os

root=tk.Tk()
root.title("Fitness Scheduler")
root.geometry("400x500")
root.tk.call("source", "Azure-ttk-theme-main/Azure-ttk-theme-main/azure.tcl")
root.tk.call("set_theme", "dark")

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def takepath(find):
    if(find.get().split(".")[-1]!="mp3" or find.get().split(".")[-1]!="mp4"):
         messagebox.showwarning(title="Oops",message="Định dang file không hợp lệ,xin lựa chọn file mp3 hoặc mp4")
         print(find.get().split(".")[-1])
         find.delete(0,tk.END)
         return
    takefilepath(find.get())
    find.delete(0,tk.END)

def takeinput1(time,reps,sound,change,ohour,ominute,otype):
    takeinput(time,reps,sound,change,ohour,ominute,otype)
    clear()
    mainframe()

def dele1(hour,minute,type):
    clear()
    Delete(hour,minute,type)
    mainframe()

def deletrack(event,selected_option,change,ohour,ominute):
    delefile(selected_option)
    clear()
    change_content(change,ohour,ominute)

def change_content(change,ohour,ominute,otype):
    clear()
    time_picker = AnalogPicker(root)
    time_picker.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    theme = AnalogThemes(time_picker)
    theme.setDracula()

    new_button1 = ttk.Button(root, text="Nút 1",command=mainframe)
    new_button1.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  
    
    alarm_frame = ttk.Frame(root)
    alarm_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Label for alarm count
    alarm_count_label = ttk.Label(alarm_frame, text="Số lần báo thức:")
    alarm_count_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Entry for alarm count (allowing user to input)
    cur_val=tk.StringVar(value=0)
    sdt=cur_val
    s=tk.Spinbox(alarm_frame,from_=1,to=10,textvariable=cur_val).grid(row=0,column=1,padx=5,pady=5,sticky='w')
    sdt.get()
    # Label for alarm sound selection
    alarm_sound_label = ttk.Label(alarm_frame, text="Chọn nhạc chuông:")
    alarm_sound_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    list=readfile()
    alarm_sound_options = [item[1] for item in list] # Thay bằng danh ssách các nhạc chuông
    alarm_sound_variable = tk.StringVar(root)
    if(alarm_sound_options!=[]):
        alarm_sound_variable.set(alarm_sound_options[0])  # Thiết lập giá trị mặc định
    alarm_sound_dropdown = ttk.Combobox(alarm_frame, textvariable=alarm_sound_variable, values=alarm_sound_options, state="readonly")
    alarm_sound_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    for option in alarm_sound_options:
        ToolTip(alarm_sound_dropdown, msg=f"Chuột phải để xoá lựa chọn")
    alarm_sound_dropdown.bind("<Button-3>", lambda event: deletrack(event, alarm_sound_variable.get(),change,ohour,ominute))

    new_button2 = ttk.Button(root, text="Nút 2",command=lambda : takeinput1(time_picker.time(),int(sdt.get()),alarm_sound_variable.get(),change,ohour,ominute,otype))
    new_button2.grid(row=0, column=1, padx=10, pady=10, sticky="ne")
def mainframe():
    clear()
    records=read_input()
    for i,record in enumerate(records):
        frame = ttk.Frame(root,borderwidth=5,relief="solid",padding=(10,10),height=50,style='Card.TFrame')
        frame.grid(row=i, column=0, sticky="w",pady=5)
        label = ttk.Label(frame, text=f"Hour={record[0]}, Minute={record[1]}, Type={record[2]}", padding=(5, 5), foreground="grey")
        label.grid(row=0, column=0, sticky="w")
        label.bind("<Button-1>",lambda event:change_content(1,record[0],record[1],record[2]))
        var=tk.IntVar(value=record[5])
        def takestate():
            switch(var.get(),record[0],record[1],record[2])
        button = ttk.Checkbutton(frame, style='Switch.TCheckbutton',variable=var,command=takestate)
        button.grid(row=0,column=1, sticky="w")
        delete_button = ttk.Button(frame, text="Delete",command=lambda : dele1(record[0],record[1],record[2]),style='Accent.TButton')
        delete_button.grid(row=0, column=2, sticky="w",padx=(10,5))
    find=ttk.Entry(root,font=20)
    find.grid(column=0,sticky="s",pady=30)
    def search_for_file_path (root): 
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
        find.delete(0,tk.END)
        find.insert(tk.END,tempdir)
        return tempdir
    path=ttk.Button(root,text="Browse",command=lambda: search_for_file_path(root)).grid(column=0)
    submit=ttk.Button(root,text="Submit",command=lambda: takepath(find)).grid()
    button = ttk.Button(root, text="Nhấn vào đây", command=lambda: change_content(0,0,0,"null"))
    button.grid( column=0, sticky="s", pady=20)
    ToolTip(button,msg="Thêm lịch tập")
    
   
mainframe()
root.mainloop()
