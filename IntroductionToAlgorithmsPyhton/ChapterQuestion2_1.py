for i in range(1950, 2051):
    if(i % 4 == 0):
        if(i % 100 == 0):
            if(i % 400 == 0):
                print(str(i) + "年\n")
        else: print(str(i) + "年\n")