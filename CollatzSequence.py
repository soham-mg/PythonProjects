from Arithmetic import evenorodd
from time import ctime
import time
import statistics
import Colors
import sys
sys.set_int_max_str_digits(100000000)
def main():
    while True:
        number = ask_number()
        starttime = time.time()
        count, num_list = sequence(number)
        display(count, num_list, time,starttime)

def ask_number():
    while True:
        try:
            number = int(input(f"{Colors.text_color('magenta')}What's the number? "))
            # number = int(time.time())
            return number
        except ValueError:
            print("Please enter a valid number(It shouldn't have any decimal values) ")

def sequence(n):
    count = 0
    num_list = [n]
    while n != 1:
        if evenorodd(n) == "Even":
            n //= 2
            num_list.append(n)
            count += 1
        elif evenorodd(n) == "Odd":
            n = (3*n)+1
            num_list.append(n)
            count += 1
    return count, num_list

def display(count, num_list, time, starttime):
    print(f"{Colors.text_color('green')}Total count {count}:")
    i = 1
    for number in num_list:
        print(f"{Colors.text_color('blue')}{i}. {Colors.text_color('cyan')}{number}")
        i += 1
    print(f"{Colors.text_color('yellow')}{ctime()}")
    endtime = time.time()
    print(f"{Colors.text_color('white')}Exit time: {endtime-starttime}")

if __name__ == "__main__":
    main()