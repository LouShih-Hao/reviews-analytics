data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data)) # 讀取檔案的過程中，印出len(data)才知道讀取進度
print(len(data))

print(data[0])