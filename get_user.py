import requests
def get_user():
    """
    Get user information from randomuser.me

    Returns:
        dict: User information
    """
    data=requests.get("https://randomuser.me/api/").json()
    return data["results"][0]
print(get_user())