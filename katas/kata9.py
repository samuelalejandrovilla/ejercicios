def promedio(lista_de_valores):
    suma= sum(lista_de_valores)
    return suma/len(lista_de_valores)
def informe(tanque1, tanque2, tanque3):
    return f'''
    Tanque1 = {tanque1}
    Tanque2 = {tanque2}
    Tanque3 = {tanque3}
promedio = {promedio([tanque1, tanque2, tanque3])}
    
    '''
print(promedio(10, 20 , 30))