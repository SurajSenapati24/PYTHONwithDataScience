import pandas as pd

# Read the CSV file into a Pandas DataFrame
file_name = 'titanic1.csv'

try:
    df = pd.read_csv(file_name)

    # Check if the 'Name' column exists
    if 'Name' in df.columns:
        # Find the passenger with the longest name
        longest_name_row = df.loc[df['Name'].apply(len).idxmax()]
        longest_name = longest_name_row['Name']
        passenger_id = longest_name_row['PassengerId']
        
        # Output the result
        print(f"The passenger with the longest name is {longest_name} (PassengerId: {passenger_id}).")
    else:
        print("Error: 'Name' column not found in the dataset.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"Unexpected error: {e}")
