from datetime import datetime
import pytz  # Install via 'pip install pytz' if not already installed

# Data structure: Dictionary of continents, each containing a list of tuples with country names, capitals, and time zones
continents = {
    'Asia': [
        ('Pakistan', 'Islamabad', 'Asia/Karachi'),
        ('Japan', 'Tokyo', 'Asia/Tokyo'),
        ('United Arab Emirates', 'Abu Dhabi', 'Asia/Dubai'),
        ('India', 'New Delhi', 'Asia/Kolkata'),
        ('China', 'Beijing', 'Asia/Shanghai'),
        ('South Korea', 'Seoul', 'Asia/Seoul'),
        ('Saudi Arabia', 'Riyadh', 'Asia/Riyadh'),
        ('Indonesia', 'Jakarta', 'Asia/Jakarta'),
        ('Singapore', 'Singapore', 'Asia/Singapore'),
        ('Thailand', 'Bangkok', 'Asia/Bangkok'),
    ],
    'Europe': [
        ('United Kingdom', 'London', 'Europe/London'),
        ('France', 'Paris', 'Europe/Paris'),
        ('Russia', 'Moscow', 'Europe/Moscow'),
        ('Germany', 'Berlin', 'Europe/Berlin'),
        ('Italy', 'Rome', 'Europe/Rome'),
        ('Spain', 'Madrid', 'Europe/Madrid'),
        ('Netherlands', 'Amsterdam', 'Europe/Amsterdam'),
        ('Switzerland', 'Bern', 'Europe/Zurich'),
        ('Sweden', 'Stockholm', 'Europe/Stockholm'),
        ('Norway', 'Oslo', 'Europe/Oslo'),
    ],
    'North America': [
        ('United States', 'Washington, D.C.', 'America/New_York'),
        ('Canada', 'Ottawa', 'America/Toronto'),
        ('Mexico', 'Mexico City', 'America/Mexico_City'),
        ('Cuba', 'Havana', 'America/Havana'),
        ('Panama', 'Panama City', 'America/Panama'),
    ],
    'South America': [
        ('Brazil', 'Brasília', 'America/Sao_Paulo'),
        ('Argentina', 'Buenos Aires', 'America/Argentina/Buenos_Aires'),
        ('Chile', 'Santiago', 'America/Santiago'),
        ('Colombia', 'Bogotá', 'America/Bogota'),
        ('Peru', 'Lima', 'America/Lima'),
    ],
    'Australia/Oceania': [
        ('Australia', 'Canberra', 'Australia/Sydney'),
        ('New Zealand', 'Wellington', 'Pacific/Auckland'),
        ('Fiji', 'Suva', 'Pacific/Fiji'),
        ('Papua New Guinea', 'Port Moresby', 'Pacific/Port_Moresby'),
        ('Samoa', 'Apia', 'Pacific/Apia'),
    ],
    'Africa': [
        ('Egypt', 'Cairo', 'Africa/Cairo'),
        ('South Africa', 'Pretoria', 'Africa/Johannesburg'),
        ('Nigeria', 'Abuja', 'Africa/Lagos'),
        ('Kenya', 'Nairobi', 'Africa/Nairobi'),
        ('Morocco', 'Rabat', 'Africa/Casablanca'),
    ]
}

# Function to display available continents
def display_continents():
    print("Available Continents:")
    for index, continent in enumerate(continents.keys()):
        print(f"{index + 1}. {continent}")
    print("0. Go Back")
    print("-1. Exit")

# Function to get the continent based on user's choice
def get_continent(choice):
    continent_list = list(continents.keys())
    if choice == 0:
        return 'Go Back'
    elif choice == -1:
        return 'Exit'
    elif 1 <= choice <= len(continent_list):
        return continent_list[choice - 1]
    else:
        print("Invalid choice. Please try again.")
        return None

# Function to display countries in the selected continent
def display_countries(selected_continent):
    print(f"\nAvailable Countries in {selected_continent}:")
    country_list = continents[selected_continent]
    for index, (country, capital, zone) in enumerate(country_list):
        print(f"{index + 1}. {country}")
    print("0. Go Back")
    print("-1. Exit")

# Function to get the country details based on user's choice
def get_country_details(selected_continent, choice):
    country_list = continents[selected_continent]
    if choice == 0:
        return ('Go Back', None, None)
    elif choice == -1:
        return ('Exit', None, None)
    elif 1 <= choice <= len(country_list):
        return country_list[choice - 1]  # Returns a tuple: (country, capital, time_zone)
    else:
        print("Invalid choice. Please try again.")
        return (None, None, None)

