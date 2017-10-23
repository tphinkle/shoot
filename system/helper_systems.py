class Subject(object):
    def __init__(self):
        self.observers = []

    def AddObserver(self, observer):
        self.observers.append(observer)

    #def RemoveObserver(self, remove_observer):
        #self.observers = [observer for observer in self.observers if observer not remove_observer]

    def NotifyObservers(self, entity, event):
        for observer in self.observers:
            observer.OnNotify(entity, event)


class Observer(object):
    def __init__(self):
        pass

    def OnNotify(self, entity, event):
        '''
        This is a pure virtual method
        Overwritten by any class inheriting Observer
        '''
        
        pass
