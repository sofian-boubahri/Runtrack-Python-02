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
while a <= 10:  
    print(n, "x", a * 7, "=", n * (a * 7))  
    a += 1  
