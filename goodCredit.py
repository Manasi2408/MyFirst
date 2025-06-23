# good credit score check 

price = 10000000

print("House price is ₹ 1,00,00,000")

while True:
    print("Do you want to buy it ? (yes/no)")
    answer = input().upper()

    if answer == "YES":
        print("Do you have good credit score ? (yes/no)")
        cred = input().upper()

        if cred == "YES":
            print("Down payment by 10%")
            downPay = price * 0.1
            break

        elif cred == "NO":
            print("Down payment by 20%")
            downPay = price * 0.2
            break
            
        else:
            print("Error")
            continue
        
    elif answer == "NO":
        print("No worries !")
        downPay = 0
        cred = "N/A"
        break
        
    else:
        print("Error")    

print()

print("House buy :",answer)
print("Good Credit Score :",cred)
print("How much to pay ₹",downPay)