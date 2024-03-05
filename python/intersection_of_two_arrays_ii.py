class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {}
        nums2_map = {}
        nums3 = []
        
        for i in nums1:
            if i in nums1_map.keys():
                nums1_map[i] = nums1_map[i] + 1
            else:
                nums1_map[i] = 1
        
        for i in nums2:
            if i in nums2_map.keys():
                nums2_map[i] = nums2_map[i] + 1
            else:
                nums2_map[i] = 1
        
        for i in nums1_map.keys():
            if i in nums2_map.keys():
                if nums1_map[i] <= nums2_map[i]:
                    for x in range(0, nums1_map[i]):
                        nums3.append(i)
                else:
                    for x in range(0, nums2_map[i]):
                        nums3.append(i)
                        
        return nums3