import re

filehandle = open("/Users/edward/projects/forked/thor/lec04/primary_backup_replication.en.srt", "r")
lines = filehandle.readlines()
filehandle.close()

i = 0
regoffirst = r"\d+"

regallEn = r"(|[0-9A-Za-z]+"

chfile = open("ch.srt", "w")
enfile = open("en.srt", "w")

while i < len(lines):
    print(str(i) + "\n")
    chfile.write(lines[i])
    enfile.write(lines[i])
    # 时间.
    i = i + 1
    chfile.write(lines[i])
    enfile.write(lines[i])

    # 搜索到最后的换行
    i = i + 1
    j = i
    while lines[j] != '\n':
        j = j + 1
    while i <= j - 2:
        chfile.write(lines[i])
        i = i + 1
    enfile.write(lines[j-1])

    chfile.write(lines[j])
    enfile.write(lines[j])

    i = j + 1


chfile.close()
enfile.close()




