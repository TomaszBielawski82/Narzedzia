for i in range(1, 101):
    
    if (i % 5 == 0 and i % 3 == 0):
        print (i, "BEST")
    elif (i % 5 == 0):
        print (i, "BETTER")
    elif (i % 3 == 0):
        print (i, "GOOD")
    else:
        print (i)
