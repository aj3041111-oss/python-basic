import json

CONFIG_FILE = "config.json"

# Default settings
default_config = {
    "username": "guest",
    "theme": "light",
    "language": "English",
    "notifications": True
}

# Load configuration
def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_config.copy()

# Save configuration
def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

# Display configuration
def display_config(config):
    print("\nCurrent Configuration:")
    for key, value in config.items():
        print(f"{key}: {value}")

# Update setting
def update_config(config):
    key = input("Enter setting to update: ")

    if key in config:
        value = input("Enter new value: ")

        # Convert True/False strings
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False

        config[key] = value
        print("Configuration updated.")
    else:
        print("Setting not found.")

# Main Program
config = load_config()

while True:
    print("\n===== User Configuration Manager =====")
    print("1. View Configuration")
    print("2. Update Configuration")
    print("3. Save Configuration")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_config(config)

    elif choice == "2":
        update_config(config)

    elif choice == "3":
        save_config(config)
        print("Configuration saved.")

    elif choice == "4":
        save_config(config)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")