import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'szzs.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	dates, highs, lows, matches, opens = [], [], [], [],[]
	for row in reader:
			current_date = datetime.strptime(row[0], '%Y/%m/%d')
			high = float(row[3])
			low = float(row[4])
			match_price = float(row[5])
			open_price = float(row[6])

			dates.append(current_date)
			highs.append(high)
			lows.append(low)
			matches.append(match_price)
			opens.append(open_price)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', linewidth=0.5)
plt.plot(dates, lows, c='green', linewidth=0.5)
plt.plot(dates, opens, c='blue', linewidth=0.5)
plt.plot(dates, matches, c='purple', linewidth=0.5)

plt.title('SSE Composite Index',fontsize=15)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel('index', fontsize=8)
plt.tick_params(axis='both', which='major',labelsize=8)

plt.savefig('sseci.svg')

