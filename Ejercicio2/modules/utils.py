def ordenar_cristales_mayor_energia(cristales):
    if not isinstance(cristales,list):
        raise ValueError("Se espera una lista de cristales")
    return sorted(cristales,key=lambda c:c.energia_lunar,reverse=True)

def filtrar_cristales_superiores(cristales):
    if not isinstance(cristales,list):
        raise ValueError("se espera una lista de cristales")
    return list(filter(lambda c:c.energia_lunar>=50,cristales))

def mapear_nombres(cristales):
    if not isinstance(cristales,list):
        raise ValueError("se espera una lista de cristales")
    return list(map(lambda c:c.nombre,cristales))

