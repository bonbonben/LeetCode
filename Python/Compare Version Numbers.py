# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
# The . character does not represent a decimal point and is used to separate number sequences.
# The default revision number for each level of a version number is 0.

# Input: version1 = "0.1", version2 = "1.1"
# Output: -1

# Input: version1 = "1.0.1", version2 = "1"
# Output: 1

# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1

# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”

# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        print(v1, v2)
        minL = min(len(v1), len(v2))
        for ii in range(minL) :
            if v1[ii] > v2[ii] :
                return 1
            elif v1[ii] < v2[ii] :
                return -1
        
        if len(v1) > len(v2) and sum(v1[minL:]) > 0:
            return 1
        elif len(v1) < len(v2) and sum(v2[minL:]) > 0:
            return -1
        return 0
