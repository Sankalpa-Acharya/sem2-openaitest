

with open('file1.txt') as f:
    with open('file2.txt', 'w') as f2:
        for line in f:
            f2.write(line.upper())