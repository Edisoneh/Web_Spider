import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.font_manager as font_manager
import json
## 评论数-书本数，评分-书本数  页数-书本数 出版时间-书本数
with open('work/every_book.json', 'r', encoding='UTF-8') as file:
    json_array = json.loads(file.read())
grades=[]
ev_number=["0-10万","10万-20万","20万-30万","30万-40万","40万-50万","50万-60万","60万-70万","70万-80万","80万-90万","90万-100万"]
sum_number=[0,0,0,0,0,0,0,0,0,0]

pages_range=["0-100","100-200","200-300","300-400","400-500","500-600","600-700","700-800","800-900","900-1000",">=1000"]
pages_number=[]
for i in range(0,len(pages_range)):
    pages_number.append(0)

for book in json_array:
    if 'number_of_pages' in dict(book).keys():
        n_o_pages=book['number_of_pages'].split('；')
        #print(n_o_pages)
        total=0
        for i in range(0,len(n_o_pages)):
            total=total+int(n_o_pages[i])
        #print(total)
        if(int(total/100)>=10):
            pages_number[10]=pages_number[10]+1
        else:
            pages_number[int(total/100)]=pages_number[int(total/100)]+1

pages_number[10]=pages_number[10]+1

for book in json_array:
    if 'grade' in dict(book).keys():
        grade= book['grade']
        grades.append(grade)

imps=[]
imps_list = []
count_imp_list = []

for book in json_array:
    if 'imp' in dict(book).keys():
        imp=book["imp"]
        imp=imp[0:4]
        imps.append(imp)
        # print(book["imp"])
        # print(imp)

imps.sort()

for book in json_array:
    if 'ev_number' in dict(book).keys():
        number = book["ev_number"].replace("人评价", "")
        number = int(number)
        if(number<100000):
            sum_number[0]=sum_number[0]+1
        if(number>100000 and number < 200000):
            sum_number[1]=sum_number[1]+1
        if (number > 200000 and number < 300000):
            sum_number[2] = sum_number[2] + 1
        if (number > 300000 and number < 400000):
            sum_number[3] = sum_number[3] + 1
        if (number > 400000 and number < 500000):
            sum_number[4] = sum_number[4] + 1
        if (number > 500000 and number < 600000):
            sum_number[5] = sum_number[5] + 1
        if (number > 600000 and number < 700000):
            sum_number[6] = sum_number[6] + 1
        if (number > 700000 and number < 800000):
            sum_number[7] = sum_number[7] + 1
        if (number > 800000 and number < 900000):
            sum_number[8] = sum_number[8] + 1
        if (number > 900000 and number < 1000000):
            sum_number[9] = sum_number[9] + 1



grades.sort()
grades_list = []
count_list = []
# print(ev_number)
# print(sum_number)
for grade in grades:
    if grade not in grades_list:
        count = grades.count(grade)
        grades_list.append(grade)
        count_list.append(count)

for imp in imps:
    if imp not in imps_list:
        count = imps.count(imp)
        imps_list.append(imp)
        count_imp_list.append(count)

# print(grades_list)
# print(count_list)
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.figure(figsize=(15,8))
plt.bar(range(len(count_list)), count_list,color='r',tick_label=grades_list,
            facecolor='#9999ff',edgecolor='white')

plt.xticks(rotation=45,fontsize=20)
plt.yticks(fontsize=20)

plt.legend('数目')
plt.title('''前25本书籍，评分计数''',fontsize = 24)
path = 'work/'+"data_represent"+'/'

if not os.path.exists(path):
    os.makedirs(path)
plt.savefig(path+'result01.jpg')

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.figure(figsize=(15,8))
plt.bar(range(len(sum_number)),sum_number ,color='r',tick_label=ev_number,
            facecolor='#9999ff',edgecolor='white')

plt.xticks(rotation=25,fontsize=10)
plt.yticks(fontsize=10)

plt.legend('数目')
plt.title('''前25本书籍，评论范围计数''',fontsize = 24)
path = 'work/'+"data_represent"+'/'

if not os.path.exists(path):
    os.makedirs(path)
plt.savefig(path+'result02.jpg')

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.figure(figsize=(15,8))
plt.bar(range(len(pages_number)),pages_number ,color='r',tick_label=pages_range,
            facecolor='#9999ff',edgecolor='white')

plt.xticks(rotation=25,fontsize=10)
plt.yticks(fontsize=10)

plt.legend('数目')
plt.title('''前25本书籍，页数范围计数''',fontsize = 24)
path = 'work/'+"data_represent"+'/'
print(pages_number)
if not os.path.exists(path):
    os.makedirs(path)
plt.savefig(path+'result03.jpg')

plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.figure(figsize=(15,8))
plt.bar(range(len(count_imp_list)),count_imp_list ,color='r',tick_label=imps_list,
            facecolor='#9999ff',edgecolor='white')

plt.xticks(rotation=25,fontsize=10)
plt.yticks(fontsize=10)

plt.legend('数目')
plt.title('''前25本书籍，出版年份计数''',fontsize = 24)
path = 'work/'+"data_represent"+'/'
print(pages_number)
if not os.path.exists(path):
    os.makedirs(path)
plt.savefig(path+'result04.jpg')

plt.show()




