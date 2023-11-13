class Elevador:

    def __init__(self, id):
        self.__id = id
        self.__andar = 1

    def SetAndar(self, andar):
        self.__andar = andar

    def GetAndar(self, andar):
        return self.__andar

    def ChekId(self):
        return (self.__id == id)

    def GetId(self):
        return self.__id

