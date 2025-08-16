def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is less than 20%, no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {final_price:.2f}")
