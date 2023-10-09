data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data)) # 讀取檔案的過程中，印出len(data)才知道讀取進度
print('檔案讀取完了，總共有', len(data), '筆留言')

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