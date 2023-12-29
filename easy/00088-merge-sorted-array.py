#https://leetcode.com/problems/merge-sorted-array/description/
                nums1[ins] = nums2[p2]
                p2 -= 1
            else:
        # only need to insert into nums1 from nusm2
        while p2 >= 0:
            if p1 < 0 or nums1[p1] <= nums2[p2]:
        p1,p2,ins = m-1, n-1, m+n-1
                nums1[ins] = nums1[p1]
            ins -= 1
        
                p1 -= 1
        
        # p1,p2,ins = m-1, n-1, m+n-1
        # while ins>=0:
        #     if p1>= 0:
        #         if p2>=0:
        #             if nums1[p1] >= nums2[p2]:
        #                 nums1[ins] = nums1[p1]
        #                 p1 -= 1
        #             else:
        #                 nums1[ins] = nums2[p2]
        #                 p2 -= 1
        #         else:
        #             nums1[ins] = nums1[p1]
        #             p1 -= 1