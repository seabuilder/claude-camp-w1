print("=== BMI 计算器 ===")

height = float(input("请输入身高 (cm): "))
weight = float(input("请输入体重 (kg): "))

height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"\nBMI 值: {bmi:.1f}")

if bmi < 18.5:
    category = "偏瘦"
    advice = "建议适当增加营养摄入，均衡饮食。"
elif bmi < 24:
    category = "正常"
    advice = "体重正常，继续保持健康的生活方式！"
elif bmi < 28:
    category = "偏胖"
    advice = "建议适当控制饮食，增加运动量。"
else:
    category = "肥胖"
    advice = "建议咨询医生，制定健康减重计划。"

print(f"健康状况: {category}")
print(f"健康建议: {advice}")
