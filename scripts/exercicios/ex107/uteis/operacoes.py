def metade (n):
    m = n/2
    
    return m

def dobro (n):
    m = n*2
    
    return m

def aumentar (n, q):
    '''n recebe o valor que você quer aumentar
    q recebe o percentual que você deseja aumentar
    m retorna o valor aumentado no percentual q
    '''
    m = n + (n*q/100)
    
    return m

def diminuir (n, q):
    '''
    n recebe o valor que você deseja diminuir
    
    q recebe o percenteual que você deseja diminuir
    
    m retorna o valor diminuido o percentual q
    '''
    m = n - (n*q/100)
    
    return m
    