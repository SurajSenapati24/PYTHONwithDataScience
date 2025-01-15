import pandas as pd

# Read the Titanic dataset
file_name = 'titanic.csv'

try:
    # Load the CSV data into a DataFrame
    df = pd.read_csv(file_name)

    # Display the distribution of ticket prices (Fare)
    print("Ticket price distribution:")
    print(df['Fare'].describe())  # This provides basic statistics (min, max, mean, etc.) of ticket prices

    # Filter passengers who were under 18 years old
    under_18_passengers = df[df['Age'] < 18]

    # Display the names of passengers under 18 years old
    print("\nPassengers under 18 years old:")
    print(under_18_passengers['Name'])

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"Unexpected error: {e}")
