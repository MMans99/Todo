from tkinter import *
import tkinter.messagebox



window=Tk()
window.title("Todo-list")

def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()
    root1.mainloop()
    
#function to facilitate the delete task from the Listbox
def deletetask():
    #selects the selected item and then deletes it 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

#Executes this to mark completed/uncompleted 
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    #if condition to mark it complete or show warning
    if "✔" not in temp_marked: 
        temp_marked = temp_marked + " ✔"
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Already completed!")
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)

def markuncompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    #if condition to mark it uncomplete or show warning
    if "✔" in temp_marked: 
        temp_marked=temp_marked.replace("✔", "")
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="Already uncompleted!")
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)


#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()
#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font = "Helvetica")  
listbox_task.pack(side=tkinter.LEFT)
#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)
#Button widget 
entry_button=Button(window,text="Add Task",width=50,command=entertask)
entry_button.pack(pady=3)
delete_button=Button(window,text="Delete Selected Dask",width=50,command=deletetask)
delete_button.pack(pady=3)
mark_button=Button(window,text="Mark as Completed ",width=50,command=markcompleted)
mark_button.pack(pady=3)
mark_button=Button(window,text="Mark as Uncompleted ",width=50,command=markuncompleted)
mark_button.pack(pady=3)
window.mainloop()




