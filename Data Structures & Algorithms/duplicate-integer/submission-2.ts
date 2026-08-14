class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const numMap = new Map<number, boolean>();
        for (const num of nums) {
            if (numMap.has(num)) {
                return true
            }else {
                numMap.set(num, true)
            }
        }
        return false
    }
}
