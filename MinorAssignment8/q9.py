def safe_divide():
    try:
        # Input for numerator and denominator
        numerator = input("Enter the numerator: ").strip()
        denominator = input("Enter the denominator: ").strip()
        
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            print("Error: Division by zero is not allowed.")
            return
        
        # Perform the division
        result = num / den
        print(f"Result: {result:.2f}")
    
    except ValueError:
        # Handle non-numeric inputs
        print("Error: Please enter valid numeric values.")

# Run the safe divide function
safe_divide()
