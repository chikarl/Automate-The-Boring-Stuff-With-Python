def Un(n):
    if n == 0 or n == 1:
        un = 1

    elif n > 1 and n < 10:
        un = 7 * (n-1)

    elif n >= 10:
        un = (2*(n-1))+(3*(n-2))

    return un


with open("uba.txt", "w") as file:
    for n in range(50):
        file.write(f"{str(Un(n))} \n")
