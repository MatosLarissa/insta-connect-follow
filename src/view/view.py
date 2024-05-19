from flask import send_from_directory, request
from src.controller.connect_and_follow import connect_and_follow

def submit():
    if request.method == 'POST':
        instagram_username = request.form['username']
        instagram_password = request.form['password']
        accounts_to_follow = request.form['accounts'].split(",")
        print("requests: ", instagram_username,instagram_username,instagram_username)
        connect_and_follow(instagram_username, instagram_password, accounts_to_follow)

    return send_from_directory('src/view/', 'index.html')
