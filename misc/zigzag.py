class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        strs = [""] * numRows
        #for k in range(numRows):
            #strs.append("")
        j = 0
        dir = True # dir is going down
        for i in range(len(s)):
            #print j
            #print strs[j]
            #print strs[j]
            strs[j] = strs[j] + s[i]
            if numRows > 1:
                if j is numRows - 1:
                    dir = False # going up
                elif j is 0:
                    dir = True
                if dir:
                    j += 1
                else: 
                    j -= 1
        newstr = ""
        '''
        for k in range(numRows):
            newstr += strs[k]
        return newstr
        '''
        print newstr.join(strs)
s = Solution()
s.convert("hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx", 503) # should return "PAHNAPLSIIGYIR"