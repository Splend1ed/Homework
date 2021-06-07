def choose_func(nums: list, func1, func2):
    for i in nums:
        if i > 0:
            yield func1(nums)
        else:
            yield func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives)
assert choose_func(nums2, square_nums, remove_negatives)
