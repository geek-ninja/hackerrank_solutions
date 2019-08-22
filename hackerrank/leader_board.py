#Climbing Leader Board

def climbingLeaderboard(scores, alices):
    unique_scores = list(reversed(sorted(set(scores))))
    i = len(alices)-1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(scores) or scores[j] <= alices[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1

    for i in (reversed(ans)):
        print(i)
n=int(input())
leaders=list(set(list(map(int,input().split()))))
leaders.sort()
leaders.reverse()
m=int(input())
alice_score=list(map(int,input().split()))
(climbingLeaderboard(leaders,alice_score))
