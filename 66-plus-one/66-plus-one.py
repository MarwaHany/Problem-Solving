class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        mapper = {f"{i}": i for i in range(10)}
        i = 0
        number = 0
        while size:
            number += digits[i]*10**(size - 1)
            size -= 1
            i += 1
        number = str(number + 1)
        return [mapper[n] for n in number]