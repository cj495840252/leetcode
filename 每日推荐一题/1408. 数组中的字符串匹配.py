"""
1408. 数组中的字符串匹配
给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。

如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。

"""

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        sets = set()
        for i in range(len(words)):
            for j in range(len(words)):
                # if words[i] in words[j]:
                #     sets.add(words[i])
                if words[i] in words[j] and i != j:
                    sets.add(words[i])
        return list(sets)

if __name__ == '__main__':
    words = ["mass", "as", "hero", "superhero"]
    s = Solution().stringMatching(words)
    print(s)