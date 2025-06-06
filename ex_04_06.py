def computepay(hrs, rate):
    if hrs <= 40 :
        pay = hrs * rate
    else :
        pay = 40 * rate + (hrs - 40) * rate * 1.5    
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

pay = computepay(float(hrs), float(rate))
print("Pay", pay)