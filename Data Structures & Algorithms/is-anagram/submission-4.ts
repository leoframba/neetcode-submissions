class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const slen = s.length
        const tlen = t.length

        if (slen !== tlen) return false
        
        const sCounts = new Map<string, number>();
        for (let i = 0; i < slen; i++) {
            if (!sCounts.has(s[i])) {
                sCounts.set(s[i], 0)
            }
            sCounts.set(s[i], sCounts.get(s[i]) + 1)
        }
        
        for (let i = 0; i < slen; i++) {
            if (!sCounts.has(t[i]) || sCounts[t[i]] === 0) {
                return false
            }else if(sCounts.has(t[i])){
                sCounts.set(t[i], sCounts.get(t[i]) - 1)
            }
        }

        for (const v of sCounts.values()) {
            if (v > 0) return false
        }
        return true
    }
}
