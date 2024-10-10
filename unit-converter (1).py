def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_conversion_type():
    while True:
        print("\nAvailable conversion types:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        choice = input("Choose conversion type (1-3): ")
        if choice in ['1', '2', '3']:
            return {'1': 'Length', '2': 'Weight', '3': 'Temperature'}[choice]
        print("Invalid choice. Please try again.")

def get_units(conversion_type):
    units = {
        'Length': ['meters', 'feet', 'inches', 'centimeters'],
        'Weight': ['kilograms', 'pounds', 'ounces', 'grams'],
        'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin']
    }
    
    print(f"\nAvailable {conversion_type.lower()} units:")
    for i, unit in enumerate(units[conversion_type], 1):
        print(f"{i}. {unit}")
    
    while True:
        try:
            from_unit = int(input(f"Select initial unit (1-{len(units[conversion_type])}): "))
            to_unit = int(input(f"Select target unit (1-{len(units[conversion_type])}): "))
            if 1 <= from_unit <= len(units[conversion_type]) and 1 <= to_unit <= len(units[conversion_type]):
                return units[conversion_type][from_unit-1], units[conversion_type][to_unit-1]
        except ValueError:
            pass
        print("Invalid selection. Please try again.")

def convert_length(value, from_unit, to_unit):
    # Convert to meters first
    meters = {
        'meters': lambda x: x,
        'feet': lambda x: x * 0.3048,
        'inches': lambda x: x * 0.0254,
        'centimeters': lambda x: x * 0.01
    }[from_unit](value)
    
    # Convert from meters to target unit
    return {
        'meters': lambda x: x,
        'feet': lambda x: x / 0.3048,
        'inches': lambda x: x / 0.0254,
        'centimeters': lambda x: x / 0.01
    }[to_unit](meters)

def convert_weight(value, from_unit, to_unit):
    # Convert to grams first
    grams = {
        'kilograms': lambda x: x * 1000,
        'pounds': lambda x: x * 453.592,
        'ounces': lambda x: x * 28.3495,
        'grams': lambda x: x
    }[from_unit](value)
    
    # Convert from grams to target unit
    return {
        'kilograms': lambda x: x / 1000,
        'pounds': lambda x: x / 453.592,
        'ounces': lambda x: x / 28.3495,
        'grams': lambda x: x
    }[to_unit](grams)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    celsius = {
        'Celsius': lambda x: x,
        'Fahrenheit': lambda x: (x - 32) * 5/9,
        'Kelvin': lambda x: x - 273.15
    }[from_unit](value)
    
    # Convert from Celsius to target unit
    return {
        'Celsius': lambda x: x,
        'Fahrenheit': lambda x: x * 9/5 + 32,
        'Kelvin': lambda x: x + 273.15
    }[to_unit](celsius)

def perform_conversion(value, conversion_type, from_unit, to_unit):
    converters = {
        'Length': convert_length,
        'Weight': convert_weight,
        'Temperature': convert_temperature
    }
    return converters[conversion_type](value, from_unit, to_unit)

def main():
    print("Welcome to the Unit Converter")
    
    while True:
        # Choose conversion type
        conversion_type = get_conversion_type()
        
        # Get initial value and units
        from_unit, to_unit = get_units(conversion_type)
        value = get_numeric_input(f"Enter value in {from_unit}: ")
        
        # Perform conversion and display result
        result = perform_conversion(value, conversion_type, from_unit, to_unit)
        print(f"\nResult: {value} {from_unit} = {result:.4f} {to_unit}")
        
        if input("\nWould you like to perform another conversion? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
