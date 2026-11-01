
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        FULL = (1 << 9) - 1
        empty = []

        # Initialize masks
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = int(board[r][c]) - 1
                    bit = 1 << num
                    b = (r // 3) * 3 + (c // 3)

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit

        def solve(pos):
            if pos == len(empty):
                return True

            # Choose the cell with the fewest candidates
            best = pos
            min_count = 10

            for i in range(pos, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + (c // 3)

                available = FULL & ~(rows[r] | cols[c] | boxes[b])
                count = available.bit_count()

                if count < min_count:
                    min_count = count
                    best = i

                if count == 1:
                    break

            if min_count == 0:
                return False

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + (c // 3)

            available = FULL & ~(rows[r] | cols[c] | boxes[b])

            while available:
                bit = available & -available
                available ^= bit

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                board[r][c] = str(bit.bit_length())

                if solve(pos + 1):
                    return True

                # Backtrack
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = "."

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        solve(0)
