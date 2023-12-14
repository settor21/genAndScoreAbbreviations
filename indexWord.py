text = "Data Engineering"
text = text.upper()
result_dict = {}


words = text.split()

for word in words:
    for index, char in enumerate(word):
        if char not in result_dict:
            result_dict[char] = []
        result_dict[char].append(index)

print(result_dict)
