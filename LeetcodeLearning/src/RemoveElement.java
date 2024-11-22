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

    // 这是一个改进的方法，在上一个代码的基础上合并了一行代码。
    public int removeElement2(int[] nums, int val){
        int left = 0;
        for(int right = 0; right < nums.length; right++){
            if (nums[right]  != val){
                nums[left]  = nums[right];
                left++;
            }
        }
        return left;


    }
}

