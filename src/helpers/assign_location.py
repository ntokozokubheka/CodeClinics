from src.helpers.utils import print_yellow, print_red


def get_location():
    campus_venues = {
        "Jhb main": ["4-Robotics Lab (2)", "4-Robotics Lab (1)", "5-Open Area"],
        "Jhb cjc": ["Venue 1B", "Venue 2B", "Venue 3B"],
        "Dbn": ["Venue 1C", "Venue 2C", "Venue 3C"],
        "Cpt": ["Venue 1D", "Venue 2D", "Venue 3D"]
    }

    while True:
        print_yellow("Choose a location:")
        print_yellow("1. Johannesburg main")
        print_yellow("2. Johannesburg park town")
        print_yellow("3. Durban")
        print_yellow("4. Cape town")
        print_yellow("5. Online")

        location_choice = input("\033[94mEnter your choice (1-5): \033[0m")

        if location_choice in ['1', '2', '3', '4']:
            campus_name = ["Jhb main", "Jhb cjc", "Dbn",
                           "Cpt"][int(location_choice) - 1]
            venues = campus_venues[campus_name]

            print(f"Choose a venue for {campus_name}:")
            for idx, venue in enumerate(venues, start=1):
                print(f"{idx}. {venue}")

            venue_choice = input("\033[94mEnter your choice (1-3): \033[0m")

            if venue_choice in ['1', '2', '3']:
                selected_venue = venues[int(venue_choice) - 1]
                return f"{campus_name}, {selected_venue}"
            else:
                print_red("Invalid venue choice. Please try again.")
        elif location_choice == '5':
            return "Online"
        else:
            print_red("Invalid location choice. Please try again.")
