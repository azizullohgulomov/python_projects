def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num } is Odd"

num = int(input("Enter a number: "))
print(even_or_odd(num))