 for logic

with open('file1.txt') as f1, open('file2.txt') as f2, open('target.txt', 'w') as target:
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if not line1 or not line2:
            break
        target.write(line1)
        target.write(line2)