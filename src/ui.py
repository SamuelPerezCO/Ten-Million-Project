from customtkinter import *
from crud import *

set_appearance_mode("dark")

app = CTk()
app.geometry("600x500")
app.minsize(600, 500)
app.title("Ten Million Project")

# Layout general
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=3)


def btn_create_savings():
    create_savings()


def btn_read_savings():
    read_savings()


def btn_update_savings():
    update_savings


def btn_delete_saving():
    delete_savings()


left_container = CTkFrame(master=app, fg_color="transparent")
left_container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

left_container.grid_columnconfigure(0, weight=1)
left_container.grid_rowconfigure(1, weight=1)

label_savings = CTkLabel(master=left_container, text="Savings", font=("Arial", 18, "bold"))
label_savings.grid(row=0, column=0, pady=(0, 10))  # centrado

left_frame = CTkScrollableFrame(
    master=left_container,
    fg_color="#1E1E1E",
    border_color="#FFCC70",
    border_width=2
)
left_frame.grid(row=1, column=0, sticky="nsew")


right_frame = CTkFrame(master=app, fg_color="transparent")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

btn_create = CTkButton(
    master=right_frame,
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
    master=right_frame,
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
    master=right_frame,
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
    master=right_frame,
    text="DELETE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=btn_delete_saving
)
btn_delete.place(relx=0.5, rely=0.8, anchor="center")

label_version = CTkLabel(master=right_frame, text="Version 0.0.1", font=("Arial", 10))
label_version.place(relx=0.99, rely=0.99, anchor="se")


for i in range(1, 21):
    CTkLabel(left_frame, text=f"Item {i}").pack(anchor="w", padx=10, pady=4)

app.mainloop()
