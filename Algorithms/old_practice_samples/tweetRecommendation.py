'''
Function to generate recommended tweets
'''

def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    userFollows = set(map(lambda x: x[1], filter(lambda x: x[0] == targetUser, followGraph_edges)))
    tweets = {}
    for tw in likeGraph_edges:
        if tw[0] in userFollows:
            tweets[tw[1]] = tweets.get(tw[1], 0) + 1
    print tweets
    re = sorted(filter(lambda x: tweets[x] >= minLikeThreshold, tweets.keys()), key = lambda x: tweets[x], reverse=True)
    return re



if __name__ == '__main__':
    A, B, C, D, E = 'A', 'B', 'C', 'D', 'E'
    T1, T2, T4, T6 = 'T1', 'T2', 'T4', 'T6'
    followGraph_edges = [(A,B), (A,C), (B,C), (A, D), (A, E)]
    likeGraph = [(A, T1), (B, T2), (A, T2), (C, T1), (B, T1), (E, T4), (D, T4), (E, T6), (B, T4)]
    print getRecommendedTweets(followGraph_edges, likeGraph, 'A', 2)
