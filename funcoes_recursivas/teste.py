def recursiva(inicio=0, fim=10):
    
    print(inicio, fim)
    # caso base
    if inicio >= fim:
        return fim 
    
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())