## if its your 50 anniversary, give the user a 50% discount

hotel_rate = 155
num_years = int(input("Enter years married: "))

if num_years == 50:
    hotel_rate /= 2
    print("Congrats on your anniversary")

print(f"Your hotel rate: ${hotel_rate:.2f}")