def calcVolume(altu, comp, larg):
    volume = (altu*comp*larg)/1000
    return volume

def calcTermo(volume, tempDese, tempAmbi):
    potencia = volume * 0.05 * (tempDese - tempAmbi)
    return potencia

def calcFiltragem(volume):
    litros = volume * 2.5
    return litros
