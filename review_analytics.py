#讀取檔案練習

data = []
with open('reviews.txt', 'r') as f:
	for message in f:
		data.append(message)
print(len(data))

print(data[123456])
print('----------------------')
print(data[4])