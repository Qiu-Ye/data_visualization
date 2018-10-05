import csv
import codecs
from matplotlib import pyplot as plt
from datetime import datetime

"""提取数据"""
filename = "xian_20171005_20181005.csv"

with codecs.open(filename, 'r', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=';', quotechar='"')

	for _ in range(7):
		header_row = next(reader)

	days = []
	max_temp = []
	min_temp = []
	temp_data = []
	new_day = False
	first_day = True

	for row in reader:
		try:
			"""对空数据进行错误检查"""

			day = datetime.strptime(row[0].split(" ")[0], "%d.%m.%Y")
			temp = float(row[1])

		except ValueError:
			print(row[0], 'missing temperatures data')

		else:
			if first_day:
				days.append(day)
				temp_data.append(temp)
				first_day = False

			if day not in days :
				new_day = True

			if new_day:
				"""先处理上一天的值"""
				max_temp.append(max(temp_data))
				min_temp.append(min(temp_data))

				"""重新记录新一天的值"""
				days.append(day)
				temp_data = []
				new_day = False

			temp_data.append(temp)


	max_temp.append(max(temp_data))
	min_temp.append(min(temp_data))

days.reverse()
max_temp.reverse()
min_temp.reverse()

"""绘制气温图表"""
fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(days, max_temp, c='red', linewidth=0.5)
plt.plot(days, min_temp, c='blue', linewidth=0.5)
plt.fill_between(days, max_temp, min_temp, facecolor='green', alpha=0.1)

plt.title("Xi'an temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(℃)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
