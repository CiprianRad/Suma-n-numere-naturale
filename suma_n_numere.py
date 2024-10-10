def sum_of_natural_numbers(n):
    total = 0
    for i in range (0, n):
        total += i
    return total



def get_natural_number_input():
    while True:
        try:
            n = int(input("Enter a natural number: "))
            if n > 0:
                return n
            else:
                print("Please enter a number greater than zero: ")
        except ValueError:
            print("Invalid input. Please enter a valid natural number ")






def main():
    n = get_natural_number_input()
    print("Sum of the first n numbers is", sum_of_natural_numbers(n))

main()


