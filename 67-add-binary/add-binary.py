class Solution:
    def addBinary(self, a: str, b: str) -> str:
        iter_a = len(a) - 1
        iter_b = len(b) - 1
        carry = 0
        answer = list()

        while iter_a >= 0 or iter_b >= 0:
            sum_ = carry
            if iter_a >= 0:
                sum_ += int(a[iter_a])
            if iter_b >= 0:
                sum_ += int(b[iter_b])
            answer.append(str(sum_ % 2))
            carry = sum_ // 2
            iter_a -= 1
            iter_b -= 1
        
        if carry:
            answer.append("1")
        
        return "".join(answer)[::-1]