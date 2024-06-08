print("Half Pyramid")
n=int(input("Enter the number to print pyramid ::"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")