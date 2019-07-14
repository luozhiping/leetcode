# 468. 验证IP地址
# https://leetcode-cn.com/problems/validate-ip-address/

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        alpha = ["a", "b", "c", "d", "e", "f"]
        if "." in IP:
            parts = IP.split(".")
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if part.isdigit() and 0 <= int(part) <= 255:
                    if 100 > int(part) > 0 and part[0] == "0":
                        return "Neither"
                    if int(part) == 0 and len(part) > 1:
                        return "Neither"
                    continue
                return "Neither"
            return "IPv4"
        elif ":" in IP:
            parts = IP.split(":")
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"
                for c in part:
                    if c.isdigit():
                        continue
                    if c.isalpha() and c.lower() in alpha:
                        continue
                    return "Neither"
                # if int(part) <= 255
            return "IPv6"
        return "Neither"

s = Solution()
# print("1".isdigit())
print(s.validIPAddress("172.16.254.1"))
print(s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))