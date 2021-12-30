from time import time


def sumOfN(number):
    if number == 0:
        return 0
    return number + sumOfN(number - 1)


def factorialOfN(number):
    if number == 0:
        return 1
    return number * factorialOfN(number - 1)


if __name__ == '__main__':
    currentTime = time()
    for i in range(500):
        x = sumOfN(i)
        # print(f"Sum of first {i} Numbers is = {x}")

    print(f"Sum Function Executed in {time() - currentTime} s")

    currentTime = time()
    for i in range(500):
        x = factorialOfN(i)
        # print(f"Factorial of first {i} Numbers is = {x}")

    print(f"Factorial Function Executed in {time() - currentTime} s")
