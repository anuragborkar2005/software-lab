import random, time
import duplicates as slow
import duplicates_optimized as fast
random.seed(42)
for n in (1000, 5000, 10000):
    data = [random.randint(1, n) for _ in range(n)]
    t0 = time.perf_counter(); r1 = slow.find_duplicates_brute_force(data); t1 = time.perf_counter()
    t2 = time.perf_counter(); r2 = fast.find_duplicates(data); t3 = time.perf_counter()
    assert sorted(r1) == sorted(r2)
    print(f"n={n} | original {t1-t0:.6f} s | optimized {t3-t2:.6f} s")