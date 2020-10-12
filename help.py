class Cat1Product:

    def __init__(self, name: str):
        self.name = name
        self.cuc = float(input())
        self.cup = float(input())
    
    def __generate_row_code(self) -> str:
        html = '''
        <div class="row mb-0 dash-line mx-1">
            <div class="col-6 product-name">
                <p>{}</p>
            </div>
            <div class="col price">
                <p>{}</p>
            </div>
            <div class="col price">
                <p>{}</p>
            </div>
        </div>

        '''.format(self.name, self.cuc, self.cup)
        return html

    def generate_row(self) -> str:
        return self.__generate_row_code()


class Cat2Product (Cat1Product):

    def __init__(self, name: str):
        super().__init__(name)
        self.grcuc = float(input())
        self.grcup = float(input())
    
    def __generate_row_code(self) -> str:
        html = '''
        <div class="row mb-0 dash-line mx-1">
            <div class="col-4 product-name">
                <p>{}</p>
            </div>
            <div class="col-2 price">
                <p>{}</p>
            </div>
            <div class="col-2 price">
                <p>{}</p>
            </div>
            <div class="col-2 price">
                <p>{}</p>
            </div>
            <div class="col-2 price">
                <p>{}</p>
            </div>
        </div>

        '''.format(self.name, self.cuc, self.cup, self.grcuc, self.grcup)
        return html
    
    def generate_row(self) -> str:
        return self.__generate_row_code()
        

class Cat3Product (Cat1Product):

    def __init__(self, name: str):
        super().__init__(name)
        self.medcuc = float(input())
        self.medcup = float(input())
        self.grcuc = float(input())
        self.grcup = float(input())
    
    def __generate_row_code(self) -> str:
        html = '''
        <div class="dash-line">
            <div class="product-name mx-1 pt-1">
                <p>{}</p>
            </div>
            <div class="row mx-1">
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Pequeño</h2>
                                    <h2>CUC</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Pequeño</h2>
                                    <h2>CUP</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Mediana</h2>
                                    <h2>CUP</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Mediana</h2>
                                    <h2>CUP</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Grande</h2>
                                    <h2>CUC</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2 product-name">
                    <div class="menu-price">
                        <div class="four-cols">
                            <div class="menu-price">
                                <div class="four-cols">
                                    <h2>Grande</h2>
                                    <h2>CUP</h2>
                                    <p class="price">{}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''.format(self.name, self.cuc, self.cup, self.medcuc, self.medcup, self.grcuc, self.grcup)
        return html
    
    def generate_row(self) -> str:
        return self.__generate_row_code()
        

if __name__ == "__main__":
    while True:
        name = input()

        if name == '':
            break

        prod = Cat3Product(name)
        print(prod.generate_row())


