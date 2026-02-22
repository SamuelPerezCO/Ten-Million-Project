from customtkinter import *
from crud import *

set_appearance_mode("dark")

app = CTk()
app.geometry("600x500")
app.minsize(600, 500)
app.title("Ten Million Project")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)

def btn_create_savings():
    show_view("create")

def btn_read_savings():
    read_savings()

def btn_update_savings():
    update_savings()

def btn_delete_saving():
    delete_savings()

left_container = CTkFrame(master=app, fg_color="transparent")
left_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

left_container.grid_columnconfigure(0, weight=1)
left_container.grid_rowconfigure(1, weight=1)

label_savings = CTkLabel(master=left_container, text="Savings", font=("Arial", 18, "bold"))
label_savings.grid(row=0, column=0, pady=(0, 10))

left_frame = CTkScrollableFrame(
    master=left_container,
    fg_color="#1E1E1E",
    border_color="#FFCC70",
    border_width=2
)
left_frame.grid(row=1, column=0, sticky="nsew")

right_frame = CTkFrame(master=app, fg_color="transparent")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

crud_frame = CTkFrame(master=right_frame, fg_color="transparent")
create_frame = CTkFrame(master=right_frame, fg_color="transparent")

views = {
    "crud": crud_frame,
    "create": create_frame,
}

def show_view(name: str):
    for v in views.values():
        v.grid_forget()
    views[name].grid(row=0, column=0, sticky="nsew")

# ===== CRUD VIEW =====
btn_create = CTkButton(
    master=crud_frame,
    text="CREATE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=btn_create_savings
)
btn_create.place(relx=0.5, rely=0.2, anchor="center")

btn_read = CTkButton(
    master=crud_frame,
    text="READ",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=btn_read_savings
)
btn_read.place(relx=0.5, rely=0.4, anchor="center")

btn_update = CTkButton(
    master=crud_frame,
    text="UPDATE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=btn_update_savings
)
btn_update.place(relx=0.5, rely=0.6, anchor="center")

btn_delete = CTkButton(
    master=crud_frame,
    text="DELETE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=btn_delete_saving
)
btn_delete.place(relx=0.5, rely=0.8, anchor="center")

label_version = CTkLabel(master=crud_frame, text="Version 0.0.1", font=("Arial", 10))
label_version.place(relx=0.99, rely=0.99, anchor="se")

title_create = CTkLabel(master=create_frame, text="Add Savings Item", font=("Arial", 18, "bold"))
title_create.place(relx=0.5, rely=0.12, anchor="center")

entry_name = CTkEntry(master=create_frame, placeholder_text="Item name")
entry_name.place(relx=0.5, rely=0.28, anchor="center", relwidth=0.7)

entry_amount = CTkEntry(master=create_frame, placeholder_text="Amount (COP)")
entry_amount.place(relx=0.5, rely=0.40, anchor="center", relwidth=0.7)

def save_item():
    name = entry_name.get().strip()
    amount = entry_amount.get().strip()

    # Logica para guardadr el item nuevo
    
    entry_name.delete(0, "end")
    entry_amount.delete(0, "end")
    show_view("crud")

btn_save = CTkButton(
    master=create_frame,
    text="SAVE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=save_item
)
btn_save.place(relx=0.5, rely=0.58, anchor="center")

btn_back = CTkButton(
    master=create_frame,
    text="BACK",
    corner_radius=32,
    fg_color="transparent",
    border_color="#FFCC70",
    border_width=2,
    command=lambda: show_view("crud")
)
btn_back.place(relx=0.5, rely=0.72, anchor="center")

# Mostrar vista inicial
show_view("crud")

for i in range(1, 21):
    CTkLabel(left_frame, text=f"Item {i}").pack(anchor="w", padx=10, pady=4)

app.mainloop()