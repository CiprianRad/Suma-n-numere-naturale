#this function calculates the sum of the first n numbers using a loop
def sum_of_natural_numbers(n):
    total = 0
    for i in range (0, n):
        total += i
    return total


# this function allows us to get a valid input from the user
def get_natural_number_input():
    while True:  # while True will run this function until we get the valid input from the user
        try:  # the try block will probe if what the user inputed will lead to an error or not 
            n = int(input("Enter a natural number: "))
            if n > 0:
                return n
            else: # this is how we handled the error or exception in case n is negative
                print("Please enter a number greater than zero: ")
        except ValueError: #we used a value error keyword to make sure the user does not input strings or other charaters
            print("Invalid input. Please enter a valid natural number ")






def main():
    n = get_natural_number_input()
    print("Sum of the first n numbers is", sum_of_natural_numbers(n))

main()



