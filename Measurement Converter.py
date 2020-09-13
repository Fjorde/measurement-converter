#Measurement Converter v0.1
#Inputs
print("Measurement Converter v0.1")
print("Inch = in, Mile = mi, Foot = ft,\nPound = lb, Stone = st, Ounce = oz,\nGallon = gl, Quart = qu, Fl. Ounce = fl oz")
unittype = input("Type L for length, M for mass/weight,\nC for capacity, and T for temperature,\nS for speed, A for area, V for volume: ").upper()
unit1 = input("Measurement to convert from: ").lower()
unit2 = input("Measurement to convert to: ").lower()
value = float(input("Value: "))
#Messages
invalid = "What you have typed is invalid. Please type two valid measurements"
valid = "Your measurements have been received. Calculating..."
#Temperature
if unittype == "L":
    if unit1 == "cm" and unit2 == "m":
        print(valid)
        ans = float(value/100)
    elif unit1 == "m" and unit2 == "cm":
        print(valid)
        ans = float(value*100)
    elif unit1 == "ft" and unit2 == "m":
        print(valid)
        ans = float((value/100)*30.48)
    else:
        print(invalid)
    print(ans, unit2)
#Temperature
if unittype == "T":
    if unit1 == "f" and unit2 == "c":
        print(valid)
        ans = float((value-32)*(5/9))
    elif unit1 == "k" and unit2 == "c":
        print(valid)
        ans = float(value+273.15)
    elif unit1 == "f" and unit2 == "k":
        print(valid)
        ans = float((value-32)*(5/9)+273.15)
    elif unit1 == "c" and unit2 == "k":
        print(valid)
        ans = float(value-273.15)
    elif unit1 == "k" and unit2 == "f":
        print(valid)
        ans = float((value-273.15)*(9/5)+32)
    elif unit1 == "c" and unit2 == "f":
        print(valid)
        ans = float((value*(9/5))+32)
    else:
        print(invalid)
    print(ans, unit2)
