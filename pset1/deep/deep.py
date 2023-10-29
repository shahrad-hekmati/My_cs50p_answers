answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

if answer.strip() == "42" or answer.lower().replace("-", " ") == "forty two":

    print("Yes")

else:

    print("No")