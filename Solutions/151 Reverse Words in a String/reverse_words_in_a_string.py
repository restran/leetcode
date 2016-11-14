# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_list = [t for t in s.split(' ') if t != '']
        return ' '.join(s_list[::-1])
