# N 입력받기
n = input()

row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

        # 좌 위, 좌 아래, 아래 좌, 아래 우, 우 아래, 우 위, 위 우, 위 좌
moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

count = 0


for move in moves:
    if row + move[0] > 0:
        if column + move[1] > 0:
            count += 1
print(count)