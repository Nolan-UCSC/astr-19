import math #I used inport math to get the math functions I think that should be fine

pi = math.pi

def table(num_entries):
    #writes out a table
    table1 = []
    for i in range(num_entries):
        x = i * (2 * pi) / (num_entries - 1)  # Generate x values between 0 and 2pi
        sin_x = math.sin(x)  # find sin(x)
        table1.append((x, sin_x))
    return table1


def main():
    #thousand entries
    num_entries = 1000
    sin_table = table(num_entries)
    # Print the table values
    for x, sin_x in sin_table:
        print(f"{x}\t {sin_x}")

if __name__ == "__main__":
    main()
