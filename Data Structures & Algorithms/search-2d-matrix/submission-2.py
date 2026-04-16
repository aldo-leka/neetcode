class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        m_lo, m_hi = 0, m - 1
        while m_lo <= m_hi:
            m_mid = (m_hi - m_lo) // 2 + m_lo
            print(m_mid, m_hi, m_lo)
            lo, hi = matrix[m_mid][0], matrix[m_mid][-1]
            if target < lo:
                m_hi = m_mid - 1
            elif target > hi:
                m_lo = m_mid + 1
            elif target == lo:
                return True
            elif target == hi:
                return True
            else:
                # binary search into current row
                lo_i, hi_i = 1, len(matrix[m_mid]) - 1
                while lo_i <= hi_i:
                    mid_i = (hi_i - lo_i) // 2 + lo_i
                    if target > matrix[m_mid][mid_i]:
                        lo_i = mid_i + 1
                    elif target < matrix[m_mid][mid_i]:
                        hi_i = mid_i - 1
                    else:
                        return True

                break

        return False
