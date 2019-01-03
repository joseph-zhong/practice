#!/usr/bin/env python3
"""
Longest Palindromic String
https://leetcode.com/problems/longest-palindromic-substring/
"""

def longestPalindrome(s):
  """ Returns the longest palindromic substring within 's'.

  Approach: Bottom-up dynamic programming.

  We can break down this problem into two parts, first determining whether a substring s[i:j] is a palindrome, and secondly to maximize the length
  of this palindrome.

  - A substring s[i:j] is a palindrome if s[i] == s[j] and s[i+1:j-1] is also a palindrome. Thus all 1-length strings are palindromes,
    and all 2-length strings where each character is the same also is a palindrome.
  - We can compute the longest palindromes from lengths 1 to len(s).
  """
  if len(s) == 0:
    return ''

  opt = dict()
  start = 0
  max_len = 1

  for i in range(len(s)):
    opt[i, i] = True
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      opt[i, i+1] = True
      max_len = 2
      start = i

  for j in range(len(s)):
    for i in range(j-1):
      if (i+1, j-1) in opt and opt[i+1, j-1] and s[i] == s[j]:
        opt[i, j] = True
        if max_len < j-i+1:
          max_len = j-i+1
          start = i
  return s[start:start+max_len]

def longestPalindrome2(s):
  """ Returns the longest palindromic substring within 's'.
  Approach: expansion from palindrome center.

  Rather than maintaining a DP table, we can compute the longest palindrome in place since the left and right sides are the same, expanding from
  the palindrome's center.

  """
  if len(s) <= 1: return s

  def expand(i, j):
    """ Returns the length of the palindrome centered between 'i' and 'j'. """
    while 0 <= i and j < len(s) and s[i] == s[j]:
      i-=1
      j+=1
    return j-i-1

  max_len = 0
  left = 0
  for i in range(len(s)):
    len1 = expand(i, i)
    len2 = expand(i, i+1)
    curr_len = max(len1, len2)
    if curr_len > max_len:
      max_len = curr_len
      if curr_len == len2:
        left = i - (max_len // 2) + 1
      else:
        left = i - (max_len // 2)

  return s[left:left+max_len]

def manacherAlgo(s):
  """
    ???
  """
  if len(s) == 0: return s
  n = 2 * len(s) + 1
  l = [0] * n
  l[0] = 0
  l[1] = 1

  center = 1
  r = 2
  maxLPSLen = 0
  maxLPSCenter = 0

  for i in range(2, n):
    iMirror = 2 * center - i
    l[i] = 0
    diff = r - i
    if diff > 0:
      l[i] = min(l[iMirror], diff)

    try:
      while i + l[i] < n and i - l[i] > 0 \
          and ((i+l[i]+1) % 2 == 0 or s[(i + l[i] + 1)//2] == s[(i - l[i] - 1)//2]):
        l[i] += 1
    except:
      pass

    if l[i] > maxLPSLen:
      maxLPSLen = l[i]
      maxLPSCenter = i

    if i + l[i] > r:
      center = i
      r = i + l[i]
  start = (maxLPSCenter - maxLPSLen) // 2
  end = start + maxLPSLen - 1
  return s[start:end+1]

# print(longestPalindrome("aba") == 'aba')
# print(longestPalindrome("caba") == 'aba')
# print(longestPalindrome("cabac") == 'cabac')
# print(longestPalindrome("abac") == 'aba')

print(longestPalindrome2("aba") == 'aba')
print(longestPalindrome2("caba") == 'aba')
print(longestPalindrome2("cabac") == 'cabac')
print(longestPalindrome2("abac") == 'aba')
print(longestPalindrome2("cbbd") == 'bb')

# print(manacherAlgo('aba'))
# print(manacherAlgo('caba'))
# print(manacherAlgo('cabac'))
# print(manacherAlgo('abac'))