#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        length = len(path)
        start = 0
        end = start

        # split
        path_list = []
        while start < length:
            while start < length and path[start] == "/":
                start += 1
            end = start + 1
            while end < length and path[end] != "/":
                end += 1

            if start < length:
                path_list.append(path[start: end])
            start = end

        stack = []
        for p in path_list:
            if p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        if stack:
            path = ""
            for p in stack:
                path += f"/{p}"
            return path
        return "/"

    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for p in path:
            if p == "." or not p:
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

# if __name__ == "__main__":
#     s = Solution()
#     print(s.simplifyPath("/.."))
# @lc code=end
