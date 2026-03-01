from customtkinter import *
from crud import init_db, create_savings, read_savings

init_db()
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
    show_view("read")


def btn_update_savings():
    show_view("update")


def btn_delete_saving():
    show_view("delete")


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


def clear_left_list():
    for w in left_frame.winfo_children():
        w.destroy()


def refresh_left_list():
    clear_left_list()

    items = read_savings(limit=200)

    if not items:
        CTkLabel(left_frame, text="No items yet").pack(anchor="w", padx=10, pady=6)
        return

    for tx in items:
        tx_id = tx["id"]
        title = tx["title"]
        amount = tx["amount"]
        tx_type = tx["type"]
        created_at = tx["created_at"]

        sign = "+" if tx_type == "deposit" else "-"
        text = f"#{tx_id} {title}  {sign}{amount}  ({created_at})"
        CTkLabel(left_frame, text=text).pack(anchor="w", padx=10, pady=4)


right_frame = CTkFrame(master=app, fg_color="transparent")
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

# ===== VIEWS =====
crud_frame = CTkFrame(master=right_frame, fg_color="transparent")
create_frame = CTkFrame(master=right_frame, fg_color="transparent")
read_frame = CTkFrame(master=right_frame, fg_color="transparent")
update_frame = CTkFrame(master=right_frame, fg_color="transparent")
delete_frame = CTkFrame(master=right_frame, fg_color="transparent")

views = {
    "crud": crud_frame,
    "create": create_frame,
    "read": read_frame,
    "update": update_frame,
    "delete": delete_frame,
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


# ===== CREATE VIEW =====
title_create = CTkLabel(master=create_frame, text="Add Savings Item", font=("Arial", 18, "bold"))
title_create.place(relx=0.5, rely=0.12, anchor="center")

entry_create_name = CTkEntry(master=create_frame, placeholder_text="Item name")
entry_create_name.place(relx=0.5, rely=0.28, anchor="center", relwidth=0.7)

entry_create_amount = CTkEntry(master=create_frame, placeholder_text="Amount (COP)")
entry_create_amount.place(relx=0.5, rely=0.40, anchor="center", relwidth=0.7)

label_create_status = CTkLabel(master=create_frame, text="")
label_create_status.place(relx=0.5, rely=0.49, anchor="center")


def save_item():
    name = entry_create_name.get().strip()
    amount_raw = entry_create_amount.get().strip()

    if not name:
        label_create_status.configure(text="Name is required")
        return

    if not amount_raw.isdigit():
        label_create_status.configure(text="Amount must be a number")
        return

    amount = int(amount_raw)

    try:
        create_savings(title=name, amount=amount, tx_type="deposit")
        label_create_status.configure(text="Saved")
    except Exception as e:
        label_create_status.configure(text=f"Error: {e}")
        return

    entry_create_name.delete(0, "end")
    entry_create_amount.delete(0, "end")
    refresh_left_list()
    show_view("crud")


btn_create_save = CTkButton(
    master=create_frame,
    text="SAVE",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=save_item
)
btn_create_save.place(relx=0.5, rely=0.58, anchor="center")

btn_create_back = CTkButton(
    master=create_frame,
    text="BACK",
    corner_radius=32,
    fg_color="transparent",
    border_color="#FFCC70",
    border_width=2,
    command=lambda: show_view("crud")
)
btn_create_back.place(relx=0.5, rely=0.72, anchor="center")


# ===== READ VIEW =====
title_read = CTkLabel(master=read_frame, text="Read Savings", font=("Arial", 18, "bold"))
title_read.place(relx=0.5, rely=0.12, anchor="center")

entry_read_filter = CTkEntry(master=read_frame, placeholder_text="Filter by name (optional)")
entry_read_filter.place(relx=0.5, rely=0.26, anchor="center", relwidth=0.7)

read_output = CTkTextbox(master=read_frame)
read_output.place(relx=0.5, rely=0.58, anchor="center", relwidth=0.85, relheight=0.45)


def do_read():
    read_output.delete("1.0", "end")
    query = entry_read_filter.get().strip() or None

    items = read_savings(limit=300, search=query)

    if not items:
        read_output.insert("end", "No results\n")
        return

    for tx in items:
        tx_id = tx["id"]
        title = tx["title"]
        amount = tx["amount"]
        tx_type = tx["type"]
        created_at = tx["created_at"]
        sign = "+" if tx_type == "deposit" else "-"
        read_output.insert("end", f"#{tx_id} | {title} | {sign}{amount} | {created_at}\n")


btn_read_run = CTkButton(
    master=read_frame,
    text="RUN",
    corner_radius=32,
    fg_color="#0000FF",
    hover_color="#4158D0",
    border_color="#0000FF",
    border_width=2,
    command=do_read
)
btn_read_run.place(relx=0.5, rely=0.38, anchor="center")

btn_read_back = CTkButton(
    master=read_frame,
    text="BACK",
    corner_radius=32,
    fg_color="transparent",
    border_color="#FFCC70",
    border_width=2,
    command=lambda: show_view("crud")
)
btn_read_back.place(relx=0.5, rely=0.92, anchor="center")


# ===== UPDATE VIEW =====
title_update = CTkLabel(master=update_frame, text="Update Savings", font=("Arial", 18, "bold"))
title_update.place(relx=0.5, rely=0.12, anchor="center")

CTkLabel(master=update_frame, text="Soon").place(relx=0.5, rely=0.45, anchor="center")

btn_update_back = CTkButton(
    master=update_frame,
    text="BACK",
    corner_radius=32,
    fg_color="transparent",
    border_color="#FFCC70",
    border_width=2,
    command=lambda: show_view("crud")
)
btn_update_back.place(relx=0.5, rely=0.92, anchor="center")


# ===== DELETE VIEW =====
title_delete = CTkLabel(master=delete_frame, text="Delete Savings", font=("Arial", 18, "bold"))
title_delete.place(relx=0.5, rely=0.12, anchor="center")

CTkLabel(master=delete_frame, text="Soon").place(relx=0.5, rely=0.45, anchor="center")

btn_delete_back = CTkButton(
    master=delete_frame,
    text="BACK",
    corner_radius=32,
    fg_color="transparent",
    border_color="#FFCC70",
    border_width=2,
    command=lambda: show_view("crud")
)
btn_delete_back.place(relx=0.5, rely=0.92, anchor="center")


show_view("crud")
refresh_left_list()

app.mainloop()