# -*- coding: utf-8 -*-
class MyDataWrapper():
    def __init__(self, data):
        self.dataSource = data
    
    def interface_doSomeThing(self):
        strReturn ='data from me( I am model) :'+self.dataSource
        print strReturn
        return strReturn
