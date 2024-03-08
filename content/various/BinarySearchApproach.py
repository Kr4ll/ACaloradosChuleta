lower_bound = 2
upper_bound = 10
# Number to be guessed is 9
# Applying Binary Search interactively
while (lower_bound <= upper_bound) :
    mid = (lower_bound + upper_bound) // 2
    # Print guessed number
    print(mid)
    stdout.flush()
    # Input the response from the judge
    response = int(input())
    if (response == -1) :
        lower_bound = mid + 1
    elif (response == 1) :
        upper_bound = mid - 1
    elif (response == 0) :
        print("Number guessed is :", mid)
        stdout.flush()
        break
