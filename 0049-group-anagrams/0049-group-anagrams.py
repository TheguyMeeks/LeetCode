class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = defaultdict(list) # default value of a key that doesn't exist yet is an empty list

        # for every word in the list, sort it then append it to the corresponding list
        # this works because there's only ever two cases, the sorted key exists or it doesn't
        # if key already exists, I just add whatever word that rearranges to it to it's list of values
        # if the key did not already exist, its a brand new word with no anagrams and I can just create a new sorted key for it and add the unsorted word as the first item in it's list of values
        for string in strs:
            sorted_str = "".join(sorted(string))
            map[sorted_str].append(string)

        return list(map.values())

