class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        st = list()
        for start, end in intervals:
            if st and st[-1][1] >= end:
                continue
            elif st and st[-1][1] >= start:
                st[-1][1] = end
                continue
            st.append([start, end])
        return st