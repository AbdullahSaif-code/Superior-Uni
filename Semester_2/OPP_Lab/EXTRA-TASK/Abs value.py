def Absulate_Number(x):
    if type(x) in [int,float]:
        print(abs(x))
        print(f"Type of value is: {type(x)}")
    else:
        print("Enter numaric value.")
Absulate_Number(-15)