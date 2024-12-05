import random
import cowsay

def main():
    On = True
    while On:
        user, secret_number = ask()
        guess(secret_number, user)
        while True:
            print(str(cowsay.ghostbusters(f"So {user}, wanna play the game once again? ")))
            response = str(input("\033[34m\u2192 ")).strip().capitalize()
            if response == "Yes":
                break
            elif response == "No":
                print(f"""{cowsay.pig("Alright then! Quitting........")}""")
                break
            else:
                print(f"Hey {user}, seems like you haven't entered s valid prompt, please prompt either 'Yes' or 'No'")

        if response == "Yes":
            continue
        elif response == "No":
            break

def ask():
    name = str(input("\033[1mWhat's your name? \033[0m")).strip().capitalize()
    print(cowsay.miki(f"Hi, \033[36m{name}."))
    while True:
        try:
            x = int(input('''\033[ 
What should be the range of the secret number: From?? '''))
            y = int(input(f"What should be the range of the secret number: From \033[33m{x}\033[0m to? "))
            break
        except ValueError:
            print(cowsay.stegosaurus("Please enter a number!"))
    print(f"The secret number is between {x} to {y}")
    secret_number = random.randint(x, y)
    return name, secret_number

def guess(s,user):
    r1 = ["What do you think the number is ? ", "Your guess? ", "What's your guess? ", ]
    On = True
    while On:
        try:
            guess = int(input(f"{random.choice(r1)}"))
            if guess == s:
                print(f"\033[32mYou made the right guess! {guess} is the secret number")
                print(cowsay.dragon(f"Voila! {user} you won!!!"))
                break
            elif guess > s:
                print(cowsay.tux(f""""\033[31mSorry! You made the wrong guess
                {guess} is greater than the secret number"""))
            else:
                print(cowsay.trex(f""""\033[33mSorry! You made the wrong guess
                {guess} is smaller than the secret number"""))
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()



