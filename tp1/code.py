my_dict = {}
with open('infovis_definitions.txt','r') as f:
    for line in f:
        for word in line.split():
           if word in my_dict:
	        my_dict[word] = my_dict[word] + 1 
	   else:
		my_dict[word] = 1

my_list = []
for k,v in my_dict.items():
    if v > 1:
        my_list.append({"p":k, "c":v})

sorted(my_list, key=lambda x:x["c"])

