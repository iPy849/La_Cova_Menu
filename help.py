'''
    Este generador de codigo tiene las siguientes caracteristicas:
    Los lineas que comiencen con:
    '#' se traducen a comentario html
    '/' inician un saltos de lineas en los comentarios del archivo externo
    '*' si hay saltos de lineas, y se encuentra este simbolo entonces para el salto de lineas
    '' linea vacia, se salta

    Formato para poner los productos:
    primera linea: cuantos precios tiene el producto (categoria del producto)
    segunda linea: nombre del producto
    tercera a quinta linea: precio del producto (segun la categoria del producto)
'''
class Cat1Product:

    def __init__(self, name: str):
        self.name = name
        self.min = float(input())

    def roundFloat(self, num: float) -> str:
        try:
            splitted_number = str(num).split('.')
            if len(splitted_number[1]) <= 2:
                if len(splitted_number[1]) < 2:
                    splitted_number[1] += '0'
                return splitted_number[0] + '.' + splitted_number[1]
            else:
                return splitted_number[0] + '.' + splitted_number[1][0] + splitted_number[1][1]
        except:
            raise Exception("Error de formato: Los precios deben tener '.' obligatoriamente")
    
    def __generate_row_code(self) -> str:
        html = f'''
        <div class="row dash-line">
            <div class="col-10 product-name">
                <p>{self.name}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.min)}</p>
            </div>
        </div>
        '''
        return html

    def generate_row(self) -> str:
        return self.__generate_row_code()


class Cat2Product (Cat1Product):

    def __init__(self, name: str):
        super().__init__(name)
        self.max = float(input())
    
    def __generate_row_code(self) -> str:
        html = f'''
        <div class="row dash-line">
            <div class="col-8 product-name">
                <p>{self.name}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.min)}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.max)}</p>
            </div>
        </div>
        '''
        return html

    def generate_row(self) -> str:
        return self.__generate_row_code()
        

class Cat3Product (Cat1Product):

    def __init__(self, name: str):
        super().__init__(name)
        self.mid = float(input())
        self.max = float(input())
    
    def __generate_row_code(self) -> str:
        html = f'''
        <div class="row dash-line">
            <div class="col-6 product-name">
                <p>{self.name}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.min)}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.mid)}</p>
            </div>
            <div class="col-2 price">
                <p>{self.roundFloat(self.max)}</p>
            </div>
        </div>
        '''
        return html

    def generate_row(self) -> str:
        return self.__generate_row_code()


def print_comments(comment: str):
    list(comment).pop(0)
    print(f'<!--{comment}-->')

if __name__ == "__main__":
    is_comment = None
    while True:
        choice = input()
        comment_start = ['#', '/']

        if len(choice) == 0: continue
        elif choice[0] == '+': break
        elif not is_comment and comment_start.__contains__(choice[0]):
            if choice[0] == comment_start[1]:
                is_comment = True
            else:
                print_comments(choice)
            continue
        elif is_comment and choice[0] == '*':
            is_comment = False
            continue
        elif is_comment:
            continue

        choice = int(choice)
        name = input()
        prod = None

        if choice == 1:
            prod = Cat1Product(name)
        elif choice == 2:
            prod = Cat2Product(name)
        else:
            prod = Cat3Product(name)
        
        print(prod.generate_row())


