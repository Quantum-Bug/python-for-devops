import requests
import json


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        return []


def process_users(users):
    processed = []
    for user in users:
        processed.append({
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city")
        })
    return processed


def save_to_file(data):
    try:
        with open("day-03/output.json", "w") as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print("File write error:", error)


def main():
    users = fetch_users()
    if not users:
        print("No data received. Exiting safely.")
        return

    processed_data = process_users(users)
    save_to_file(processed_data)

    print("Processed User Data:")
    for user in processed_data:
        print(user)


if __name__ == "__main__":
    main()
