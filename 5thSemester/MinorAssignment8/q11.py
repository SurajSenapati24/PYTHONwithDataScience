def calculate_price_per_unit(file_weights, file_prices, output_file):
    try:
        # Read weights from the first file
        with open(file_weights, 'r') as weights_file:
            weights = [float(line.strip()) for line in weights_file]

        # Read prices from the second file
        with open(file_prices, 'r') as prices_file:
            prices = [float(line.strip()) for line in prices_file]

        # Check if both files have equal size
        if len(weights) != len(prices):
            print("Error: The files do not have the same number of lines.")
            return

        # Calculate price per unit weight
        price_per_unit = [price / weight if weight != 0 else 0 for weight, price in zip(weights, prices)]

        # Write the results to the output file
        with open(output_file, 'w') as output:
            for ppu in price_per_unit:
                output.write(f"{ppu:.2f}\n")

        print(f"Price per unit weight has been written to '{output_file}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: One of the files contains invalid data (non-numeric values).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_weights = input("Enter the name of the file containing weights: ").strip()
file_prices = input("Enter the name of the file containing prices: ").strip()
output_file = input("Enter the name of the output file: ").strip()

calculate_price_per_unit(file_weights, file_prices, output_file)
