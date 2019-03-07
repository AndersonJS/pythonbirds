class Pessoa:
    pass

# Para importar uma classe e semelhante a uma função:
from OO.pessoa import Pessoa
p = Pessoa()
type(p)

# <class 'OO.pessoa.Pessoa'>

print(__name__)
