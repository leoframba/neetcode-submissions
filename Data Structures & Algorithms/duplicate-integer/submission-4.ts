class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const numSet = new Set<number>();
        return nums.some((num) => {
            if (numSet.has(num)){
                return true
            }else{
                numSet.add(num)
            }
        })
    }
}
