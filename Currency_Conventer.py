USD = 42.0  # 1 USD = 42.0 TRY
EUR = 45.0  # 1 EUR = 45.0 TRY
GBP = 50.0  # 1 GBP = 50.0 TRY

print("Welcome to the Currency Converter!")
print("Available currencies: USD, EUR, GBP")

currency_from = input("Enter the currency you want to convert from (USD, EUR, GBP): ").upper()
amount = input("Enter how much you want to convert: ")

## try hata almamak için

try:
    amount_value = float(amount)
except ValueError:
    print("Invalid amount entered.")
else:
    if currency_from == "USD":
        converted_amount = amount_value * USD
        print(f"{amount_value} USD is equal to {converted_amount} TRY")
    elif currency_from == "EUR":
        converted_amount = amount_value * EUR
        print(f"{amount_value} EUR is equal to {converted_amount} TRY")
    elif currency_from == "GBP":
        converted_amount = amount_value * GBP
        print(f"{amount_value} GBP is equal to {converted_amount} TRY")
    else:
        print("Invalid currency selected.")