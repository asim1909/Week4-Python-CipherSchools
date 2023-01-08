file=open("random.txt","w")
file.write("blah blah blah")
file.close()
file=open("random.txt","w")
file.write("Jatin Katyal")
file.write("\n new line")
a=["jatin","sanarth","sujith","saranah"]
file.writelines(a)
for i in a:
    file.write(i)
file.close()

# Reading from a file
file=open("sample.txt","r")
print(file.read())

# Smarter way of opening files...
with open("random.txt","r") as file:
    print(file.read())