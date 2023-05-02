def groupAnagrams(strs):
    ans = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
    return ans.values()
