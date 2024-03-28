weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
if unit=="l":
    print("you are ", 0.45*int(weight)," kilos")
elif unit=="k":
    print("you are ", int(weight)/0.45, " pounds")
