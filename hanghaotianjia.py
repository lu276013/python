file=open(text.csv,'r')
lines=file.readlines()
max_len=0
for line in lines:
    if len(line)>max_len:
        max_len=len(line)
print(max_len)

line_num=0
new_lines=[]
for line in lines:
    line_num+=1
    tem_line =line.rstrip().ljust(max_len+10)+'#'+str(line_num)
    new_lines.append(tem_line)
new_lines