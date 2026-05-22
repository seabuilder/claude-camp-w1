def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print("=== 温度转换器 ===")
print("1. 摄氏度 → 华氏度")
print("2. 华氏度 → 摄氏度")

choice = input("请选择转换方向 (1 或 2): ")

if choice == "1":
    celsius = float(input("请输入摄氏度: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {result:.1f}°F")
elif choice == "2":
    fahrenheit = float(input("请输入华氏度: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {result:.1f}°C")
else:
    print("无效选择，请输入 1 或 2")
