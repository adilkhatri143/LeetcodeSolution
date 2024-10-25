class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        answer = []
        prev = ""
        for path in folder:
            if not prev or not path.startswith(prev + "/"):
                answer.append(path)
                prev = path
        return answer