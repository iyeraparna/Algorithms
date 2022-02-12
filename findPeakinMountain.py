def binarySearch(start,end,target,nums):
    while start <= end:
        mid = (start+end)//2
        midVal = nums[mid]

        if start == end:
            return nums[start]

        #climbing mountain
        elif nums[mid]< nums[mid+1]:
            start = mid + 1
        
        #going down the mountain
        elif nums[mid] > nums[mid+1]:
            end = mid

if __name__ == "__main__":
    nums = [2,3,4,5,6,7,8,9,10,28,30,45,55,67,78,89]
    start = 0
    end = len(nums)
    print(binarySearch(start,end,nums))