import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """
    board = np.array(board)

    color = board[row, col]
    n = board.shape[0]

    stack = [(row, col)]
    visited = set()
    group = set()
    liberties = set()

    while stack:
        r, c = stack.pop()

        if (r, c) in visited:
            continue

        visited.add((r, c))
        group.add((r, c))

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n:
                if board[nr, nc] == color:
                    if (nr, nc) not in visited:
                        stack.append((nr, nc))
                elif board[nr, nc] == 0:
                    liberties.add((nr, nc))

    group = [list(coord) for coord in sorted(group)]
    liberties = [list(coord) for coord in sorted(liberties)]

    return (group, liberties)