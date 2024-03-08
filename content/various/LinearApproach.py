if __name__=='__main__':
    lower_bound = 2; 
    upper_bound = 10; 
    # Number to be guessed is 6 
    # Iterating from lower_bound to upper_bound 
    for i in range(lower_bound, upper_bound + 1):
        print(i)
        # Input the response from the judge 
        response = int(input())
        if (response == 0):
            print("Number guessed is :", i, end = '') 
            break;
