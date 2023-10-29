grocery_dict = {}
try:
    while True:
        element = input().upper()

        if element in grocery_dict:
            grocery_dict[element] += 1
        else:
            grocery_dict[element] = 1

except EOFError:
    sorted_keys = sorted(grocery_dict.keys())
    for k in sorted_keys:
        print(f"{grocery_dict[k]} {k}")