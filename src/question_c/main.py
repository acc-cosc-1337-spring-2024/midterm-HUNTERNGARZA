from question_c import is_prime


while True:
    user_continue = input("continue (y/n)?? ")
    if user_continue == "n":
        break

    user_number = int(input("number plz: "))
    print("number is prime: ", is_prime(user_number))
