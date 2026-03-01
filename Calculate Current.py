V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohms): "))
if R == 0:
    print("Resistance cannot be zero!")
else:
    I = V / R
    
    print("Current (I) =", I, "Amperes")
    if I < 0.5:
        print("Low current")
    elif 0.5 <= I <= 2:
        print("Normal current")
    else:
        print("High current")