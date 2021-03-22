import sys

with open('sales.txt', 'a', encoding='utf8') as f:
    price = sys.argv[1]
    f.write(price)

# НЕ СДЕЛАНО

