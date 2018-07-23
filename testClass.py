class A(object):
    def __init__(self,id,name,sex):
        self.id=id
        self.name=name
        self.sex=sex
    def run(self):
        print(self.id,self.name,self.sex)