from models import BaristaDrink, ColdBrew, \
                     Latte, add_espresso_shots_to_latte, \
                     add_espresso_shots_to_cold_brew

if __name__ == "__main__":
    print(BaristaDrink('Yasser', ColdBrew()).prepare())
    print(BaristaDrink('Yasser', Latte()).prepare())

    BaristaDrink('Yasser', add_espresso_shots_to_latte)\
        .prepare_with_function()
    BaristaDrink('Yasser', add_espresso_shots_to_cold_brew)\
        .prepare_with_function() 