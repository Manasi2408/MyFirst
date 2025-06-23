# converting dollar to rupees

print("'d' to convert from $ to ₹")
print("'r' to convert from ₹ to $")

convert = input()

if convert == 'd':
    dollar = float(input("Enter $ : "))
    rs = 85.80 * dollar
    print(dollar,"$ is",rs,"₹")
else:
    rs = float(input("Enter ₹ : "))
    dollar = 0.012 * rs
    print(rs,"₹ is",dollar,"$")