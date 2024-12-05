# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
INVERT = "\033[7m"
# Text color
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
# Background color
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def text_color(color):
    color = color.strip().title()
    if color == "Black":
        return f"{BLACK}"
    elif color == "Red":
        return f"{RED}"
    elif color == "Green":
        return f"{GREEN}"
    elif color == "Yellow":
        return f"{YELLOW}"
    elif color == "Blue":
        return f"{BLUE}"
    elif color == "Magenta":
        return f"{MAGENTA}"
    elif color == "Cyan":
        return f"{CYAN}"
    elif color == "White":
        return f"{WHITE}"

if __name__ == "__main__":
    print(f"{BLACK}HEY,{BLUE}HEY,{RED}HEY,{GREEN}HEY,{YELLOW}HEY,{MAGENTA}HEY,{CYAN}HEY,{WHITE}HEY")
