class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.tweetings = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetings[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.followings[userId].add(userId)
        for following in self.followings[userId]:
            if self.tweetings[following]:
                idx = len(self.tweetings[following]) - 1
                time, tweetID = self.tweetings[following][idx] 
                heapq.heappush(heap, [time, tweetID, following, idx - 1]) 

        while heap and len(res) < 10:
            time, tweetID, following, idx = heapq.heappop(heap) 
            res.append(tweetID) 
            if idx >= 0: 
                time, tweetID = self.tweetings[following][idx]
                heapq.heappush(heap, [time, tweetID, following, idx - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)
