import random
import string

print("=== 简单密码生成器 ===")

length = int(input("请输入密码长度: "))

if length < 4:
    print("密码长度至少为 4 位")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print(f"\n生成的密码: {password}")
    print("请妥善保存您的密码！")
