#this is for prompt 2 of code journal 1
#print the sum of two floating point numbers
#print the diffrence between two intergers
#the product of a floating point number and an interger
#each one should print out the data type of the resulting answer

#print the sume of two floating point numbers
def part1():
    floatingnumber = 3.141592
    floatingnumber2 = 5.102023
    print("Sum of two floating point numbers,", floatingnumber, "+", floatingnumber2,"=", floatingnumber + floatingnumber2)
    print("The data type for the sum of two floating point numbers is:", type(floatingnumber + floatingnumber2))

#prints the difference between the two ints
def part2():
    int1 = 5
    int2 = 10
    print("The Difference between two intergers,", int1,"+", int2, "=", int1 - int2)
    print("The data type for the diffrence between two intergers is:", type(int1 - int2))

#the product of a floating point number and an interger
def part3():
    floatingnumber = 6.242003
    int1 = 5
    print("The product of a floating point number and an interger,",floatingnumber, "+", int1, "=", floatingnumber * int1)
    print("The data type for the product of a floating point number and an interger is:", type(floatingnumber * int1))

#runs all the above funcitons
def main():
    part1()
    part2()
    part3()

#run the main
if __name__ == "__main__":
    main()