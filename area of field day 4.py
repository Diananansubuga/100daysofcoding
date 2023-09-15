# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

length=int((input("please enter the lenght of your field in feet: ")))
width=int((input("please enter the width of your field in feet: ")))

area=length*width
acre=(1/43560)*area
print("This is the area of your farm in acres ",acre)