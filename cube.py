length=float(input("Enter length of cube: "))
breadth=float(input("Enter breadth of cube: "))
height=float(input("Enter height of cube: "))
volume=length*breadth*height
sa=2*((length*breadth)+(breadth*height)+(length*height))
print("Volume of cube is:",str(volume))
print("Total Surface area of cube is:",str(sa))