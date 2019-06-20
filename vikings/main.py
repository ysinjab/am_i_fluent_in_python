import collections
from functools import reduce, partial

from models import Farmer, Ship


def give_farmer_a_weapon(weapon, farmer):
    print(f"{farmer.name} has {weapon}")


give_farmer_a_sword = partial(give_farmer_a_weapon, 'sword')


def create_ship():
    # calling Farmer here like a function return a new object
    farmer_1 = Farmer('Ragnar')
    farmer_2 = Farmer('Rollo', age=25)

    # multiline works for: [], (), {} without \ line continuation escape.
    farmers = [farmer_1,
       farmer_2]
    ship = Ship(farmers)
    print(f"{len(ship)}")
    print(f"{ship[-1]}")
    print(f"{bool(ship)}")
    print(f"{farmer_2.name} is {farmer_2.age} years old")
    print(farmer_2.travel.__annotations__)
    print(farmer_2.travel('Paris'))
    print(give_farmer_a_sword(farmer_2))


def use_tuple_as_record():
    """ Tuples are usually used as tuples and not only as immutable lists
    """
    # tuple unpacking
    name, age, is_farmer = ('Ragnar', 28, True)
    print(f'{name} was {age} and he was a {"farmer" if is_farmer else ""}')
    warriors = []
    # append is a built_in method
    warriors.append(('Ragnar', 28, True))
    warriors.append(('Floki', 28, False))
    warriors.append(('Rollo', 24, True))
    print(warriors)
    ragnar, *others_warriors = warriors
    print(others_warriors)

    # lambda is a User-defined functions
    print(list(map(lambda x: print(f'Hello {x[1]}'), others_warriors)))


def use_tuple_as_record_using_named_tuple():
    Warrior = collections.namedtuple('Warrior', 'name age is_farmer')
    ragnar = Warrior('Ragnar', 28, True)
    print(ragnar)


if __name__ == "__main__":
    create_ship()
    use_tuple_as_record()
    use_tuple_as_record_using_named_tuple()
