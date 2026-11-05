# Step 1
# In this workshop, you will practice working with numbers and mathematical operations to build a bill splitter. This tool will calculate how much each person owes after adding meal costs and a tip.

# To start, you need a way to keep track of the total amount as costs are added.

# Create a variable named running_total and assign it the value 0.
running_total = 0

# Step 2
# Next, you need to account for the number of people sharing the bill. Store this value in a variable, as you did in the previous step.

# Create a variable named num_of_friends and assign it the value of 4. This will be used later in the workshop to calculate the final split.
num_of_friends = 4

# Step 3
# Each course has a cost. You need to store these amounts in variables to use them later. Since these amounts include cents, you will use the float type.

# Create four variables: appetizers set to 37.89, main_courses set to 57.34, desserts set to 39.39, and drinks set to 64.21.
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Step 4
# Now that you have stored the individual costs, you can calculate the total.

# Recall that the += operator adds a value to an existing variable and updates it at the same time. For example:

# Example Code
# total = 10
# total += 2 + 2 + 1
# print(total)  # total is now 15
# Use the += operator once to add appetizers, main_courses, desserts, and drinks to running_total.

# Finally, use print() to display the string Total bill so far: followed by a space and the value of running_total.

# Note: You might notice that the output has more decimal digits than expected. As you learned in a previous lesson, this happens because numbers are stored in binary, and many decimal values cannot be represented exactly in this format, which leads to rounding errors.
running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}')

# Step 5
# The service was excellent, so the group decides to leave a 25% tip. To calculate a percentage in Python, you can multiply the total by the decimal equivalent of the percentage.

# For example, to find 10% of a value, you would multiply it by 0.10 using the * operator:

# Example Code
# tax = total * 0.10
# Create a variable named tip and assign it the result of multiplying running_total by 0.25.

# Finally, use print() to display the string Tip amount: followed by a space and the value of your tip variable.
tip = running_total * 0.25
print(f'Tip amount: {tip}')

# Step 6
# Now that you have calculated the tip, you need to add it to your running_total to find the final bill amount.

# Use the += operator to add the value of tip to your running_total. Finally, use print() to display the string Total with tip: followed by a space and the value of running_total.
running_total += tip
print(f"Total with tip: {running_total}")

# Step 7
# With the tip now included, you have the final amount for the entire group. You have to determine how much each person owes by dividing the total bill by the number of friends.

# In Python, you use the forward slash / to perform division. For example:

# Example Code
# half = 10 / 2
# Create a variable named final_bill and assign it the result of dividing running_total by num_of_friends.

# Finally, use the print() function to display the string Bill per person: followed by a space and the value of final_bill.
final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

# Step 8
# The bill is split, but division often results in long decimal numbers. Since money is typically represented with two decimal places, you should round the final result.

# In an earlier lesson, you learned about the round() function which takes two arguments: the number you want to round and the number of decimal places to keep. Here's an example:

# Example Code
# num = 4.815162342
# round(num, 3) # 4.815
# Use the round() function to round final_bill to two decimal places and assign the result to a new variable named each_pays.

# Finally, use print() to display the string Each person pays: followed by a space and your each_pays variable.

# With that, the bill splitter workshop is complete.
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
