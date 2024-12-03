"""
Blackjack
Chef is playing a variant of Blackjack, where 3 numbers are drawn and each number lies between 1 and 10 (with both 1 and 10 inclusive). 
Chef wins the game when the sum of these 3 numbers is exactly 21.
Given the first two numbers A and B, that have been drawn by Chef, what should be 3-rd number that should be drawn by the Chef in order to win the game?

Note that it is possible that Chef cannot win the game, no matter what is the 3-rd number. In such cases, report -1 as the answer.
"""
#https://codechef.com/practice/course/logical-problems/DIFF800/problems/BLACKJACK?tab=statement

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    C = 21- (A+B)
    if C <= 10:
        print(C)
    else:
        print(-1)
