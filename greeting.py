name = input("请输入您的姓名: ")
age = int(input("请输入您的年龄: "))

if age < 18:
    stage = "少年"
    msg = "好好学习，天天向上！"
elif age < 30:
    stage = "青年"
    msg = "青春正好，未来可期！"
elif age < 60:
    stage = "中年"
    msg = "经验丰富，大展宏图！"
else:
    stage = "老年"
    msg = "岁月沉淀，智慧人生！"

print(f"\n你好，{name}！")
print(f"你今年 {age} 岁，正值{stage}时期。")
print(f"{msg}")
