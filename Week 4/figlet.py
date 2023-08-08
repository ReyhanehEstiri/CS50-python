import sys, random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]

def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        render_message("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        render_message("Input: ", font)
    else:
        sys.exit("Invalid usage")


def render_message(prompt, f):
    txt = input(prompt)
    figlet.setFont(font=f)
    print("Output:",figlet.renderText(txt), sep="\n")
    
if __name__ == "__main__":
    main()
