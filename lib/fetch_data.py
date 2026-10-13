import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_data():
    """Return the post as a dict, or {} if the request fails."""
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.RequestException:
        return {}
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
