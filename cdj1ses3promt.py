#Write a Python program that defines a function f(x) that returns x**3 + 8.
def f(x):
    return x ** 3 + 8

#in the main function
def main():
    #call f(x)
    x = 9
    #with x = 9
    result = f(x)
    #and print the result
    print("f(9) =", result)
    #if the result is larger than 27
    if result > 27:
        #prints “YAY!”
        print("YAY!")


if __name__ == "__main__":
    main()
