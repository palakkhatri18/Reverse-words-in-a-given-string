#Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
         words = S.split('.')
         words.reverse()
         result = '.'.join(words)
         return result