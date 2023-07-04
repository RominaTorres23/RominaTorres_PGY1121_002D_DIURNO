class Container:
    codigo = ''
    producto = ''
    valor = 0
    destino = ''
    impuesto = 0

    def __init__(self):
        codigo = 'AA-01'
        producto = 'Limones'
        valor = 2000000
        destino = 'China'
        impuesto = 20000

#Reglas de negocio

#Codigo 5 digitos, 2 alpha 1 - y 2 isdigit
    def setcodigo(self,codigo):
        if len (codigo) == 5:
            if codigo[0:2].isalpha and codigo[2:3] == '-' and codigo[3:5].isdigit():
                self.codigo = codigo
                return True
            else:
                print("El codigo debe ser en formato AA-01")
        else:
            print("El codigo debe tener 5 carácteres, por ejemplo: AA-01")
            return False

    #Producto: Solo debe exportar Limones, peras y manzanas
    def setproducto(self,producto):
        if producto.upper() == 'LIMONES' or producto.upper() == 'PERAS' or producto.upper() == 'MANZANAS':
            self.producto = producto
            return True
        else:
            print("Ingreso un producto incorrecto, solo exportamos LIMONES, PERAS Y MANZANAS")
            return False
    #Costo: sobre 1200000 hay 10% de impuesto y todo lo demas tiene un 5% de impusto

    def setvalor(self,valor):
            if valor >=900000  and valor <=4500000:
                self.valor = valor
                return True
            else:
                print("El valor debe estar entre $900.000 y $4.500.000")
                return False

