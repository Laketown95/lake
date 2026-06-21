import re

def main():
   print(validate(input("IPv4 Address: ")))

def validate(ip):
    byte = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    pattern = rf"^{byte}\.{byte}\.{byte}\.{byte}$"

    return bool(re.match(pattern, ip))

if __name__ == "__main__":
    main()
