#how do we implement an array-reverse function in-place?

def reverse(arr):
    #this doesnt work because under the hood slicing creates a copy of the input array
    # return arr[::-1]

    #use a two-pointer technique
    #swap indices on each new interation

    left = 0
    right = len(arr) - 1

    #how do we interate
    #iterate so long as left is less than right
    #what if there's an odd number of elements in the arr?
    #we'd have a case where `left` and `right` would land on middle element
    while left < right:
      #this uses an extra `temp` variable under the hood
      arr[left], arr[right] = arr[right], arr[left]
      #increment the left pointer
      #decrement the right pointer
      left += 1
      right -= 1

    return arr
    

##Typescript

# function reverse(arr: number[]): number[]{
#   let left = 0;
#   let right = arr.length - 1;

#   while (left < right){
#     [arr[left], arr[right]] = [arr[right], arr[left]];
#     left ++;
#     right --;
#   }
#   return arr
# }