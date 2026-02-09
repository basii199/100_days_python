class User:
    # initialize class with __init__
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f'Initialized {username} ({user_id})')

    def follow_user(self, user):
        self.following += 1
        user.followers += 1

user_1 = User(5, 'Basi')
user_2 = User(8, 'James')

user_2.follow_user(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)