# Main function where the program runs
def main():
    print("Welcome to the Global Time Zone Converter!")
    print("-----------------------------------------\n")

    while True:  # Main loop for the entire program
        # Current Location Selection Loop
        while True:
            # Select current continent
            print("Select your current continent:")
            display_continents()
            try:
                current_continent_choice = int(input("Enter the number corresponding to your continent: "))
                current_continent = get_continent(current_continent_choice)
                if current_continent == 'Go Back':
                    continue  # Since we're at the top level, we can just continue
                elif current_continent == 'Exit':
                    print("Exiting the program. Goodbye!")
                    return  # Exit the main function
                elif current_continent:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Current Country Selection Loop
        while True:
            display_countries(current_continent)
            try:
                current_country_choice = int(input("Enter the number corresponding to your country: "))
                current_country, current_capital, current_zone = get_country_details(current_continent, current_country_choice)
                if current_country == 'Go Back':
                    # Go back to continent selection
                    break  # Breaks out of current loop to go back
                elif current_country == 'Exit':
                    print("Exiting the program. Goodbye!")
                    return
                elif current_country:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if current_country == 'Go Back':
            continue  # Go back to continent selection

        # Input current time from user
        while True:
            print("\nEnter your current time.")
            print("Format: HH:MM:SS AM/PM (e.g., 03:30:00 PM)")
            print("Type 'back' to go back or 'exit' to quit.")
            current_time_input = input("Your current time: ")
            if current_time_input.lower() == 'back':
                # Go back to country selection
                break  # Break to go back to the country selection
            elif current_time_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                return
            else:
                # Validate time format
                try:
                    datetime.strptime(current_time_input, '%I:%M:%S %p')
                    break  # Valid time entered
                except ValueError:
                    print("Incorrect time format. Please ensure you follow the specified format.")

        if current_time_input.lower() == 'back':
            continue  # Go back to country selection

        # Target Location Selection Loop
        while True:
            # Select target continent
            print("\nSelect the continent you want to convert the time to:")
            display_continents()
            try:
                target_continent_choice = int(input("Enter the number corresponding to the continent: "))
                target_continent = get_continent(target_continent_choice)
                if target_continent == 'Go Back':
                    # Go back to time input
                    break
                elif target_continent == 'Exit':
                    print("Exiting the program. Goodbye!")
                    return
                elif target_continent:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if target_continent == 'Go Back':
            continue  # Go back to time input

        # Target Country Selection Loop
        while True:
            display_countries(target_continent)
            try:
                target_country_choice = int(input("Enter the number corresponding to the target country: "))
                target_country, target_capital, target_zone = get_country_details(target_continent, target_country_choice)
                if target_country == 'Go Back':
                    # Go back to target continent selection
                    break
                elif target_country == 'Exit':
                    print("Exiting the program. Goodbye!")
                    return
                elif target_country:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if target_country == 'Go Back':
            continue  # Go back to target continent selection

        # Convert time zones
        fmt_input = '%I:%M:%S %p'  # Input time format (12-hour with AM/PM)
        fmt_output = '%I:%M:%S %p'  # Output time format (12-hour with AM/PM)
        try:
            # Combine current date with the input time
            now = datetime.now()
            current_time_str = now.strftime('%Y-%m-%d ') + current_time_input
            # Parse the datetime string to a datetime object
            naive_time = datetime.strptime(current_time_str, '%Y-%m-%d %I:%M:%S %p')

            # Localize the time to the current time zone
            current_tz = pytz.timezone(current_zone)
            localized_time = current_tz.localize(naive_time)

            # Convert to target time zone
            target_tz = pytz.timezone(target_zone)
            target_time = localized_time.astimezone(target_tz)

            # Calculate time difference
            time_difference = target_time.utcoffset() - localized_time.utcoffset()
            hours_difference = int(time_difference.total_seconds() // 3600)
            minutes_difference = int((time_difference.total_seconds() % 3600) // 60)
            difference_str = f"{abs(hours_difference)} hours"
            if minutes_difference > 0:
                difference_str += f" {minutes_difference} minutes"
            if time_difference.total_seconds() > 0:
                difference_str += " ahead"
            elif time_difference.total_seconds() < 0:
                difference_str += " behind"
            else:
                difference_str = "Same time zone"

            # Output the result
            print("\nTime Conversion Result:")
            print(f"Your current time in {current_country}/{current_capital}: {localized_time.strftime(fmt_output)}")
            print(f"The time in {target_country}/{target_capital}: {target_time.strftime(fmt_output)}")
            print(f"Time difference: {difference_str}")

        except Exception as e:
            print("An error occurred during time conversion.")
            print(f"Error details: {e}")

        # After displaying results, ask if the user wants to perform another conversion or exit
        while True:
            print("\nWould you like to perform another time conversion?")
            print("1. Yes")
            print("2. No (Exit)")
            choice = input("Enter 1 or 2: ")
            if choice == '1':
                break  # Restart the main loop
            elif choice == '2':
                print("Thank you for using the Global Time Zone Converter. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()