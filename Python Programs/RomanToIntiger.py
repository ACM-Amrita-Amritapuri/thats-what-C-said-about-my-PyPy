class Convert:
    def romanToInt(self, s: str) -> int:
        Roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        l = len(s)
        value = 0
        for i in range(l):
            value += Roman[s[i]]
            if i < l-3:
                if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3] :
                    return "Invalid Input"
            if i < l-1:
                if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                    value -= 2*Roman[s[i]]
                if s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                    value -= 2*Roman[s[i]]
                if s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                    value -= 2*Roman[s[i]]
        return value
