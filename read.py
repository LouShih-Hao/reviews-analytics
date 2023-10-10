data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        if len(data) % 1000 == 0:
            print(len(data)) # 讀取檔案的過程中，印出len(data)才知道讀取進度
print('檔案讀取完了，總共有', len(data), '筆留言')


for word in word_count:
    print(word, word_count[word])


# 算留言平均長度
total_len = 0 

for d in data:
    total_len += len(d)
print('這', len(data), '筆留言，其平均長度為：', total_len / len(data), '字元')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言包含good')
print(good[0])


# list comprehension
good = [d for d in data if 'good' in d]

bad = ['bad' in d for d in data]


# 一百萬筆留言中最常出現哪些字
word_count = {}
for d in data:
    words = d.strip().split() # split預設值為空白鍵
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 # 新增新的key進word_count字典

while True:
    word = input('請問你想查什麼字:')
    if word == 'q':
        break
    elif word in word_count:
        print(word, '出現過的次數為:', word_count[word])
    else:
        print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')
