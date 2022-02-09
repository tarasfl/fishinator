from datetime import date
from typing import List, Union


class Fish:

    def __init__(self, name_of_fish:str, weight_of_all_fishes: float, price_in_uah_per_kilo: float, body_only: bool, origin_country : str, catch_date) -> None:
        self.name = name_of_fish
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin_country
        self.body_only = body_only
        self.weight = weight_of_all_fishes


class FishShop:
    def __init__(self) -> None:
        self.list_of_fish = {}

    def add_fish(self, fish_name: str, total_weight: float, price_of_fish_in_ukrainian_hryvnia_per_metric_kilogram_firstly_introduced_in_france_in_1840: float, body_only: bool, origin_country: str, catch_date) -> None:
        self.list_of_fish.update({price_of_fish_in_ukrainian_hryvnia_per_metric_kilogram_firstly_introduced_in_france_in_1840: Fish(name_of_fish=fish_name, weight_of_all_fishes=total_weight, price_in_uah_per_kilo=price_of_fish_in_ukrainian_hryvnia_per_metric_kilogram_firstly_introduced_in_france_in_1840, body_only=body_only, origin_country=origin_country, catch_date=catch_date)})

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        self.list_of_fish=dict(sorted(self.list_of_fish.items()))
        buffer_list = self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        sorted_list = []
        for i in buffer_list:
            sorted_list.append(i.name)
        return sorted_list

    def sell_fish(self, fish_name: str, weight: float) -> float:
        self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        for i in self.list_of_dict_elements:
            if weight <=i.weight:
                if(i.name==fish_name):
                    total_price = weight*i.price_in_uah_per_kilo
                    self.list_of_fish.update({i.price_in_uah_per_kilo: Fish(i.name, i.weight-weight, i.price_in_uah_per_kilo, i.body_only, i.origin, i.catch_date)})
                    return total_price
            else:
                print("you want too much")
                return 0

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        for i in self.list_of_dict_elements:
            if ( date.today()- i.catch_date).days>10:
                del self.list_of_fish[i.price_in_uah_per_kilo]
            else:
                continue
        buffer_list = self.list_of_dict_elements = [value for value in self.list_of_fish.values()]
        sorted_list = []
        for i in buffer_list:
            sorted_list.append(i.name)
        return sorted_list


class Seller:
    pass


class Buyer:
    pass


h = FishShop()
h.add_fish("Petro", 17.8, 18.0, True, "hukanc", date(2022, 1, 25))
h.add_fish("lystya", 17.8, 11.0, True, "hukanc",  date(1096, 8, 15))
h.add_fish("ceaser", 17.8, 13.0, True, "hukanc",  date(2019, 1, 15))
h.add_fish("chomu", 17.8, 7.0, True, "hukanc",  date(2022, 1, 23))
print(h.get_fish_names_sorted_by_price())
print(h.sell_fish("petro", 4))
print(h.list_of_fish[18.0].weight)
print(h.cast_out_old_fish())