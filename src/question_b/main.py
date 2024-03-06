from question_b import get_random_number


while True:
    user_quit = input("continue (y/n)? ")
    if user_quit == "n":
        break

    while True:
        generated_number = get_random_number()
        user_number = int(input("guess number: "))
        if generated_number == user_number:
            print("congratulations")
            break

        print("wrong, it was", generated_number)