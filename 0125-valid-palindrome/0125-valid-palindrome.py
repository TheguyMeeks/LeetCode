class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        st = "".join(st.split())
        left = 0
        right = len(st) - 1

        while left <= right:
            leftchar = st[left]
            rightchar = st[right]
            while not leftchar.isalnum() and left + 1 <= right:
                left += 1
                leftchar = st[left]
            while not rightchar.isalnum() and right - 1 >= left:
                right -= 1
                rightchar = st[right]

            if leftchar != st[right]:
                return False
            elif leftchar == rightchar:
                left += 1
                right -= 1
        return True

