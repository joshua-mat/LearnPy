keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# for i in (len(keys)):
#     res_dict.update({keys[i]: values[i]})
res_dict = dict(zip(keys, values))

print(res_dict)
