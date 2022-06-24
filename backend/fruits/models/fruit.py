class Fruit:
    def __init__(self,**kwargs):
        for field in ('name','in_season'):
            setattr(self, field, kwargs.get(field, None))

