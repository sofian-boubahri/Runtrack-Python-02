while True:
    try:
        n = int(input('Entrer un entier supérieur à zéro (N):'))
        if n > 0:
            break
        else:
            print("L'entier doit être supérieur à zéro. Essayez à nouveau.")  
    except ValueError:
        print("Ce n'est pas un entier valide. Essayez à nouveau.")


a = 1
while a <= n:  
    print("\nLa table de", a)  
    b = 1 
    while b <= 10:  
        print(a, "x", b, "=", a * b)
        b += 1
    a += 1  
