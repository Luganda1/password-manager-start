import json
from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pswd_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(1, 2)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    input_pwd.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- PASSWORD MANAGER ------------------------------- #\


def search():
    website = input_web.get()
    pswd = input_pwd.get()
    try:
        with open("data.json", mode='r')as data_file:
            # Opening in the json file
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="This file does not exist")
    else:
        if website in data:
            input_pwd.insert(0, data[website]['pswd'])
            messagebox.showinfo(title="Message", message=f"Your password for {website} is {data[website]['pswd']}")
        else:
            messagebox.showerror(title="Oops", message=f"there is no file name {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_pswd():
    website = input_web.get()
    user = input_user.get()
    pswd = input_pwd.get()
    new_data = {
        website: {
            "user": user,
            "pswd": pswd
        }
    }
    # if len(website) == 0 or len(pswd) == 0:
    if website == "" or pswd == "":
        messagebox.showerror(title="Oops", message="Sorry!! all inputs are required")
    else:
        # is_correct = messagebox.askokcancel(title="Message", message=f"Is your information correct: \n{website} \n {user} \n{pswd}")
        # if is_correct:
        try:
            with open("data.json", mode='r')as data:
                # Opening in the json file
                data_f = json.load(data)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # updating the data in the json
            data_f.update(new_data)
            with open("data.json", mode="w") as data:
                # writing the new data into the file
                json.dump(data_f, data, indent=4)
        finally:
            # clearing the prompts for new password
            input_web.delete(0, END)
            # input_user.delete(0, END)
            input_pwd.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

#creating label for website and input
label_web = Label(text="Website: ", font=("Arial", 10, "normal"))
label_web.grid(column=0, row=2)

input_web = Entry()
input_web.config(width=34)
input_web.focus()
input_web.grid(column=1, row=2)


#creating label for username or email and input
label_user = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
label_user.grid(column=0, row=3)

input_user = Entry()
input_user.config(width=55)
input_user.insert(0, "rugant4@gmail.com")
input_user.grid(column=1, row=3, columnspan=2)


#creating label for password and input
label_pwd = Label(text="Password: ", font=("Arial", 10, "normal"))
label_pwd.grid(column=0, row=4)

input_pwd = Entry()
input_pwd.config(width=34)
input_pwd.grid(column=1, row=4)



button_gen = Button(text="Generate Password", command=pswd_generator)
button_gen.config(padx=7, pady=0)
button_gen.grid(column=2, row=4)

button_gen = Button(text="Search", command=search)
button_gen.config(padx=39, pady=0)
button_gen.grid(column=2, row=2)


button_add = Button(text="Add", command=save_pswd)
button_add.config(width=46)
button_add.grid(column=1, row=5, columnspan=2)





window.mainloop()
