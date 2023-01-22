class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
    
        def backtrack(s, ans, candidates, start):
            # 1. check if the goal is fulfilled, 
            # i.e. reaching the end of string in this problem
            if start == len(s):
                # if so, we push `candidates` to ans since we've processed all characters
                ans.append(list(candidates))
                return
            # 2. find all potential candidates
            for i in range(start, len(s)):
                # we want to test all substrings, each substring is a potential candidate
                # e.g. "aab" -> "a", "a", "b", "ab", "aa", "b", "aab"
                candidate = s[start:i+1]
                # 3. check if the current candidate is palindrome or not 
                # if not, then we cannot push to `candidates`
                if not is_palindrome(candidate):
                    continue
                # 4. if so, push it to candidates
                candidates.append(candidate)
                # 5. backtrack with index + 1
                backtrack(s, ans, candidates, i + 1)
                # 6. remove the current substring from `candidates`
                candidates.pop()

        # backtracking 
        # 1. define `ans` to hold `candidates`
        ans = []
        # 2. define `candidates` to hold all potential candidates (palindromic substring)
        candidates = []
        # 3. start backtrack from index 0
        backtrack(s, ans, candidates, 0)
        # 4. return ans
        return ans
