class BrowserHistory:
    class Node():
        def __init__(self, prev, site, forw):
            self.prev = None
            self.cur_site = site
            self.forw = None

    def __init__(self, homepage: str):
        self.head = self.Node(None, homepage, None)

    def visit(self, url: str) -> None:
        new_node = self.Node(None, url, None)
        new_node.prev = self.head
        self.head.forw = new_node
        self.head = new_node

    def back(self, steps: int) -> str:
        temp = self.head
        while steps > 0 and temp.prev:
            temp = temp.prev
            steps -= 1
        self.head = temp
        return temp.cur_site

    def forward(self, steps: int) -> str:
        temp = self.head
        while steps > 0 and temp.forw:
            temp = temp.forw
            steps -= 1
        self.head = temp
        return temp.cur_site


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)