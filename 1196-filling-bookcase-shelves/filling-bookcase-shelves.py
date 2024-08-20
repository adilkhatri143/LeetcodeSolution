class Solution:
    og_shelfWidth = None
    def solve(self, idx, books, shelfWidth, cur_height, dp):
        if idx == len(books):
            return cur_height
        
        if (idx, shelfWidth, cur_height) in dp:
            return dp[(idx, shelfWidth, cur_height)]

        ans1 = self.solve(idx + 1, books, shelfWidth - books[idx][0], max(cur_height, books[idx][1]), dp) if books[idx][0] <= shelfWidth else float("inf")
        ans2 = self.solve(idx + 1, books, self.og_shelfWidth - books[idx][0], books[idx][1], dp) + cur_height

        dp[(idx, shelfWidth, cur_height)] = min(ans1, ans2)
        return dp[(idx, shelfWidth, cur_height)]

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.og_shelfWidth = shelfWidth
        return self.solve(0, books, shelfWidth, 0, dict())