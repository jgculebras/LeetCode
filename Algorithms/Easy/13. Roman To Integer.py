class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {
            "I":1,
            "V":5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

        n = len(s)

        cont = 0

        totalNum = 0
        
        while cont < n:
            nextNum = s[cont]
            
            if nextNum not in ["I", "X", "C"] or (cont + 1) >= n:
                totalNum += dict[nextNum]
            else:
                next2Num = s[1+ cont]
                if dict[next2Num] > dict[nextNum]:
                    totalNum += (dict[next2Num] - dict[nextNum])
                    cont += 1
                else:
                    totalNum += dict[nextNum]
            cont+=1

        return totalNum