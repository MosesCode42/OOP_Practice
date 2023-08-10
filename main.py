class User:
    def __init__(self, name):
        self.name = name
        # self.id = id
        self.followers = 0
        self.followings = 0
        
    def follow(self, user):
        user.followers +=1
        self.followings +=1
        
user_1 = User("David")
# user_2 = User("Marry", "2")
# user_3 = User("Jenna", "3")
# user_4 = User("Joe", "4")

# user_1.follow(user_2)
# user_2.follow(user_1)
# user_3.follow(user_1)
# user_4.follow(user_1)
# user_4.follow(user_2)



print(user_1.followings)
# print(user_1.followers)
# print(user_2.followings)
# print(user_2.followers)



