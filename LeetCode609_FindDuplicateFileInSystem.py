import collections, os


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        """
        Input:
        ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
        Output:  
        [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        """

        ans = collections.defaultdict(list)

        for path in paths:
            temp = path.split(" ")
            for item in temp[1:]:

                eachFile = item.split("(")
                filename = eachFile[0]
                key = eachFile[1]
                ans[key[:-1]].append(os.path.join(temp[0], filename)) # be OS independent, instead using temp[0] +
                # "/" + filename

        result = []


        for key in ans:
            if len(ans[key])>1:
                result.append(ans[key])

        return result


test = Solution()
print(test.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))

