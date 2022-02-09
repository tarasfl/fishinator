from fishinator_2 import *

ryba_1 = FishInfo("Petro", 18.9, date(2023, 1, 25), "Yerusalym", date(2007, 8, 14))
ryba_2 = FishInfo("klumba", 508.7, date(2034, 12, 5), "dobro", date(2001, 8, 1))
ryba_3 = FishInfo("derevo", 0.03, date(2022, 2, 25), "Zimababve", date(2022, 8, 14))
yashchyk_1 = FishBox(ryba_1, 45, date(2022, 9, 4), 56, 32, 1, 1)
yashchyk_2 = FishBox(ryba_2, 67, date(2022, 7, 4), 56, 32, 1, 1)
yashchyk_3 = FishBox(ryba_3, 154, date(2022, 10, 14), 56, 32, 1, 1)
magazyn = FishShop({yashchyk_3.fish_info.name: [yashchyk_3, ]}, {"Petro": [Fish("Petro", 17.9, date(2023, 1, 25), "Yerusalym", date(2007, 8, 14), 56, 76.1), ]})
magazyn.add_fish_box(yashchyk_1)
magazyn.add_fish_box(yashchyk_3)
magazyn.add_fish_box(yashchyk_2)
magazyn.add_fish_box(yashchyk_3)
magazyn.add_fish_box(yashchyk_2)
magazyn.add_fish_box(yashchyk_1)
magazyn.add_fish(Fish("Petro", 17.9, date(2023, 1, 25), "Yerusalym", date(2007, 8, 14), 56, 76.1))
magazyn.add_fish(Fish("Petro", 17.9, date(2023, 1, 25), "Yerusalym", date(2007, 8, 14), 56, 53.1))
magazyn.add_fish(Fish("Petro", 17.9, date(2023, 1, 25), "Yerusalym", date(2007, 8, 14), 56, 98.1))
print(magazyn.sell_fish("Petro", 90, 1))
print(magazyn)
print(magazyn.get_fresh_fish_names_sorted_by_price())