from collections import Counter

def valid_anagrams1(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


def valid_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

def valid_anagrams3(s1, s2):
    if len(s1) != len(s2):
        return False
    
    return sorted(s1) == sorted(s2)

print(valid_anagrams3("garden", "danger"))