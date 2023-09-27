import random
def millerRabin(n):
    test_time=10
    if n < 3 or n % 2 == 0:
        return n == 2
    u, t = n - 1, 0
    while u % 2 == 0:
        u = u // 2
        t = t + 1
    # test_time 为测试次数,建议设为不小于 8
    # 的整数以保证正确率,但也不宜过大,否则会影响效率
    for i in range(test_time):
        a = random.randint(2, n - 1)
        v = pow(a, u, n)
        if v == 1:
            continue
        s = 0
        while s < t:
            if v == n - 1:
                break
            v = v * v % n
            s = s + 1
        # 如果找到了非平凡平方根，则会由于无法提前 break; 而运行到 s == t
        # 如果 Fermat 素性测试无法通过，则一直运行到 s == t 前 v 都不会等于 -1
        if s == t:
            return False
    return True

x=int(input("输入："))
print("是否为素数：",millerRabin(x))