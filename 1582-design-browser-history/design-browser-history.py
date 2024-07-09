class BrowserHistory:
    class Node():
        def __init__(self, prev, site, forw):
            self.prev = prev
            self.cur_site = site
            self.forw = forw

    def __init__(self, homepage: str):
        self.head = self.Node(None, homepage, None)

    def visit(self, url: str) -> None:
        new_node = self.Node(self.head, url, None)
        self.head.forw = new_node
        self.head = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.cur_site

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.forw:
            self.head = self.head.forw
            steps -= 1
        return self.head.cur_site


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)