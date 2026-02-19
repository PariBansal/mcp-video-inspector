# src/user_interface.py

def get_user_preference(features: dict) -> dict:
    print("\n=== Extracted Features ===")
    for key, value in features.items():
        print(f"{key.title()}: {value}\n")

    print("Select the features you want to include in the Adobe Illustrator output:")
    selected = {}
    for key in features:
        choice = input(f"Include {key}? (yes/no): ").strip().lower()
        if choice == "yes":
            selected[key] = features[key]

    return selected

