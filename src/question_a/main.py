from question_a import get_sum_of_evens


while True:
    user_input = input("continue (y/n) ")
    if user_input == "n":
        break

    num = int(input("number: "))
    print(get_sum_of_evens(num))
