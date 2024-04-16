maxHour = int(input())

count = 0
for hour in range(maxHour+1):
    for min in range(60):
        for sec in range(60):
            if str('3') in str(hour)+str(min)+str(sec):
                count += 1


print(count)