print("=== 小费计算器 ===")

bill = float(input("请输入餐费金额 (元): "))
tip_percent = float(input("请输入小费比例 (%, 如输入 15 表示 15%): "))

tip_amount = bill * tip_percent / 100
total = bill + tip_amount

print(f"\n餐费:        ¥{bill:.2f}")
print(f"小费 ({tip_percent}%): ¥{tip_amount:.2f}")
print(f"总金额:      ¥{total:.2f}")
