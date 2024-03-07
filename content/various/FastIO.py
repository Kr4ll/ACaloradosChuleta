def fast_io(): 

# Reinitialize the Input function
# to take input from the Byte Like
# objects
    input = io.BytesIO(os.read(0, \ 
         os.fstat(0).st_size)).readline 

    # Taking input as string
    s = input().decode() 

def fast_out():
# Output String
    s = "GeeksforGeeks\n"
    sys.stdout.write(s) 

# Output Array
    arr = [1, 2, 3, 4] 
    sys.stdout.write( 
        " ".join(map(str, arr)) + "\n"
    ) 
