class Solution1:
    def romanToInt(self, s: str) -> int:
        num = 0
        prev_sym = None

        for sym in s:
            if sym == "I":
                num += 1
                prev_sym = "I"
            elif sym == "V":
                if prev_sym == "I":
                    num += 3
                else:
                    num += 5
                prev_sym = "V"
            elif sym == "X":
                if prev_sym == "I":
                    num += 8
                else:
                    num += 10
                prev_sym = "X"
            elif sym == "L":
                if prev_sym == "X":
                    num += 30
                else:
                    num += 50
                prev_sym = "L"
            elif sym == "C":
                if prev_sym == "X":
                    num += 80
                else:
                    num += 100
                prev_sym = "C"
            elif sym == "D":
                if prev_sym == "C":
                    num += 300
                else:
                    num += 500
                prev_sym = "D"
            elif sym == "M":
                if prev_sym == "C":
                    num += 800
                else:
                    num += 1000
                prev_sym = "M"

        return num


syms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution2:
    def romanToInt(self, s: str) -> int:
        num = 0
        prev = None
        symbs = {
            None: {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000},
            "I": {"I": 1, "V": 3, "X": 8},
            "V": {"I": 1, "V": 5},
            "X": {"I": 1, "V": 5, "X": 10, "L": 30, "C": 80},
            "L": {"I": 1, "V": 5, "X": 10, "L": 50},
            "C": {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 300, "M": 800},
            "D": {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500},
            "M": {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000},
        }

        for sym in s:
            num += symbs[prev][sym]
            prev = sym

        return num


class Solution3:  # got from someone else, and it makes sense to change input
    # in a way such that it works for normal mode without adding strings
    def romanToInt(self, s: str) -> int:
        syms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for sym in s:
            num += syms[sym]

        return num


if __name__ == "__main__":
    x = ["III", "LVIII", "MCMXCIV"]
    y = [3, 58, 1994]
    fnc = Solution3()
    preds = [fnc.romanToInt(s) for s in x]
    print(preds)
    print(preds == y)
