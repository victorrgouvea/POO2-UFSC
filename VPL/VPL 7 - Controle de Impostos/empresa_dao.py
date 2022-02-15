import pickle
from empresa import Empresa


class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        f = open(self.__datasource, 'wb')
        pickle.dump(self.__object_cache, f)
        f.close()

    def __load(self):
        f = open(self.__datasource, 'rb')
        self.__object_cache = pickle.load(f)
        f.close()

    def add(self, empresa: Empresa):
        key = empresa.cnpj
        self.__object_cache[key] = empresa
        self.__dump()

    def remove(self, empresa):
        try:
            self.__object_cache.pop(empresa.cnpj)
            self.__dump()
        except:
            print("Essa empresa não existe")

    def get(self, cnpj):
        return self.__object_cache[cnpj]

    def get_all(self):
        list = []
        for key in self.__object_cache.keys():
            list.append(self.__object_cache[key])
        return list

    @property
    def object_cache(self):
        return self.__object_cache

'''
a = EmpresaDAO()
b = Empresa(123123, 'aaa')
print(b.cnpj)
a.add(b)
print(a.get_all())
'''