from instagrapi import Client

def login_to_instagram(username, password):
    client = Client()
    client.login(username, password)
    print("!login_to_instagram", client)
    print("!login_to_instagram", username, password)
    return client