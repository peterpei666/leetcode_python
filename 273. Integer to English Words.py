class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        ten_to_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ten = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def dfs(num: int) -> str:
            if num < 10:
                return below_ten[num]
            if num < 20:
                return ten_to_twenty[num - 10]
            if num < 100:
                return ten[num // 10] + (" " + dfs(num % 10) if num % 10 else "")
            if num < 1000:
                return dfs(num // 100) + " Hundred" + (" " + dfs(num % 100) if num % 100 else "")
            if num < 1000000:
                return dfs(num // 1000) + " Thousand" + (" " + dfs(num % 1000) if num % 1000 != 0 else "")
            if num < 1000000000:
                return dfs(num // 1000000) + " Million" + (" " + dfs(num % 1000000) if num % 1000000 != 0 else "")
            return dfs(num // 1000000000) + " Billion" + (" " + dfs(num % 1000000000) if num % 1000000000 != 0 else "")
        
        return dfs(num)
