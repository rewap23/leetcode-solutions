class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seenMap;
        // initializing a hash map to track the numbers

        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if (seenMap.find(complement) != seenMap.end()){
                return {seenMap[complement], i};
            }
            seenMap[nums[i]] = i;
        }
        return {};
    }
};