def product_of(numbers_tuple):
    product = 1
    for number in numbers_tuple:
        product = product * number
    return product
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = product_of(numbers)
print("The tuple of numbers is ", numbers)
print("The product is ", result)