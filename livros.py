class Livro:
    def __init__(self, titulo: str, qtd_paginas: int, paginas_lidas: int):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.paginas_lidas = paginas_lidas

    def get_titulo(self) -> str:
        return self.titulo

    def set_titulo(self, titulo: str) -> None:
        self.titulo = titulo

    def get_qtd_paginas(self) -> int:
        return self.qtd_paginas

    def set_qtd_paginas(self, qtd_paginas: int) -> None:
        self.qtd_paginas = qtd_paginas

    def get_paginas_lidas(self) -> int:
        return self.paginas_lidas

    def set_paginas_lidas(self, paginas_lidas: int) -> None:
        self.paginas_lidas = paginas_lidas

    def verificar_progresso(self) -> None:
        if self.qtd_paginas == 0:
            print("O livro não tem páginas registradas.")
        else:
            progresso = (self.paginas_lidas / self.qtd_paginas) * 100
            print(f"Você já leu {progresso:.2f}% do livro.")
