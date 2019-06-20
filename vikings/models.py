import collections


class Farmer:

    def __init__(self, name, *args, age=None, **kwargs):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __repr__(self):
        return f"I am a farmer and my name is: {self._name}"

    def travel(self, destination: str, days: 'travel not more than 90 days' = 30)\
         -> str:
        print(f"Me {self._name} will travel to {destination} for {days}")
        return 'traveld'


class Ship:
    _warriors = []

    def __init__(self, warriors):
        self._warriors = warriors

    def __len__(self):
        return len(self._warriors)

    def __getitem__(self, position):
        return self._warriors[position]

    def __bool__(self):
        return bool(self._warriors)
