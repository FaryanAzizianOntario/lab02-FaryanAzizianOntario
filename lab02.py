# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:0d}:{minutes:02d}:{seconds:02d}"


def admission_price(age):

    price = 10.0

    if(age < 0):
        return "Age must be more than 0"

    if(age < 5):
        price = 0.0

    elif(5 <= age <= 12):
        price = 8.0

    elif(13 <= age <= 64):
        price = 15.0

    return price



def sum_multiples(limit):

    num = 0
    sum = 0

    while(num < limit):

        if(num % 3 == 0 or num % 5 == 0):
            sum += num

        num += 1

    return sum


def total_of_positives(numbers):

    sum = 0

    for num in numbers:
        if(num >= 0):
            sum += num
            
    return sum

def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    #print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass

if __name__ == "__main__":
    main()
