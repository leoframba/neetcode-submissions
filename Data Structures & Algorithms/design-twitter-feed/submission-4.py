import time
class Twitter:
    
    class User:
        def __init__(self, id):
            self.id = id
            self.following = set()
            #self.followers = set()

    
    def __init__(self):
        self.users = {} # id : user
        self.feed = [] # generic feed of all users
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users.setdefault(userId, self.User(userId))
        tweet = (time.time(), tweetId, userId)
        self.feed.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users.setdefault(userId, self.User(userId))
        personal = [tweet for tweet in self.feed if tweet[2] in user.following or tweet[2] == user.id]
        personal = heapq.nlargest(10, personal)
        return [tweet[1] for tweet in personal]

        
    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.setdefault(followerId, self.User(followerId))
        #followee = self.users.setdefault(followeeId, self.User(followeeId))

        follower.following.add(followeeId)
        print(f"{followerId} is following {followeeId}")
        #followee.followers.add(follower)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.setdefault(followerId, self.User(followerId))
        #followee = self.users.setdefault(followeeId, self.User(followeeId))

        if followeeId in follower.following:
            follower.following.remove(followeeId)
        #followee.followers.remove(follower)
        
