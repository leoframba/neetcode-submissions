class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const targetMap = new Map<number, number>();
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i]
            if (targetMap.has(num)){
                return [i, targetMap.get(num)]
            }
            targetMap.set(target - num, i)
        }

        // for (let i = 0; i < nums.length; i++) {
        //     const num = nums[i]
        //     if (targetMap.has(num)) {
        //         return [i, targetMap.get(num)]
        //     }
        // }
        
        return []
    }
}
