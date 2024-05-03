class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Extract the version numbers from both versions
        version1 = [int(x) for x in version1.split(".")] 
        version2 = [int(x) for x in version2.split(".")]
      
        n = len(version1)
        m = len(version2)
        i = 0

        # Compare the version numbers from left to right to determine the largest
        while i < n and i < m:
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
            i += 1

        # Compare the rest of the numbers in version1 to 0, if version1 is longer than version2
        while i < n:
            if version1[i] > 0:
                return 1
            i+=1

        # Compare the rest of the numbers in version2 to 0, if version2 is longer than version1
        while i < m:
            if version2[i] > 0:
                return -1
            i += 1
            
        return 0
