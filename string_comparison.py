def comparison (str1, str2):
    if isinstance(str1,str) != isinstance(str2,str):
        print("0")
    elif str1 == str2:
        print("1")
    elif str1 > str2:
        print("2")
    elif str1 != str2 and str2 == "learn":
        print("3")

comparison(1, "learn")
comparison("learn", "learn")
comparison("!!!!!!!!", "!!")
comparison("!!!!!!!!", "learn")

