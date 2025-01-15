import json

def safe_load_json(file_path):
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)  # Deserialize JSON data
        print("JSON data successfully loaded.")
        print("Deserialized Data:", data)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        print("No valid data could be loaded.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON data.")
        print("No valid data could be loaded.")


safe_load_json('data.json')  # Replace with the path to your valid JSON file

