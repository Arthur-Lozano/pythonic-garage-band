class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    def __init__(self, name, type, instrument):
        self.name = name
        self.type = type
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.type}"


class Guitarist(Musician):
    def _init_(self, name):
        super().__init__(name, type="Guitarist", instrument="guitar")

    def play_solo():
        pass

    def get_instrument(self):
        return f"My instrument is {self.type}"


class Bassist:
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Drummer:
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
