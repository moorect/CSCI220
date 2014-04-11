# sort.py
#    Implementation of selection sort.
#    Author: Zelle (p. 444).

def selSort(nums):
    # sort nums into ascending order
    
    n = len(nums)
    
    # for each position in the list (except the very last)
    for front in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]
        # ("mp" seems to mean "position of the minimum")
        mp = front                     # bottom is smallest initially
        for i in range(front+1,n):     # look at each position
            if nums[i] < nums[mp]:      # this one is smaller
                mp = i                  #   remember its index

        # swap smallest item to the bottom
        temp = nums[mp]
        nums[mp] = nums[front]
        nums[front] = temp


