
#promp for the lenght of the angle
a = float(input( "enter lenght of side a"))
b = float(input( "enter lenght of side b"))
c = float(input( "enter lenght of side c"))
#calculate the semi-premiter
s = (a+ b+ + c) / 2
#calculate using Heron formular
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# output the result
print(f"The area of the triangle is {area:.2f}")