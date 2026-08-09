class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1 = []
        d1 = {}
        for i in strs:
            string = str(sorted(i))
            if string in d1:
                d1[string].append(i)
            elif string not in d1:
                d1[string] = [i]
        for j in d1:
            l = list(d1[j])
            l1.append(l)
        return l1

        