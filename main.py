print("Welcome to the Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Want to add pepperoni? Y or N ")
extra_cheese = input("Want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
if extra_cheese == "Y":
    bill +=1

print(f"This is your total amount: ${bill}")