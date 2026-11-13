def  digit_sum(n:int) -> bool:
    sum = 0
    for char in str(n):
        sum += int(char)
    return sum