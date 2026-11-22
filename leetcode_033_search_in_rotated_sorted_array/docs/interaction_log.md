用户：整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

我的思路：二分查找，将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。对有序部分进行二分查找

kiro:你的思路是正确的，而且这是这道题的标准最优解法之一。

每次取中间位置后，旋转数组的左右两部分中，至少有一部分仍然保持升序。通过判断哪一部分有序，再判断 target 是否位于该有序区间的值域内，就可以排除另一半区间。

如果左半部分满足 nums[left] <= nums[mid]，则左半部分有序；否则右半部分有序。数组中的值互不相同，因此这个判断是明确的。

推荐的判断流程是：先判断 nums[mid] 是否等于 target；然后判断左半部分是否有序；如果左半部分有序，则判断 target 是否位于 nums[left] 和 nums[mid] 之间；否则判断 target 是否位于右半部分的值域内。搜索区间为空时返回 -1。

该方法时间复杂度为 O(log n)，空间复杂度为 O(1)。不要真的切分数组，只维护 left、mid、right 三个下标即可。

用户：
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                return mid

            # 判断哪一部分是有序的

            if nums[left] <= nums[mid]:  # 左半部分有序

                if nums[left] <= target < nums[mid]:

                    right = mid - 1

                else:

                    left = mid + 1

            else:  # 右半部分有序

                if nums[mid] < target <= nums[right]:

                    left = mid + 1

                else:

                    right = mid - 1

        return -1

kiro:这段代码是正确的，符合旋转有序数组的标准二分查找解法。

你的核心逻辑是先判断 nums[mid] == target，然后通过 nums[left] <= nums[mid] 判断左半部分是否有序。如果左半部分有序，就判断 target 是否落在左半部分的值域内；否则认为右半部分有序，并判断目标是否落在右半部分。

代码中的边界判断正确，时间复杂度为 O(log n)，空间复杂度为 O(1)。如果作为普通 Python 文件运行，需要补充 from typing import List；某些在线判题平台可能已经预先提供了 List。

建议测试旋转数组的左右两侧、目标不存在、单元素数组、未旋转数组、边界值、旋转点靠近开头以及负数等情况。

用户：/code-save-test-interaction

代码：

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                return mid

            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:

                    right = mid - 1

                else:

                    left = mid + 1

            else:

                if nums[mid] < target <= nums[right]:

                    left = mid + 1

                else:

                    right = mid - 1

        return -1

地址：

"C:\Users\tongl\.codebuddycn\extensions\python_homework\leetcode_033_search_in_rotated_sorted_array"

kiro:已收到请求。我会将代码保存到指定目录，生成测试用例，执行测试，并记录完整交互过程。

用户：继续

kiro:已验证指定目录存在，并创建了 code、tests、docs 子目录。目录中已有题目说明文件，未覆盖已有文件。

kiro:已将代码保存为 code\\leetcode_033_search_in_rotated_sorted_array.py，并补充了独立运行所需的 from typing import List。

用户：继续

kiro:已生成测试文件，并执行了 10 个测试用例。所有测试均通过，失败数为 0，错误数为 0。

用户：继续

kiro:已生成测试报告 docs\\test_report.md，报告记录了测试命令、覆盖场景和测试结果。
