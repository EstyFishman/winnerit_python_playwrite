
def calculate_discount(price, discount_percent):
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount_percent must be non-negative")
    else:
        return price * (1 - discount_percent / 100)
