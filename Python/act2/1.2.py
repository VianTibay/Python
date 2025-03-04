import csv

rates = {}
with open('C:/Users/96597/Documents/FEU tech files/2-year/intgrative prog and tech/Python/Python/act2/currency.csv', mode='r', newline='', encoding='utf-8', errors='replace') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        try:
            rates[row[0].upper()] = float(row[1])  # Convert to float
        except ValueError:
            print(f"Skipping invalid row: {row}")  # Debugging output

usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").upper()
converted_amount = usd_amount * rates.get(target_currency, 0)

print(f"\nDollar: {usd_amount} USD")
if converted_amount:
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found in the exchange rates.")
