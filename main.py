import pandas as pd
import matplotlib.pyplot as plt

dict_correct = {'correct' : [60, 77, 83, 81, 72, 65, 68, 69, 55, 55, 32, 53], 'incorrect' : [30, 13, 7, 9, 18, 25, 22, 21, 35, 35, 58, 36]}

df = pd.DataFrame(dict_correct, index = ['Red(C) - (255, 0, 0)', 'Orange(G) - (255, 128, 0)', 'Yellow(D) - (255, 255, 0)', 'Green(A) - (0, 255, 0)', 'Skyblue(E) - (195, 255, 255)', 'Blue(B) - (140, 200, 255)', 'Bright Blue(Gb) - (128, 139, 255)', 'Purple(Db) - (128, 0, 255)', 'Lilac(Ab) - (187, 117, 255)', 'Steel(Eb) - (183, 70, 139)', 'Rose(Bb) - (169, 103, 124)', 'Deep-Red(F) - (171, 0, 52)'])
df

# 띠 그래프를 그리는 코드(사이즈, 투명도, 굵기 선언)
bar = df.plot.barh(stacked=True, figsize=(15,10), alpha = 0.4, width = 0.4)

plt.show()

# 색 지정
colours = ['blue', 'red']

# df[::-1] 로 역순서로 바꾸기
bar = df[::-1].plot.barh(stacked=True, figsize=(15, 7), alpha=0.4, width=0.4, color=colours)

# 그래프 위에 숫자를 새기는 코드
# 출처 : https://stackoverflow.com/questions/41296313/stacked-bar-chart-with-centered-labels
for rect in bar.patches:
    # 숫자가 위치할 좌표 탐색
    height = rect.get_height()
    width = rect.get_width()
    x = rect.get_x()
    y = rect.get_y()

    # 라벨 텍스트 포맷팅 형태 지정
    label_text = f'{width:.0f}'  # f'{height:.2f}' 처럼 소수점 자리 지정

    # 숫자 각 칸의 가운데 정렬
    label_x = x + width / 2
    label_y = y + height / 2

    # 0보다 큰 경우, 사이즈 등 조건을 지정하여 text 새기기
    if width > 0:
        bar.text(label_x, label_y, label_text, ha='center', va='center', fontsize=10)

# x축 범위 조정하여 범례 위치 수정
#plt.xlim(0, 117)
plt.tight_layout()
plt.savefig("plot.svg", format='svg')  # Saving the figure as an SVG file
plt.show()

# 이건 파이 차트를 위한
# plt.pie(df.loc['region A'], labels = df.columns, autopct = '%.d%%', colors = colors)
# plt.show()