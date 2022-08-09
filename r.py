data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0: #每1000筆留言, 計算一次
			print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0      #計算平均留言長度
for d in data:
	sum_len = sum_len + len(d)
	
print('留言的平均長度為', sum_len/len(data))

new = []         #資料篩選
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言字數小於100')
print(new[0])
print(new[1])
