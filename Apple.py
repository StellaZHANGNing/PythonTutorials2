from EcnoModel import EconModelClass
class MyModelClass(EconModelClass):
    
    def settings(self):
        pass

    def setup(self):
        pass

    def allocate(self):
        pass        

mymodel = MyModelClass(name='mymodel')