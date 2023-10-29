text = input("Enter the text: ")
res = [text[0].lower()]
for char in text[1:]:
    if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        res.append('_')
        res.append(char.lower())
    else:
        res.append(char)

print(''.join(res))