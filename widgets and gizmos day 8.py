# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.
widgets=20
gizmos=112
num_widgets=int(input("please write the number of widgets: "))
num_Gizmos=int(input("please write the number of Gizmos: "))

total_widgets=widgets*num_widgets
total_gizmos=gizmos*num_Gizmos

total=total_gizmos+total_widgets
print(total)