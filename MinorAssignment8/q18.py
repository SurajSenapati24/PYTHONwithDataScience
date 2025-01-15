import csv

def merge_csv_files(file1, file2, output_file):
    try:
        # Read the first file
        with open(file1, 'r') as f1:
            reader1 = list(csv.reader(f1))
            header1 = reader1[0]  # Extract the header
            data1 = reader1[1:]   # Extract the data

        # Read the second file
        with open(file2, 'r') as f2:
            reader2 = list(csv.reader(f2))
            header2 = reader2[0]  # Extract the header
            data2 = reader2[1:]   # Extract the data

        # Ensure headers match
        if header1 != header2:
            print("Error: Headers of the CSV files do not match!")
            return

        # Combine the datasets
        combined_data = [header1] + data1 + data2

        # Write to the output file
        with open(output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerows(combined_data)

        print(f"Successfully merged {file1} and {file2} into {output_file}.")
        
        # Print the combined dataset
        print("\nCombined Dataset:")
        for row in combined_data:
            print(row)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Input file names
file1 = 'titanic1.csv'
file2 = 'titanic2.csv'
output_file = 'combined_titanic.csv'

# Call the function
merge_csv_files(file1, file2, output_file)
