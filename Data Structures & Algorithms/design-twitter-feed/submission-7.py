import heapq
class Twitter:
    class User:
        def __init__(self, id):
            self.id = id
            self.following = set()
            self.tweets = []

    
    def __init__(self):
        self.users = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create / get user
        user = self.users.setdefault(userId, self.User(userId))

        # create tweet
        tweet = (self.time, tweetId, userId)
        self.time += 1

        user.tweets.append(tweet)
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        # get user
        user = self.users[userId]

        feed = user.tweets[:]
        # build feed - 10 most recent
        for fid in user.following:
            f = self.users[fid]
            feed += f.tweets
        
        return [t[1] for t in heapq.nlargest(10, feed)]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: 
            return
        follower = self.users.setdefault(followerId, self.User(followerId))
        follower.following.add(followeeId)
        return

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.setdefault(followerId, self.User(followerId))
        if followeeId in follower.following:
            follower.following.remove(followeeId)
        return
        
        
