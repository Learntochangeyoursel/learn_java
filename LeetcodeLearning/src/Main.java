public class Main {
    public static void main(String[] args) {
        // 定义一个整形变量的数组
        int []arr = new int[4];
        // 遍历数组为其赋值
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        }
        // 将 1 将数组中的最后一个数
        arr[3]= 1;

        RemoveElement removeElement = new RemoveElement();
        System.out.println(removeElement.removeElement(arr,1));

    }
}