import requests

POST_API_URL = "https://api.reddit.com/api/info/?id=t3_mejfeu"
FILENAME = "VACCINES.md"


def get(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    try:
        return requests.get(url, headers=headers).json()
    except:
        return {}


def main():
    data = get(POST_API_URL)
    post_contents = data["data"]["children"][0]["data"]["selftext"]
    if data and post_contents:
        with open(FILENAME, "w") as f:
            f.write(post_contents)


if __name__ == "__main__":
    main()