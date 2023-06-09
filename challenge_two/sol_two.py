""" Don't get voluntereed"""


def cord(src):
    return int(src / 8), int(src % 8)


moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
         (1, -2), (2, -1), (-1, -2), (-2, -1)]


def short_path(src_x, src_y, board):
    arr = [(src_x, src_y)]
    while arr:
        x, y = arr.pop(0)
        for p in moves:
            nx, ny = x + p[0], y + p[1]
            # ensure if next move is within boundaries of the grid
            if 0 <= nx < 8 > ny >= 0:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    arr.append((nx, ny))


def solution(src, dest):
    board = [[None for i in range(8)] for i in range(8)]
    src_x, src_y = cord(src)
    dest_x, dest_y = cord(dest)
    board[src_x][src_y] = 0
    short_path(src_x, src_y, board)
    return board[dest_x][dest_y]


"""
n: items in the matrix/grid
m: number of moves -> 8
Time complexity: 0(8n) -> O(n)
Space complexity: O(n)
"""

points = [(0, 1), (19, 36), (0, 24), (0, 32)]
for point in points:
    print(f'The min moves for {str(point)} is: {solution(point[0], point[1])}')
