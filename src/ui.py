from customtkinter import *

set_appearance_mode("dark")

app = CTk()
app.geometry("600x500")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)  
app.grid_columnconfigure(1, weight=3)  

left_frame = CTkScrollableFrame(
    master=app,
    width=220,
    fg_color="#1E1E1E",
    border_color="#FFCC70",
    border_width=2
)
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

right_frame = CTkFrame(master=app, fg_color="transparent")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


def click_handler():
    print("Button Clicked")


btn = CTkButton(
    master=right_frame,
    text="Click Me",
    corner_radius=32,
    fg_color="#4158D0",
    hover_color="#4158D0",
    border_color="#FFCC70",
    border_width=2,
    command=click_handler
)
btn.place(relx=0.5, rely=0.5, anchor="center")

label = CTkLabel(master=right_frame, text="Some Text...", font=("Arial", 20))
label.place(relx=0.5, rely=0.35, anchor="center")

combobox = CTkComboBox(
    master=right_frame,
    values=["option 1", "Option 2", "Option 3"],
    fg_color="#0093E9",
    border_color="#FBA7BE",
    dropdown_fg_color="#0093E9"
)
combobox.place(relx=0.5, rely=0.6, anchor="center")

entry = CTkEntry(
    master=right_frame,
    placeholder_text="How much are you going to save?",
    width=250
)
entry.place(relx=0.5, rely=0.7, anchor="center")

for i in range(1, 21):
    CTkLabel(left_frame, text=f"Item {i}").pack(anchor="w", padx=10, pady=4)

app.mainloop()
