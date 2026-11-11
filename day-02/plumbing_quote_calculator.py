# TODO 1: Print "Welcome to the Plumbing Job Quote Calculator".

# TODO 2: Ask how many hours were worked, and save it as a float.

# TODO 3: Ask for the hourly rate and the total cost of materials. Put a $ in each prompt, and save both as floats.

# TODO 4: Ask for the sales tax percent, and save that as a float too.

# TODO 5: Labor is hours times the hourly rate. Round it to 2 decimal places.

# TODO 6: Taxed materials are the material cost times (sales tax / 100 + 1). Round that to 2 decimal places.

# TODO 7: The quote total is labor plus taxed materials. Round it to 2 decimal places.

# TODO 8: Print "Your quote is:" then Labor, Materials (with tax), and Total cost, each on its own line,
#   as dollars and cents (two digits after the decimal).

print("Welcome to the Plumbing Job Quote Calculator")
hours_worked = float(input("How many hours did you work? "))
hourly_rate = float(input("What is your hourly rate? $"))
cost_of_materials = float(input("What was the total cost of materials? $"))
sales_tax = float(input("What is the sales tax %? "))
labor = round(hours_worked * hourly_rate, 2)
materials = round(cost_of_materials * (sales_tax / 100 + 1), 2)
total_quote = round(labor + materials, 2)
print(f"Your quote is:\nLabor: ${labor:.2f}\nMaterials (with tax): ${materials:.2f}\nTotal cost: ${total_quote:.2f}")
