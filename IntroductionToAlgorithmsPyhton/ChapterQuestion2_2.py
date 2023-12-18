year = input("西暦の年号を入力してください：")
if(int(year) >= 1868 and int(year) < 1912):
    year = int(year) - 1868
    if(year == 0):
        print("明治元年です。")
    else: print("明治" + str(year) + "年です。")
elif(int(year) >= 1912 and int(year) < 1926):
    year = int(year) - 1912
    if(year == 0):
        print("大正元年です。")
    else: print("大正" + str(year) + "年です。")
elif(int(year) >= 1926 and int(year) < 1989):
    year = int(year) - 1926
    if(year == 0):
        print("昭和元年です。")
    else: print("昭和" + str(year) + "年です。")
elif(int(year) >= 1989 and int(year) < 2019):
    year = int(year) - 1989
    if(year == 0):
        print("平成元年です。")
    else: print("平成" + str(year) + "年です。")
elif(int(year) >= 2019):
    year = int(year) - 2019
    if(year == 0):
        print("令和元年です。")
    else: print("令和" + str(year) + "年です。")