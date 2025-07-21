from urllib.parse import parse_qs

class Solution:
    def url_to_dict (self, url:str)->str:

        res = parse_qs (url.split("?")[1])

        return res

url = input ("Enter the url")
sol = Solution()
print (sol.url_to_dict(url))


