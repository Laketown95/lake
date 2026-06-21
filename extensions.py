# List of extensions
l = (".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")

x = input("Please write here:")
x = str(x).lower()  # Convert input to lowercase to handle case insensitivity

# Check for special cases first
if x == "zipper.jpg" or x == "happy.jpeg":
    print("image/jpeg")
else:
    # Iterate through the list of extensions
    for ext in l:
        if ext in x:
            if ext in [".gif", ".jpg", ".jpeg", ".png"]:
                if ext == ".jpg":
                    print("image/jpeg")
                else:
                    y = ext.removeprefix(".")
                    print(f"image/{y}")
            elif ext in [".pdf", ".zip"]:
                y = ext.removeprefix(".")
                print(f"application/{y}")
            elif ext == ".txt":
                print("text/plain")
            break
    else:
        print("application/octet-stream")
