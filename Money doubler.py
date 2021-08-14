import math
import matplotlib.pyplot as plt


def main():
    money = money_type()
    n, array = calculations(money)
    output(n)
    graphs(array)


def money_type():
    money_in = input("""Please input the type of money you would like to have double for thirty
                     days (penny, nickel, dime, quarter, one dollar, five dollars, ten dollars, 
                     fifty dollars, one hundred dollars: """)
    money_word = str(money_in)
    if money_word == "penny":
        money = float(0.01)
        return money
    elif money_word == "nickel":
        money = float(0.05)
        return money
    elif money_word == "dime":
        money = float(0.1)
        return money
    elif money_word == "quarter":
        money = float(0.25)
        return money
    elif money_word == "one dollar":
        money = float(1.00)
        return money
    elif money_word == "five dollars":
        money = float(5.00)
        return money
    elif money_word == "ten dollars":
        money = float(10.00)
        return money
    elif money_word == "fifty dollars":
        money = float(50.00)
        return money
    elif money_word == "one hundred dollars":
        money = float(100.00)
        return money


def calculations(money):
    n = float(money)
    array = []
    for i in range(1, 30, 1):
        value = float(n * 2)
        n = float(value)
        array.append(n)
    return n, array


def output(n):
    print("You would have " + str(n) + " dollars after 30 days")


def graphs(array):
    time = []
    for i in range(1, 30, 1):
        time.append(i)
    amount = array

    plt.plot(time, amount)
    plt.xlabel('Time (days)')
    plt.ylabel('Amount (dollars)')
    plt.show()


if __name__ == '__main__':
    main()
