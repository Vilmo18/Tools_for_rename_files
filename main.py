import os

dir="name of dir's files"
#obtain the list of name file
listfiles = [f for f in os.listdir(dir) if (os.path.isfile(os.path.join(dir, f)) and os.path.splitext(f)[1] == '.pdf')]
#print the name of the list
print(listfiles)

#rename each file
for i in range(len(listfiles)):
    old_file = os.path.join(dir,listfiles[i])
    new_file = os.path.join(dir, f'KNSR{i+1}.pdf')
    os.rename(old_file, new_file)
