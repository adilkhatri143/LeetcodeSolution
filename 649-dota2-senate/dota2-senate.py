class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire_q = deque()
        radiant_q = deque()
        for i in range(len(senate)):
            if senate[i] == "D":
                dire_q.append(i)
            else:
                radiant_q.append(i)
        i = len(senate)
        while radiant_q and dire_q:
            if radiant_q[0] < dire_q[0]:
                radiant_q.append(i)
            else:
                dire_q.append(i)
            i += 1
            dire_q.popleft()
            radiant_q.popleft()
        if radiant_q:
            return "Radiant"
        return "Dire"