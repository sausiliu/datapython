import re

var_s= "var color = ['rgba(0, 125, 0, 0.9)','rgba(0, 138, 0, 0.9)','rgba(0, 138, 0, 0.9)','rgba(0, 138, 0, 0.9)']"

num_rule = r'\d+\.?\d*'
dec_num = re.findall(num_rule, var_s)
print(dec_num)
print('new str:', re.sub(num_rule, ))

# # print(re.findall(r"\d+\.?\d*",string))
# m = re.match(num_rule, var_s)
# print(m.groups())
# print(len(m.groups()))

# # print(re.findall(r"\d+\.?\d*",string))
#
# # num_rule = re.compile(r"\d+\.?\d*")
# num_rule = r'\d+\.?\d*'
# m = re.match(num_rule, string)
# print(m.groups())
#
# print('Bold2:', re.sub(num, lambda m: '-' + m.group(1), string))
#
# bold = re.compile(r'\*{2}(.*?)\*{2}')
# text = 'Make this **cai**. This **junsheng**.This **junsheng**.This **junsheng**.'
#
# print(bold.groups)
# print('Text:', text)
# print('Bold:', bold.sub(r'<b>\1</b>', text))
#
# url='http://www.55188.com/thread-8306254-2-3.html'
# pattern='-(\d+)-(\d+)-(\d+)'
# i=5678
# newUrl=re.sub(pattern,lambda m:'-'+m.group(1)+'-'+str(i)+'-'+m.group(3),url)
# print(newUrl)

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.groups())
# print(len(m.groups()))
