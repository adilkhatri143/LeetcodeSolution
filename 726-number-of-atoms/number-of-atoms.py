class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = list()
        stack.append(dict())
        n = len(formula)
        i = 0
        while i < n:
            if formula[i] == "(":
                stack.append(dict())
                i += 1
            elif formula[i] == ")":
                curr = stack.pop()
                i += 1
                num_str = ""
                while i < n and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                if num_str:
                    num_mul = int(num_str)
                    for k, v in curr.items():
                        curr[k] = v * num_mul
                for k, v in curr.items():
                    if k in stack[-1]:
                        stack[-1][k] += v
                    else:
                        stack[-1][k] = v
            else:
                str_atom = formula[i]
                i += 1
                while i < n and formula[i].isalpha() and formula[i].islower():
                    str_atom += formula[i]
                    i += 1
                str_atom = str_atom
                str_num = ""
                while i < n and formula[i].isdigit():
                    str_num += formula[i]
                    i += 1
                num = int(str_num) if str_num else 1
                if str_atom in stack[-1]:
                    stack[-1][str_atom] += num
                else:
                    stack[-1][str_atom] = num
        sorted_dict = dict(sorted(stack[-1].items(), key=lambda x:x[0]))
        answer = ""
        for k, v in sorted_dict.items():
            if v == 1:
                answer += k
            else:
                answer += (k + str(v))
        return answer
                