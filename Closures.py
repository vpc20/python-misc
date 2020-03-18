def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


mult6 = make_multiplier(6)
mult7 = make_multiplier(7)

print(mult6(7))  # prints 42
print(mult7(6))  # prints 42
