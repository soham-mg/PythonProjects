from random import choice
from Colors import text_color
import time
def main():
    while True:
        words = []
        with open("english_words.txt") as file:
            for word in file:
                words.append(word.strip())
        n = int(input(f"{text_color('magenta')}How many LNs you wanna generate? ").strip().title())
        for _ in range(n):
            print(f"\033[36m{choice(words)}{text_color('yellow')}@\033[34m{choice(words)}")
        print(f"{text_color('green')}{time.ctime()}")

if __name__ == "__main__":
    main()