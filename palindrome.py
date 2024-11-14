# https://leetcode.com/problems/palindrome-number/description/


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        length = len(string)
        halflength = length // 2
        for i in range(halflength):
            if string[i] != string[length - i - 1]:
                return False
        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        num_digits = 0
        k = x
        while k != 0:
            k //= 10
            num_digits += 1

        temp = x
        for i in range(num_digits // 2):
            if temp % 10 != (x // 10 ** (num_digits - i - 1)):
                return False
            temp //= 10
            x %= 10 ** (num_digits - i - 1)

        return True


class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            reversed_num = reversed_num * 10 + temp % 10  # got this from someone soln
            temp //= 10

        return reversed_num == x


class Solution4:  # 9ms still depends on load of server which test code
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  # second condition for cases like
            # 10, 100, 1000 as below it will lead to rn = 1 and x = 0
            # which will satisfy the second condition in return
            return False

        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return reversed_num == x or (reversed_num // 10) == x


class Solution5:  # 1ms
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        strx = str(x)
        left = 0
        right = len(strx) - 1

        while left < right:
            if strx[left] != strx[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    test_x = [121, -121, 10]
    test_y = [True, False, False]

    fnc = Solution5()

    calculated = [fnc.isPalindrome(i) for i in test_x]

    print("calculated: ", calculated)
    print("is same: ", calculated == test_y)
