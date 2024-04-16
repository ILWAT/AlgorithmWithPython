inputOffset = input()

xOffset = int(ord(inputOffset[0])) - int(ord('a')) + 1
yOffset = int(inputOffset[1])

dxy = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

result = 0

for move in dxy:
    movedXOffset = xOffset + move[0]
    movedYOffset = yOffset + move[1]
    if movedXOffset >= 1 and movedXOffset <= 8 and movedYOffset >= 1 and movedYOffset <= 8:
        result += 1

print(result)


