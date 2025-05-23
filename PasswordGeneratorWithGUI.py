import random
from tkinter import *
import pyperclip 

def main():
    # colors
    # color-scheme1
    tb = "#99D5C9"  # Tiffany Blue
    ms = "#6C969D"  # Moonstone
    uv = "#645E9D"  # Ultra Violet
    rv = "#392B58"  # Russian Violet
    dp = "#2D0320"  # Dark Purple
    cs1 = tb, ms, uv, rv, dp
    # color-scheme2
    sa = "#EEC643"  # Saffron
    ni = "#141414"  # Night
    af = "#EEF0F2"  # Anti-flash white
    za = "#0D21A1"  # Zaffre
    ob = "#011638"  # Oxford Blue
    cs2 = ob, za, af, ni, sa
    # color-scheme3
    sg = "#B39C4D"  # Satin sheen green
    mg = "#768948"  # Moss green
    fg = "#607744"  # Fern green
    hg = "#34623F"  # Hunter green
    dg = "#1E2F23"  # Dark green
    cs3 = sg, mg, fg, hg, dg
    # color-scheme4
    mr = "#FDE8E9"  # Misty Rose
    ft = "#E3BAC6"  # Fairy Tale
    li = "#BC9EC1"  # Lifac
    pg = "#596475"  # Payne's Grey
    rb = "#1F2232"  # Raisin Black
    cs4 = mr, ft, li, pg, rb
    # color-scheme5
    ap = "#ffcdb2"  # Apricot
    me = "#ffb4a2"  # Melon
    sp = "#e5989b"  # Salmon Pink
    olr = "#b5838d"  # Old Rose
    di = "#6d6875"  # Dim Gray
    cs5 = ap,me,sp,olr,di

    c1, c2, c3, c4, c5 = cs1

    # fonts
    f1 = ("Impact", 20)
    f2 = ("Montserrat Black", 12)

    # lists for password generation
    # For Random characters
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`',
             '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '*', '.', '?', '/', '\\', '|',
             '<', '>', ',', ';', ':', '[', ']', '{', '}', "'", '"']
    # For Random Words
    words = []
    with open("english_words.txt") as lex:
        for word in lex:
            words.append(word.strip())  # Remove any trailing newline characters

    # main window setup
    win = Tk()
    win.geometry("400x400")
    win.title("Password Generator")
    win.configure(bg=c1)
    menubar = Menu(win)
    themeselect = Menu(menubar, bg=dp,fg="yellow")
    menubar.add_cascade(label="Theme", menu=themeselect)

    # Theme functions
    def set_theme(cs):
        nonlocal c1, c2, c3, c4, c5
        c1, c2, c3, c4, c5 = cs
        win.configure(bg=c1)
        header.configure(bg=c5, fg=c1)
        selectionlabel.configure(bg=c1)
        rcrb.configure(bg=c1, fg=c5)
        rwrb.configure(bg=c1, fg=c5)
        generatedpassword.configure(bg=c1)
        enterthelengthlabel.configure(bg=c1, fg=c5)
        lengthentrybox.configure(bg=c5, fg=c1)
        submitbuttonforrc.configure(bg=c2, fg=c4)
        submitbuttonforrw.configure(bg=c2, fg=c4)
        copybutton.configure(bg=c2, fg=c4)
        exitbutton.configure(bg=c5, fg=c1)

    themeselect.add_command(label="Twilight", command=lambda: set_theme(cs1))
    themeselect.add_command(label="Dusk", command=lambda: set_theme(cs4))
    themeselect.add_command(label="Forest", command=lambda: set_theme(cs3))
    themeselect.add_command(label="Peach", command=lambda: set_theme(cs5))

    # Button and other miscellaneous prompts functionality
    def rcgeneration():
        # When 'Random Characters' is selected, prompt for length and display the generated password
        enterthelengthlabel.pack(anchor="w")
        lengthentrybox.pack(anchor="w")
        submitbuttonforrc.pack(anchor="w")

        def passworddisplay():
            try:
                length = int(lengthentrybox.get())
                if length <= 0:
                    raise ValueError
                password = "".join(random.choice(chars) for _ in range(length))
                generatedpassword.configure(text=password, fg=c5)
                generatedpassword.pack(anchor="w")
            except ValueError:
                generatedpassword.configure(text="Please enter a valid length", fg="red")
                generatedpassword.pack(anchor="w")

        submitbuttonforrc.configure(command=passworddisplay)

    def rwgeneration():
        # When 'Random Words' is selected, generate a random string of words without asking for length
        submitbuttonforrw.pack(anchor="w")

        def passworddisplay():
            password = "".join(random.choice(words) for _ in range(4))  # Generates a 3-word passphrase by default
            generatedpassword.configure(text=password)
            generatedpassword.pack(anchor="w")

        submitbuttonforrw.configure(command=passworddisplay)

    # Function to copy the generated password to the clipboard
    def copy_to_clipboard():
        password = generatedpassword.cget("text")
        if password:
            pyperclip.copy(password)  # Copy to clipboard
            print("Password copied to clipboard!")

    # widget creation
    # Main UI
    header = Label(win, text="Password Generator", font=f1, width=500, bg=c5, fg=c1)
    selectionlabel = Label(win, text="What type of password do you want to generate", bg=c1, font=("Impact", 15))
    passtype = StringVar()
    rcrb = Radiobutton(win, text="Random Characters", value="rc", variable=passtype, bg=c1, fg=c5, font=f2,
                       activebackground=c4)
    rwrb = Radiobutton(win, text="Random Words", value="rw", variable=passtype, bg=c1, fg=c5, font=f2,
                       activebackground=c4)
    generatedpassword = Label(win, fg="#40167a", bg=c1, font=f2)
    exitbutton = Button(win, text="Exit", font=f2, bg=c5, fg=c1, activebackground=c4, command=lambda: win.quit())

    # When opted for 'random characters'
    enterthelengthlabel = Label(win, text="Enter the length of the password", font=f2, bg=c1, fg=c5)
    lengthentrybox = Entry(win, bg=c5, fg=c1)
    submitbuttonforrc = Button(win, text="Generate", bg=c2, fg=c4, font=f2, activebackground=c4)

    # When opted for 'random words'
    submitbuttonforrw = Button(win, text="Generate", bg=c2, fg=c4, font=f2, activebackground=c4)

    # Copy Button for copying the generated password
    copybutton = Button(win, text="Copy to Clipboard", bg=c2, fg=c4, font=f2, activebackground=c4, command=copy_to_clipboard)

    # widget setup
    header.pack()
    selectionlabel.pack(anchor="w")
    rcrb.pack(anchor="w")
    rwrb.pack(anchor="w")

    # Binding the radio buttons to the appropriate functions
    def on_select():
        # Remove the button from previous selection and hide length input
        submitbuttonforrc.pack_forget()
        submitbuttonforrw.pack_forget()
        enterthelengthlabel.pack_forget()
        lengthentrybox.pack_forget()

        if passtype.get() == "rc":
            rcgeneration()
        elif passtype.get() == "rw":
            rwgeneration()

    rcrb.config(command=on_select)
    rwrb.config(command=on_select)

    copybutton.pack(anchor="w")  # Add the Copy button to the UI
    exitbutton.pack(anchor="e", side="bottom")

    win.config(menu=menubar)
    win.mainloop()

if __name__ == "__main__":
    main()