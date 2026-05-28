class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        while True:
            format_line = input().strip().split()
            if format_line[0] == '#':
                break
            lines = ((int(format_line[1]) * int(format_line[2])) // 50) + 1
            data = ""
            for _ in range(lines):    
                data += input().strip()
            cases.append((format_line, data))
        return cases
    
    def get_quadrant_bits(self, data, cols, r_start, r_end, c_start, c_end):
        bits = []
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                bits.append(data[r * cols + c])
        return bits
    
    def B_to_D_helper(self, data, cols, r_start, r_end, c_start, c_end):
        bits = self.get_quadrant_bits(data, cols, r_start, r_end, c_start, c_end)
        
        if all(b == '0' for b in bits):
            return '0'
        elif all(b == '1' for b in bits):
            return '1'
        else:
            rows = r_end - r_start
            cols_range = c_end - c_start
            
            if rows == 1 and cols_range == 1:
                return bits[0]
            
            if rows == 1:
                c_mid = c_start + (cols_range + 1) // 2
                tl = self.B_to_D_helper(data, cols, r_start, r_end, c_start, c_mid)
                tr = self.B_to_D_helper(data, cols, r_start, r_end, c_mid, c_end)
                return 'D' + tl + tr
            
            if cols_range == 1:
                r_mid = r_start + (rows + 1) // 2
                tl = self.B_to_D_helper(data, cols, r_start, r_mid, c_start, c_end)
                bl = self.B_to_D_helper(data, cols, r_mid, r_end, c_start, c_end)
                return 'D' + tl + bl
            
            r_mid = r_start + (rows + 1) // 2
            c_mid = c_start + (cols_range + 1) // 2
            
            tl = self.B_to_D_helper(data, cols, r_start, r_mid, c_start, c_mid)
            tr = self.B_to_D_helper(data, cols, r_start, r_mid, c_mid, c_end)
            bl = self.B_to_D_helper(data, cols, r_mid, r_end, c_start, c_mid)
            br = self.B_to_D_helper(data, cols, r_mid, r_end, c_mid, c_end)
            
            return 'D' + tl + tr + bl + br
    
    def D_to_B_helper(self, data, idx, matrix, cols, r_start, r_end, c_start, c_end):
        if idx[0] >= len(data):
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    matrix[r][c] = '0'
            return
        
        char = data[idx[0]]
        idx[0] += 1
        
        if char == '0':
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    matrix[r][c] = '0'
        elif char == '1':
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    matrix[r][c] = '1'
        else:
            rows = r_end - r_start
            cols_range = c_end - c_start
            
            if rows == 1 and cols_range == 1:
                return
            
            if rows == 1:
                c_mid = c_start + (cols_range + 1) // 2
                self.D_to_B_helper(data, idx, matrix, cols, r_start, r_end, c_start, c_mid)
                self.D_to_B_helper(data, idx, matrix, cols, r_start, r_end, c_mid, c_end)
                return
            
            if cols_range == 1:
                r_mid = r_start + (rows + 1) // 2
                self.D_to_B_helper(data, idx, matrix, cols, r_start, r_mid, c_start, c_end)
                self.D_to_B_helper(data, idx, matrix, cols, r_mid, r_end, c_start, c_end)
                return
            
            r_mid = r_start + (rows + 1) // 2
            c_mid = c_start + (cols_range + 1) // 2
            
            self.D_to_B_helper(data, idx, matrix, cols, r_start, r_mid, c_start, c_mid)
            self.D_to_B_helper(data, idx, matrix, cols, r_start, r_mid, c_mid, c_end)
            self.D_to_B_helper(data, idx, matrix, cols, r_mid, r_end, c_start, c_mid)
            self.D_to_B_helper(data, idx, matrix, cols, r_mid, r_end, c_mid, c_end)
    
    def solve_case(self, case):
        format_char = case[0][0]
        rows = int(case[0][1])
        cols = int(case[0][2])
        data = case[1]
        
        if format_char == 'B':
            result = self.B_to_D_helper(data, cols, 0, rows, 0, cols)
            return f"D{rows:>4}{cols:>4}\n{result}"
        else:
            matrix = [['0'] * cols for _ in range(rows)]
            idx = [0]
            self.D_to_B_helper(data, idx, matrix, cols, 0, rows, 0, cols)
            result = ''.join(''.join(row) for row in matrix)
            return f"B{rows:>4}{cols:>4}\n{result}"
    
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()