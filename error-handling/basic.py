def division(x, y):
    return x / y


if __name__ == "__main__":
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))

    result = 0
    # case 1
    # try:
    #     result = division(x, y)
    # except:
    #     print("got exception")

    # case 2
    try:
        result = division(x, y)
    except Exception as e:
        result = -1
        print(" >>> got exception: ", e)
    else:
        print(" >>> There are no error")
    finally:
        print(" >>> This is finally block")

    print(f"result of {x}/{y} is", result)
