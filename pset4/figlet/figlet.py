from pyfiglet import Figlet
import sys

figlet = Figlet()

if sys.argv[1] not in ["-f", "-font"]:
    sys.exit("Invalid usage")

str_input = input("Input: ")
figlet.getFonts()
figlet.setFont(font=sys.argv[2])
print(figlet.renderText(str_input))
