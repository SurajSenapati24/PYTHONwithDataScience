import re

def extract_unique_emails(input_file, output_file):
    try:
        # Open and read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Regular expression to match email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com'
        
        # Extract all email addresses
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates by converting to a seta
        unique_emails = sorted(set(emails))  # Sort the emails for better readability
        
        # Write unique email addresses to the output file
        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')
        
        print(f"Unique email addresses have been saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = 'sample.txt'  # Replace with the path to your input file
output_file = 'output.txt'  # Replace with the desired output file name

extract_unique_emails(input_file, output_file)
