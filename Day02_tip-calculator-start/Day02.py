'''
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
'''
'''
output:
Each person should pay: $19.93
'''

print('What to the tip calculator!')

bill = int(input('What was the total bill? '))

tip = int(input('How much tip would you like to give? '))

people = int(input('How many people split the bill '))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_amount = bill + total_tip_amount
split_bill = total_amount/people

round_bill = round(split_bill, 2)

print(
    f"everyone's share of the total bill is ${bill/people} plus a ${total_tip_amount/people} tip.")
print(f'Each person should pay: ${split_bill}')

