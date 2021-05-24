import tkinter

def toggle_068(): ##define function for toggle of button
    index_dict_068={"On": "Off", "Off": "On"}## defining toggle options dictionary
    index_068[0] = index_dict_068[index_068[0]] 
    t_btn_068['text'] = index_068[0]

root = tkinter.Tk()# 
index_068=["On"]#display
t_btn_068 = tkinter.Button(text=index_068[0], width=12, command=toggle_068)#button widget makes it a button
t_btn_068.pack(pady=10) # packed in a box with padding 10

root.mainloop() #end by calling main loop
