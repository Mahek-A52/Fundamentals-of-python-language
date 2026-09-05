def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers} followers")


friends = {
    "rahul": "2.3K",
    "priya": "5.1K",
    "amit": "1.8K"
}

display_friends(friends)
