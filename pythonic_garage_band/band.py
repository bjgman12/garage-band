class Band:
    band_list = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.band_list.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


    def play_solos(self):
        temp = []
        for member in self.members:
            temp.append(member.play_solo())

        return temp
    
    @classmethod
    def to_list(cls):
        return cls.band_list

class Musician:
    def play_solo(self):
        if self.get_instrument() == 'guitar':
            return 'face melting guitar solo'
        elif self.get_instrument() == 'bass':
            return 'bom bom buh bom' 
        else:
            return 'rattle boom crash'   

class Guitarist(Musician):
    def  __init__(self,name):
        self.name = name

    def get_instrument(self):
        return 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    

class Bassist(Musician):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
        

class Drummer(Musician):
    def __init__(self,name):
        self.name = name
    
    def get_instrument(self):
        return 'drums'
    
        
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'