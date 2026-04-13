class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1 = {}
        #hash map of frequecies of characters in s1
        for c in s1:
                count1[c] = 1 + count1.get(c,0)

        need = len(count1) #number of unique characters that must full match


        for i in range(len(s2)):        #trying every character
                count2, cur = {}, 0
                for j in range(i, len(s2)): #expand range of window 
                        #add current character to window's frequency map
                        count2[s2[j]] = count2.get(s2[j], 0) + 1

                        if count1.get(s2[j], 0) < count2[s2[j]]:
                                break
                        if count1.get(s2[j], 0) == count2[s2[j]]:
                                cur+=1
                        if cur ==  need:
                                return True
        return False

                        

        