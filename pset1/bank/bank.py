text = input("Greeting: ")

if text.lower().strip() == "hello" or text.lower().strip() == "hello there" or text.lower().strip() == "hello, newman" :
    print("$0")

elif text.lower().strip()[0] == "h" and text.lower().strip() != "hello":
    print("$20")

else:
    print("$100")