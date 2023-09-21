def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

unit_sys = int(input("Choose unit system\n1)Kg and m        2)lbs and ft-in\n"))
if unit_sys == 1:
    print("Enter")
    w = float(input("weight:"))
    h = float(input("height:"))
elif unit_sys == 2:
    print("Enter weight, then height")
    w = float(input("weight(lbs):"))
    h_ft = float(input("height(ft):"))
    h_in = float(input("(in):"))
    # converting from lbs and ft-in
    w = lb_to_kg(w)
    h = ft_and_inch_to_m(h_ft, h_in)

print("Your BMI is ", round(bmi(weight=w, height=h),2))
