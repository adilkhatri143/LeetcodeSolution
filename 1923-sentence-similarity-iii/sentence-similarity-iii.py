class Solution:
    def suffix_search(self, sen_lst, sen_2_lst):
        i = len(sen_lst) - 1
        j = len(sen_2_lst) - 1 
        cnt = temp_cnt = 0
        while i >= 0 and j >= 0:
            if sen_lst[i] == sen_2_lst[j]:
                i -= 1
                cnt += temp_cnt
                temp_cnt = 0
            else:
                temp_cnt = 1
            j -= 1
        if j >= 0:
            cnt += 1
        if i >= 0 or cnt > 1:
            return False
        return True
    
    def prefix_search(self, sen_lst, sen_2_lst):
        i = j = cnt = temp_cnt = 0
        while i < len(sen_lst) and j < len(sen_2_lst):
            if sen_lst[i] == sen_2_lst[j]:
                i += 1
                cnt += temp_cnt
                temp_cnt = 0
            else:
                temp_cnt = 1
            j += 1
        if j < len(sen_2_lst):
            cnt += 1
        if i < len(sen_lst) or cnt > 1:
            return False
        return True
    
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sen_lst = sentence1.split(" ")
        sen_2_lst = sentence2.split(" ")
        if len(sen_lst) < len(sen_2_lst):
            return self.prefix_search(sen_lst, sen_2_lst) or self.suffix_search(sen_lst, sen_2_lst)
        return self.prefix_search(sen_2_lst, sen_lst) or self.suffix_search(sen_2_lst, sen_lst)