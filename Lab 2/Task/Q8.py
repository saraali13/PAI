def currency_conv(amount, prev_currency, new_currency):
    currency_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "PKR": 305.0,
        "INR": 83.0,
        "JPY": 145.0
    }

    if prev_currency in currency_rates and new_currency in currency_rates:
        converted_amount = amount * (currency_rates[new_currency] / currency_rates[prev_currency])
        return converted_amount
    else:
        return "Invalid currency"

amount1 = float(input("Enter the amount: "))
x_currency = input("Enter the from currency (USD, EUR, PKR, INR, JPY): ").upper()
y_currency = input("Enter the to currency (USD, EUR, PKR, INR, JPY): ").upper()
print(f"Converted amount: {currency_conv(amount1, x_currency, y_currency)}")
