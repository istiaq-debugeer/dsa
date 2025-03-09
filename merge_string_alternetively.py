def marge_string(word1, word2):
    result = ""
    for i in range(max(len(word1), len(word2))):
        print(i)
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    print(result)


marge_string("abc", "defg")


# better solution
def mergeAlternately(word1: str, word2: str) -> str:
    res = ""
    l = min(len(word1), len(word2))
    for i in range(l):
        res += word1[i] + word2[i]
    print(res + word1[l:] + word2[l:])


mergeAlternately("abc", "pqrs")
