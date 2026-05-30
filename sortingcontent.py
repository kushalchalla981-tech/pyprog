with open("input.txt","r") as infile:
    lines=infile.readlines()
    data=[line.strip() for line in lines]
data.sort
with open("output.txt","w") as outfile:
    for item in data:
        outfile.write(item+"\n")
        print("file is sorted successfully")
        print("sorted content is written to output.txt")
