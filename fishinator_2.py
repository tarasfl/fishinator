from datetime import date, datetime


def find_closest_value(value: int, values: list[float]) -> int:
    previous_value= 0
    for i in values:
        current_difference = i-value
        if abs(previous_value-value)>abs(current_difference):
            previous_value=i
            continue
        elif i == previous_value:
            continue
        elif abs(current_difference)>=abs(previous_value-value):
            return previous_value
    return values[(len(values)-1)]
        


class FishInfo:
    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime, origin: str, catch_date: datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.due_date = due_date
        self.origin = origin
        self.catch_date = catch_date


class Fish(FishInfo):
    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime, origin: str, catch_date: datetime, age_in_mounth: float, weight: float) -> None:
        super().__init__(name, price_in_uah_per_kilo, due_date, origin, catch_date)
        self.age_in_mounth = age_in_mounth
        self.weight = weight

    def __eq__(self, other) -> bool:
        return self.name == other.name



class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, lenth: float, width: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.lenth = lenth
        self.width = width
        self.is_alive = is_alive

    def __eq__(self, other) -> bool:
        return self.name == other.name


class FishShop:
    def __init__(self, fish_boxes: dict[str, list[FishBox]], fishies: dict[str, list[Fish]]) -> None:
        self.fish_boxes = fish_boxes
        self.fishies = fishies

    def add_fish(self, fish: Fish) -> None:
        keys = [key for key in  self.fishies]
        if keys.count(fish.name) > 0:
             l = self.fishies[fish.name]
             l.append(fish)
             self.fishies.update({fish.name: l})
        else:
            self.fishies.update({fish.name: fish})
        

    def add_fish_box(self, fish_box: FishBox) -> None:
        keys = [key for key in  self.fish_boxes]
        if keys.count(fish_box.fish_info.name) > 0:
            self.fish_boxes[fish_box.fish_info.name].append(fish_box)
        else:
            self.fish_boxes.update({fish_box.fish_info.name: fish_box})

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> tuple:
        if is_fresh:
            list_of_fishies =  self.fishies[name]
            weight_list = [value.weight for value in list_of_fishies]
            fish_weight = find_closest_value(weight, sorted(weight_list, key=float))
            del list_of_fishies[weight_list.index(fish_weight)]
            total_price = self.fishies[name][0].price_in_uah_per_kilo * fish_weight
            self.fishies.update({"name": list_of_fishies})   
            return (name, fish_weight, total_price)
        else:
            pass
