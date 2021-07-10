def obliczSilnie(num):
    if (num == 1):
        return 1
    return num * obliczSilnie(num - 1);

print(obliczSilnie(3));
print(obliczSilnie(2));
print(obliczSilnie(1));
