from collections import Counter


def find_all_anagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter()

    for i, char in enumerate(s):
        s_count[char] += 1

        if i >= len(p):
            left_char = s[i - len(p)]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result