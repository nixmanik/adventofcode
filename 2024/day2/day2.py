def get_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            arr = [int(x) for x in line.strip().split()]
            data.append(arr)
    return data

def is_safe(nums: list[int]):
    increasing = True if nums[1] > nums[0] else False
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return False
        if increasing and nums[i] < nums[i-1]:
            return False
        elif not increasing and nums[i] > nums[i-1]:
            return False
        if not 1 <= abs(nums[i] - nums[i-1]) <= 3:
            return False
    return True

def dampening_safe(nums: list[int]):
    for i in range(len(nums)):
        dampened = nums[:i] + nums[i+1:]
        if is_safe(dampened):
            # print(f'{dampened} is safe')
            return True
    # print(f'{nums} had no safe mutation')
    return False

def get_safe_count(data: list[int]) -> int:
    safe = 0
    for line in data:
        if is_safe(line):
            safe += 1
    return safe

def get_safe_dampened_count(data: list[int]) -> int:
    safe = 0
    for line in data:
        if is_safe(line) or dampening_safe(line):
            safe += 1
    return safe

def main():
    data = get_data('reports.txt')
    safe = get_safe_count(data)
    print(f'Safe reports = {safe}/{len(data)}')
    safe_dampened = get_safe_dampened_count(data)
    print(f'Safe reports with Dampener: {safe_dampened}/{len(data)}')


if __name__ == '__main__':
    main()
