public class RemoveElement {
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
}
