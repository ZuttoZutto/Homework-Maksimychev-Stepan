"""Task 3. Anomalie de funxon"""


def anomalie(s1, s2):
    print(f"{s1[:2][::-1] + s1[2:]}-{s2[:2][::-1] + s2[2:]}")


s1, s2 = input(), input()
anomalie(s1, s2)