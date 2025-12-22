import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_api_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def process_data(posts):
    processed = []

    for post in posts[:5]:  # limit output
        processed.append({
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        })

    return processed


def save_to_json(data, filename="output.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    posts = fetch_api_data()
    processed_data = process_data(posts)

    print("\n--- API Data Output ---")
    for item in processed_data:
        print(f"\nID: {item['id']}")
        print(f"Title: {item['title']}")

    save_to_json(processed_data)
    print("\n✅ Data saved to output.json")


if __name__ == "__main__":
    main()