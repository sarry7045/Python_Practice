import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")


def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        jokes = data["data"]
        # print(jokes)
        random_jokes = jokes["data"]["content"]
        return random_jokes
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        random_jokes = fetch_random_jokes()
        print(f"Username: {username} \nCountry: {country}")
        print(f"Jokes: {random_jokes}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()