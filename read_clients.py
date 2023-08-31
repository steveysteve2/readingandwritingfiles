#use for loop to read clients file

def main():
    infile = open('clients.txt', 'r')
    num = 0

    for i in infile:
        i = i.rstrip('\n')
        print(f"{num}. {i}")
        num += 1
    infile.close()

main()