count= 0
with open("dracula.txt","r") as foo:
    with open("vampytimex.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                count += 1
                fang.write(line)
             
    print(count)
