def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        print_row(size)

        #For each brick in row
def print_row(width):
    print("#" * width)

main()
