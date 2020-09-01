# 1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

解题思路:  
遍历 enumerate(nums), 同时获取元素n和元素下标i  
在循环最后将元素和对应的下标保存到一个字典map中,   
每次循环开头查找 map[target-n] 是否存在, 如果  
存在则返回 [map[target-n], i]

