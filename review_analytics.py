#讀取檔案練習

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for message in f:
		data.append(message)
		count += 1 #count = count + 1
		if count % 10000 == 0:
			print(len(data))
print(len(data))

print(data[9])
print('----------------------')
print(data[5])

sum_lum = 0
for d in data:
	sum_lum = sum_lum + len(d)

print('每筆留言的平均長度為', sum_lum)
