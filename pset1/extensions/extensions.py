file_name = input("Enter the file name: ")
l = file_name.lower().split(".")
if l[-1] == "gif" or l[-1] == "jpeg" or l[-1] == "png" :
    print(f"image/{l[-1]}")
elif l[-1] == "jpg":
    print(f"image/jpeg")

elif l[-1] == "bin":
    print("application/octet-stream")

elif l[-1] == "txt":
    print("text/plain")

elif len(l) == 1:
    print("application/octet-stream")

else:
    print(f"application/{l[-1]}")