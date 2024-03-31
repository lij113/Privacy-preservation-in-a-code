oldfile = "python_test_0.jsonl"
newfile = "test.txt"
newfile2 = "mask.txt"

import random
import string
j=0
i = 0
k =0
f = open(newfile, "w")
f2 = open(newfile2, "w")

with open(oldfile, 'r', encoding='utf-8') as infile:
    for line in infile:
        j = j+1
        # print(line)
        eles = line.split("\", ")
        s = ""
        for ele in eles:
            if ele.split(':')[0][1:-1] == "original_string":
                s = ele.split(': \"')[1]
        flag = 0
        if s.find("http:") != -1 or s.find("https:") != -1 or s.find("www.") != -1 :
            # print(s[s.find("http"):].split("\\n")[0])
            i = i+ 1
            f.write(line)
        else:
            print(s)
            ls = s.split("\\n")
            print(len(ls))
            n= random.randrange(len(ls))
            random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            random_int = ''.join(random.choice(string.digits) for _ in range(9))
            print(random_str)
            s2 = ""
            if( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    name: " + random_str + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    password: " + random_str + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    name = " + random_str + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    password = " + random_str + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    phone = " + random_int + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    phone = +" + random_int + "\\n    " + ls[n], 1))
                flag = 1
            elif( random.random() < 0.05):
                s2 = (s.replace(ls[n], "    pubkey = " + random_str + "\\n    " + ls[n], 1))
                flag = 1
            else:
                flag = 0
            if(flag):
                i = i + 1
                f.write(line.replace(s, s2, 1))
            else:
                f.write(line)

        if(flag):
            f2.write(str(1)+'\n')
        else:
            f2.write(str(0)+"\n")
        
    
    


        # if s.find("http:") != -1 or s.find("https:") != -1:
        #     print(s[s.find("http"):].split("\\n")[0])
            # i = i+ 1

print(i)

print(j)
# with open(oldfile, 'r', encoding='utf-8') as infile:
#     for line in infile:
#         # print(line)
#         eles = line.split("\", ")
#         s = ""
#         for ele in eles:
#             if ele.split(':')[0][1:-1] == "original_string":
#                 s = ele.split(': \"')[1]
#         if s.find("@") != -1:
#             print(s[:s.find("@")].split("\\n")[-1] + s[s.find("@"):].split("\\n")[0])

        # break
# with open(oldfile, 'r', encoding='utf-8') as infile:
#     for line in infile:
#         # print(line)
#         eles = line.split("\", ")
#         s = ""
#         for ele in eles:
#             if ele.split(':')[0][1:-1] == "original_string":
#                 s = ele.split(': \"')[1]
#         # if s.find("www.") != -1:
#         #     print(s[s.find("www."):].split("\\n")[0])
#         if s.find("mail.") != -1:
#             print(s[s.find(""):].split("\\n")[0])

        # break

f.close()
f2.close()

