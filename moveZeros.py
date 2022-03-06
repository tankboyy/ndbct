def moveZeroes(nums):
    wIdx = 0
    for idx in range(0, len(nums)):
        if nums[idx] != 0:
            nums[wIdx] = nums[idx]
            wIdx += 1
    for i in range(wIdx, len(nums)):
        nums[i] = 0
        
    return nums


print(moveZeroes([3,0,1,2,4,6,1,2,0,0,0,1,2,3,5,1,0,4,3]))