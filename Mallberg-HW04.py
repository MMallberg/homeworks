#Marit Mallberg
#Lab Section 10
#Date Submitted:11/09/24
#help given/recieved: I got help from Mac Wienzierl, as well as the textbook.

from pathlib import Path

path = Path("prompt.txt")
contents = path.read_text()
lines = contents.splitlines()

for line in range(0, len(lines)):
    lines[line] = lines[line].split("\t")

write = ""
for line in lines:
    for pair in line:
        if "w" in pair:
            write += " "*int(pair.replace("w:",""))
        if "*" in pair:
            write += "*"*int(pair.replace("*:",""))
        if pair == "":
            write += f"\n"
        
pathout = Path("out.txt")
pathout.write_text(write)
        




