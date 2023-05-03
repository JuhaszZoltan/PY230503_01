class Dolgozo:
    def __init__(self, sor:str) -> None:
        darabok:list[str] = sor.strip().split(';')
        self.nev:str = darabok[0]
        self.nem:bool = darabok[1] == 'férfi'
        self.reszleg:str = darabok[2]
        self.belepes:int = int(darabok[3])
        self.ber:int= int(darabok[4])