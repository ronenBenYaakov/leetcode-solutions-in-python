class Solution(object):
    def frequencySort(self, s):
        freq, n, mxFreq = {}, len(s), 0

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        chars = list(s)

        chars.sort(key=lambda x: (-freq[x], x))

        return "".join(chars)
