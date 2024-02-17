# https://leetcode.com/problems/3sum-closest/
        nums.sort()
        # skip dupes
        i = 0
        while i < len(nums):
            start = i + 1
            end = len(nums) - 1
            # if local diff increases then terminate
            localdiff = float(inf)
            while start < end:
                ns,ne = nums[start], nums[end]
                curdiff = (ns + ne + nums[i]) - target
                if abs(curdiff) >= abs(localdiff):
                    if curdiff >= 0:
                        end -= 1
                    else:
                        start += 1
                else:
                    if curdiff == 0:
                        return target
                    localdiff = curdiff
            if abs(localdiff) < abs(mindiff):
                mindiff = localdiff
            while i < len(nums)- 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return mindiff + target
                
                