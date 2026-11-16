import csv

total_revenue = 0
original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity
            total_revenue += total
            original_count += 1

            print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                cleaned_count += 1

print(f"\nTotal Revenue: ${total_revenue:.2f}")
print(f"Original Rows: {original_count}")
print(f"Cleaned Rows: {cleaned_count}")

#ex6

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nDictReader Total Revenue: ${dict_total_revenue:.2f}")

# csv.reader works well when the column positions are known.
# csv.DictReader is easier when you want to access columns by name.