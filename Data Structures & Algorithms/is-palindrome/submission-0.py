class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        reversed_cleaned = "".join(char.lower() for char in s[::-1] if char.isalnum())

        if cleaned == reversed_cleaned:
            return True

        return False