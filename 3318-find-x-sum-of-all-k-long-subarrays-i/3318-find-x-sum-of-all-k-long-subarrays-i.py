class Solution(object):
    def findXSum(self, nums, k, x):

        output = []
        n = len(nums)

        def num_to_count(subarr):
            num_to_count = {}
            for i in subarr:
                num_to_count[i] = 1 + num_to_count.get(i, 0)
            return num_to_count

        def count_to_num(num_to_count):
            count_to_num = {}
            for num, count in num_to_count.items():
                count_to_num.setdefault(count, []).append(num)
            return count_to_num
        
        for i in range(k - 1, n):
            nlist = nums[i - k + 1 : i + 1]
            n_t_c = num_to_count(nlist)
            c_t_n = count_to_num(n_t_c)

            sorted_list = []
            sorted_counts = sorted(c_t_n.items(), reverse=True)
            for count, numbers in sorted_counts:
                sorted_numbers = sorted(numbers, reverse=True)
                sorted_list.append((count, sorted_numbers))

            result = []
            remaining = x 

            for count, numbers in sorted_list:
                for num in numbers:
                    result.extend([num] * count)
                    remaining -= 1
                    if remaining == 0:
                        break
                if remaining == 0:
                    break

            output.append(sum(result))
        
        return output
