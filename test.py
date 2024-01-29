def longestPrefix(strs: [str]):
    prefix = strs[0]

    for word in strs[1:]:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ''
            
    print(prefix)
longestPrefix(["flower","flow","floght",'flooo'])