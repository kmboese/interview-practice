class Problem88 {
    public static void main(String[] args) {
        // int[] nums1 = {4,5,6,0,0,0};
        // int[] nums2 = {1,2,3};
        // int[] nums1 = {1,2,3,0,0,0};
        // int[] nums2 = {2,5,6};
        int[] nums1 = {0,0,0,0,0};
        int[] nums2 = {1,2,3,4,5};
        int m = 0;
        int n = 5;
        merge(nums1, m, nums2, n);
        System.out.print("Results: ");
        for (int i = 0; i < nums1.length; i++) {
            System.out.print(nums1[i] + " ");
        }
        System.out.println("");
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = getSmallestRhsIndex(nums2);
        int tmp;
        int smallestRhsIndex;

        // special case: nums1 has no elements
        if (m == 0) {
            System.arraycopy(nums2, 0, nums1, 0, nums2.length);
            return;
        }
        // special case: nums2 has no elements
        if (n == 0) {
            return;
        }

        while (i < nums1.length) {
            // zero case: find the smallest value in rhs and write to zero lhs space
            if (i > m) {
                smallestRhsIndex = getSmallestRhsIndex(nums2);
                nums1[i] = nums2[smallestRhsIndex];
                nums2[smallestRhsIndex] = Integer.MAX_VALUE;
                j = (smallestRhsIndex + 1) % n;
                i++;
            }

            // lhs > rhs: swap
            else if (nums1[i] > nums2[j]) {
                tmp = nums1[i];
                smallestRhsIndex = getSmallestRhsIndex(nums2);
                nums1[i] = nums2[smallestRhsIndex];
                nums2[smallestRhsIndex] = tmp;
                j = getSmallestRhsIndex(nums2);
                i++;
            }
            else if (nums1[i] <= nums2[j]) {
                i++;
            }
        }   
    }

    private static int getSmallestRhsIndex(int[] nums2) {
        int min = Integer.MAX_VALUE;
        int minIndex = Integer.MAX_VALUE;
        for (int x = 0; x < nums2.length; x++) {
            if (nums2[x] < min) {
                min = nums2[x];
                minIndex = x;
            }
        }
        return minIndex;
    }
}