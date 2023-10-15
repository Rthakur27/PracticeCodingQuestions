height = float(input("Enter the height of the cylinder (in cm): "))
radius = float(input("Enter the radius of the cylinder (in cm): "))
pi = 3.14159 
volume = pi * radius**2 * height

cost_per_litre = 40 
total_cost = (volume / 1000) * cost_per_litre 

print(f"Volume of the cylinder: {volume} cubic cm")
print(f"Cost of the milk in the cylinder: Rs. {total_cost}")
