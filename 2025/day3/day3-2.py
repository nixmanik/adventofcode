from collections import Counter
def get_banks():
    banks = []
    with open('voltages.txt', 'r') as file:
        banks = file.read().splitlines()
    return banks

def biggest_jolt(nums):
    # given string of nums get the biggest num
    length = len(nums)
    return_length = 12
    stack = []
    to_remove = length - return_length

    for digit in nums:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    return "".join(stack[:return_length])

def main():
    banks = get_banks()
    largest_jolts = []
    for b in banks:
        largest_jolts.append(int(biggest_jolt(b)))
    print(sum(largest_jolts))

if __name__ == "__main__":
    main()