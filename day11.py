#  the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units
# Function to convert MPG to L/100 km
def mpg_to_l100km(mpg):
    # Conversion formula
    l_per_100km = 235.215 / mpg
    return l_per_100km

# Input from the user in MPG
mpg = float(input("Enter fuel efficiency in MPG: "))

# Perform the conversion
l_per_100km = mpg_to_l100km(mpg)

# Display the result
print(f"Equivalent fuel efficiency in L/100 km: {l_per_100km:.2f} L/100 km")
