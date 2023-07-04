class Livros:
    def __init__(self, registro, titulo, editora, edicao, fichaCatalogo, idAutor ):
        self.registro = registro
        self.titulo = titulo
        self.editora = editora
        self.edicao = edicao
        self.fichaCatalog = fichaCatalogo
        self.idAutor = idAutor

    def get_registro(self):
        return self.registro

    def set_registro(self, registro):
        self.registro = registro

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_editora(self):
        return self.editora

    def set_editora(self, editora):
        self.editora = editora

    def get_edicao(self):
        return self.edicao

    def set_edicao(self, edicao):
        self.edicao = edicao

    def get_fichaCatalog(self):
        return self.fichaCatalog

    def set_fichaCatalog(self, fichaCatalogo):
        self.fichaCatalog = fichaCatalogo

    def get_idAutor(self):
        return self.idAutor

    def set_autores(self, idAutor):
        self.idAutor = idAutor
