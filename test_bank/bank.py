def main():
    greet = (input("Greeting: ")).lower().strip()
    print(f"${value(greet)}")


def value(greeting):
    if greeting.startswith("hello"):
        return 20
    else:
        return 100




    if __name__ == "__main__":
        main()
