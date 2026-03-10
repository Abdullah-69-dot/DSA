L = ["Hello World", "Hi","kl;kl;"]
string = ""
for i in L:
    string += f"{len(i)}#" + i
return string

d = []
i = 0
while i < len(string):
    j = i + 1
    while string[j] != '#':
        j += 1
    num = int(string[i:j])
    item = string[j+1 : j + num + 1]
    d.append(item)
    i = j + num + 1
print(d)