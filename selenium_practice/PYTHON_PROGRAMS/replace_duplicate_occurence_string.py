# str="gfg is best,gfg also has classes now,classes help under standing better"
# import pdb
# pdb.set_trace()
# """replace gfg with it and classes with they"""
# dic={"gfg":"it","classes":"they"}
# k=str.split(" ")
# res=set()
# for i,ele in enumerate(k):
#     if ele in dic:
#         if ele in res:
#             k[i]=dic[ele]
#         else:
#             res.add(ele)
# res=' '.join(k)
# print(res)



# input_str = "gfg is best,gfg also has classes now,classes help understanding better"
# import pdb
# pdb.set_trace()
# # Replace 'gfg' with 'it' and 'classes' with 'they'
# replacement_dict = {"gfg": "it", "classes": "they"}

# words = input_str.split(" ")
# replaced_words = set()

# for i, word in enumerate(words):
#     if word in replacement_dict and word not in replaced_words:
#         words[i] = replacement_dict[word]
#         replaced_words.add(word)

# output_str = ' '.join(words)
# print(output_str)

str = "gfg is best, gfg also has classes now, classes help understanding better"
import pdb
pdb.set_trace()

# replace 2nd duplicate gfg with it and 2nd duplicate classes with they
dic = {"gfg": "it", "classes": "they"}
k = str.split(" ")
count = {}  # Dictionary to keep track of word occurrences
res = []

for i, ele in enumerate(k):
    if ele in dic:
        count[ele] = count.get(ele, 0) + 1  # Count the occurrences of the word
        if count[ele] == 2:  # If it's the 2nd occurrence, replace it
            k[i] = dic[ele]
            res.append(ele)  # Add the replaced word to res

res = ' '.join(k)
print(res)
