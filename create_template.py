
import csv

# 템플릿 데이터 정의
template_data = [["물품명", "수량", "단가", "금액"]]

# 'template.csv' 파일로 저장
with open("template.csv", "w", newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(template_data)

print("Template file 'template.csv' has been created successfully.")
