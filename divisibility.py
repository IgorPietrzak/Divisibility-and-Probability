def main():
    # Create list to store the upper and lower bound:
    bounds = []
    # Get user to input their desired range:
    lower_boundi = int(input("Enter lower bound: "))
    upper_boundi = int(input("Enter upper bound: "))
    if lower_boundi > upper_boundi:
        upper_bound = lower_boundi
        lower_bound = upper_boundi
    else:
        lower_bound = lower_boundi
        upper_bound = upper_boundi
    # Append bounds to list:
    bounds.append(lower_bound)
    bounds.append(upper_bound)
    print(f"Range: {bounds}")

    # Let user choose a,b for which we return the number of numbers in range divisible by a and b:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    # Variables storing the number of numbers divisible by a and b:
    num_a = 0
    num_b = 0
    # Loop counts number of numbers divisible by a and b:
    for num in range(lower_bound, upper_bound + 1):
        if num % a == 0:
            num_a = num_a + 1
    for num in range(lower_bound, upper_bound + 1):
        if num % b == 0:
            num_b = num_b + 1

    # Calculate # of numbers divisble by both a and b:
    num_a_or_b = 0
    num_a_and_b = 0
    for n in range(lower_bound, upper_bound + 1):
        if n % a == 0 or n % b == 0:
            num_a_or_b = num_a_or_b + 1
    for c in range(lower_bound, upper_bound + 1):
        if c % a == 0 and c % b == 0:
            num_a_and_b = num_a_and_b + 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"There are {num_a} numbers divisible by {a} between {lower_bound} and {upper_bound}")
    print(f"There are {num_b} numbers divisible by {b} between {lower_bound} and {upper_bound}")
    print(f"There are {num_a_or_b} numbers divisible by {a} or {b} between {lower_bound} and {upper_bound}")
    print(f"There are {num_a_and_b} numbers divisible by {a} and {b} between {lower_bound} and {upper_bound}")
    # Calculate probabilities:
    omega = []
    for i in range(lower_bound, upper_bound + 1):
        omega.append(i)
    size = len(omega) # Size of sample space
    PA = num_a / size
    PB = num_b / size
    P_A_or_B = num_a_or_b / size
    P_A_and_B = num_a_and_b / size
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("PROBABILITIES:")
    print(f"P(number is divisble by {a}) = {PA}")
    print(f"P(number is divisble by {b}) = {PB}")
    print(f"P(number is divisble by {a} OR {b}) = {P_A_or_B}")
    print(f"P(number is divisble by {a} AND {b}) = {P_A_and_B}")

    # Ask user if they want to re-run the program:
    def choose():
        choice = input("Would you like to start a new calculation y/n: ")
        if choice == "y":
            main()
        elif choice == "n":
            exit()
        else:
            print("Invalid input, please try again.")
            choose()
    choose()

main()
