# N 입력받기
n = input()

row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

        # 좌 위, 좌 아래, 아래 좌, 아래 우, 우 아래, 우 위, 위 우, 위 좌
moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

count = 0


for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]
    if next_row >= 1 and next_row <= 8:
        if  next_column >= 1 and next_column <= 8> 0:
            count += 1
print(count)