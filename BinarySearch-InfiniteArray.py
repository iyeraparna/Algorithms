def findingRange(nums,target):
    #first find the range
    #start with size = 2
    start = 0
    end = 1
    sizeofBox = 2

    #condition for target to be in the range
    #target<=endValue
    #keep doubling size while target>endValue
    #once you find target<=end -> start binarSearch
    while target>nums[end]:
        start = end + 1
        sizeofBox = sizeofBox*2
        end = end + sizeofBox*2

    return binarySearch(start,end,target,nums)


def binarySearch(start,end,target,nums):
    while start <= end:
        mid = (start+end)//2
        midVal = nums[mid]

        if midVal == target:
            return mid

        elif midVal<=target:
            start = mid + 1
            
        elif midVal>target:
            end = mid - 1
    return -1


if __name__ == "__main__":
    nums = [2,3,4,5,6,7,8,9,10,28,30,45,55,67,78,89]
    
    target = 17
    print(findingRange(nums,target))