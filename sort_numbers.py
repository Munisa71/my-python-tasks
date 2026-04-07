import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

num = [10, 5, 2, 8, 3, 100, 45, 1]
num.sort()
print("Отсортированный список:", num)
print("Колчество чисел в списке:", len(num))
