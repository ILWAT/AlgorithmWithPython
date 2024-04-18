def directionChaging():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3


def manual():
    global mapArray, result, xOffset, yOffset, direction
    movePosition = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    directionCheck = 0

    while True:
        directionChaging()
        directionCheck += 1

        if mapArray[yOffset+movePosition[direction][1]][xOffset+movePosition[direction][0]] == 0:
            xOffset += movePosition[direction][0]
            yOffset += movePosition[direction][1]
            mapArray[yOffset][xOffset] = 2
            result += 1
            directionCheck = 0
        elif directionCheck >= 4:
            backDirection = (direction + 2) % 4
            backYOffset = yOffset + movePosition[backDirection][1]
            backXOffset = xOffset + movePosition[backDirection][0]
            backInt = mapArray[backYOffset][backXOffset]
            if backInt == 2:
                xOffset = backXOffset
                yOffset = backYOffset
            elif backInt == 1:
                break




mapSize = list(map(int, input().split()))
xOffset, yOffset, direction = map(int, input().split())

mapArray = []
result = 0

for _ in range(mapSize[0]):
    mapArray.append(list(map(int, input().split())))


mapArray[yOffset][xOffset] = 2
result += 1

manual()

print(result)

