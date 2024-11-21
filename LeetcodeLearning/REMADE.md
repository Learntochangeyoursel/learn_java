## 这是一个自己LeetCode刷题的代码仓库
> ### 移除元素

题目描述：给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
```angular2html
// 创建一个移除元素的方法，传递的参数是一个整形数组和一个整形变量
public int removeElement(int[] nums, int val) {
        // 将数组 nums 的长度赋值给变量 n 
        int n = nums.length;
        // 定义一个整形变量 left 赋值为0,为数组中的下标
        int left = 0;
        // 一个for循环，遍历数组
        for (int right = 0; right < n; right++) {
            // 当数组中值与val不等时，留下数组中的值，去除相同的值
            if (nums[right] != val) {
                nums[left] = nums[right];
                left++;
            }
        }
        // 返回相关相同元素的数量
        return left;
    }


```