#Example of Hierarchical Inheritance
class classA:
    pass
class classB(classA):
    pass
class classC(classA):
    pass
class classD(classB):
    pass
class classE(classB):
    pass
class classF(classC):
    pass
class ClassG(classC):
    pass                                
#                                           CLASS A
#                                              |
#                                  ------------------------
#                                  |                     |
#                               CLASS B                 CLASS C
#                                  |                      |
#                      ------------------------   -----------------------------
#                      |                      |   |                           |
#                   CLASS D              CLASS E  CLASS F                  CLASS G