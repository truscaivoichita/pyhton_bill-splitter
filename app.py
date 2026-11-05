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
