# def calculate_discount(price, percentage):
#     if percentage < 0:
#         raise ValueError('negative discount not allowed')
#     if percentage > 100:
#         raise ValueError('discount too large')
#
#     return price - (price * percentage / 100)

def calculate_discount(price: float, percentage: float) -> float:
    """
    Calculate the discount based on price and percentage

    :param price: original price, must be non-negative
    :param percentage: discount in range [0, 100]
    :return: amount of discounted price
    """
    if not (0 <= percentage <= 100):
        raise ValueError('percentage must be between 0 and 100')

    return price * (1 - percentage / 100)
