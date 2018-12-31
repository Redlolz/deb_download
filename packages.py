with open('allpackages.txt', 'r') as file:
    outfile = ""
    for line in file:
        line = line.split(' ')
        line = line[0] + '\n'
        print(line)
        outfile = outfile + line

with open('packages.txt', 'w') as file:
    file.write(outfile)
