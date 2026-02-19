from customtkinter import *

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")

def click_handler():
    print("Button Clicked")

btn = CTkButton(master=app, text = "Click Me" , 
                corner_radius=32,
                fg_color="#4158D0",
                hover_color="#4158D0",
                border_color="#FFCC70",
                border_width=2,
                command=click_handler)

btn.place(relx=0.5, rely=0.5, anchor="center")

label = CTkLabel(master=app, text="Some Text..." , font=("Arial" , 20))

label.place(relx=0.5 , rely=0.4 , anchor="center")

combobox = CTkComboBox(master=app, values=["option 1" , "Option 2" , "Option 3"] , fg_color="#0093E9",
                       border_color="#FBAB7E" , dropdown_fg_color="#0093E9")

combobox.place(relx = 0.5 , rely = 0.6  , anchor = "center")

entry = CTkEntry(master=app , placeholder_text="How much are you going to save?" , width=300,)
entry.place(relx = 0.5 , rely = 0.7 , anchor = "center")


app.mainloop()