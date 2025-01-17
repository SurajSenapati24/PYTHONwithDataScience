try:
    # Input for numerator and denominator
    numerator = input("Enter the numerator: ").strip()
    denominator = input("Enter the denominator: ").strip()
    
    # Convert inputs to floats
    num = float(numerator)
    den = float(denominator)

        
        
    
    # Perform the division
    result = num / den
    print(f"Result: {result:.2f}")

except ValueError:
    # Handle non-numeric inputs
    print("Error: Please enter valid numeric values.")
# Run the safe divide function
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

