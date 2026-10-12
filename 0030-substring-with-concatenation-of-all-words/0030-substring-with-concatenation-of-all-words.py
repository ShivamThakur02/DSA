class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq_count = {}
        for i in words:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1
                
        result = []
        word_len = len(words[0])
        
        for i in range(word_len):
            l = i 
            temp_count = {}
            count = 0
            
            for j in range(i, len(s) - word_len + 1, word_len):
                sub_word = s[j:j + word_len]
                
                if sub_word in freq_count:
                    if sub_word in temp_count:
                        temp_count[sub_word] += 1
                    else:
                        temp_count[sub_word] = 1
                    count += 1

                    while temp_count[sub_word] > freq_count[sub_word]:
                        left_word = s[l:l + word_len]
                        temp_count[left_word] -= 1
                        count -= 1
                        l += word_len
                        
                    if count == len(words):
                        result.append(l)
                else:
                    temp_count.clear()
                    count = 0
                    l = j + word_len
                    
        return result

                

        