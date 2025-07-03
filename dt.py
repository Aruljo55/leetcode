import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = []  # List of (timestamp, userId, tweetId)
        self.follows = {}  # userId: set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets.append((self.timestamp, userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.follows:
            self.follows[userId] = set()
        self.follows[userId].add(userId)  # Ensure user follows themselves

        res = []
        count = 0

        # Traverse tweets in reverse order (most recent first)
        for time, uid, tid in reversed(self.tweets):
            if uid in self.follows[userId]:
                res.append(tid)
                count += 1
            if count == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # Cannot follow oneself
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId != followerId:
            self.follows[followerId].discard(followeeId)
