from datetime import date, datetime


def find_closest_value(value: int, values: list[float]) -> int:
    sorted_values =  sorted(values, key=float)
    previous_value= 0
    for i in sorted_values:
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

    def __str__(self) -> str:
        return f'name:{self.name} price_in_uah_per_kilo:{self.price_in_uah_per_kilo} due_date:{self.due_date} origin:{self.origin} catch_date:{self.catch_date}'

    def __repr__(self) -> str:
        return self.__str__()

class Fish(FishInfo):
    def __init__(self, name: str, price_in_uah_per_kilo: float, due_date: datetime, origin: str, catch_date: datetime, age_in_mounth: float, weight: float) -> None:
        super().__init__(name, price_in_uah_per_kilo, due_date, origin, catch_date)
        self.age_in_mounth = age_in_mounth
        self.weight = weight

    def __str__(self) -> str:
        return f'{super().__str__()}, age_in_mounth: {self.age_in_mounth}, weight: {self.weight}'

    def __repr__(self) -> str:
        return self.__str__()



class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, lenth: float, width: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.lenth = lenth
        self.width = width
        self.is_alive = is_alive

    def __str__(self) -> str:
        return f'fish_info: [{self.fish_info.__str__()}] fish_info: {self.fish_info}  weight: {self.weight}   package_date: {self.package_date} height: { self.height}  lenth: {self.lenth}   width: {self.width}   is_alive: {self.is_alive}'

    def __repr__(self) -> str:
        return self.__str__()

class FishShop:
    def __init__(self, fish_boxes: dict[str, list[FishBox]], fishies: dict[str, list[Fish]]) -> None:
        self.fish_boxes = fish_boxes
        self.fishies = fishies

    def __str__(self) -> str:
        return f'boxes:{self.fish_boxes.__str__()}   fishies:{self.fishies.__str__()} \n'
    
    def __repr__(self) -> str:
        return self.__str__()

    def add_fish(self, fish: Fish) -> None:
        keys = [key for key in  self.fishies]
        if keys.count(fish.name) > 0:
             l = self.fishies[fish.name]
             l.append(fish)
             self.fishies.update({fish.name: l})
        else:
            self.fishies.update({fish.name: [fish, ]})
        

    def add_fish_box(self, fish_box: FishBox) -> None:
        keys = [key for key in  self.fish_boxes]
        if keys.count(fish_box.fish_info.name) > 0:
            self.fish_boxes[fish_box.fish_info.name].append(fish_box)
        else:
            self.fish_boxes.update({fish_box.fish_info.name: [fish_box, ]})

    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> tuple:
        if is_fresh and self.fishies[name]:
            list_of_fishies =  self.fishies[name]
            weight_list = [value.weight for value in list_of_fishies]
            fish_weight = find_closest_value(weight, weight_list)
            del list_of_fishies[weight_list.index(fish_weight)]
            total_price = self.fishies[name][0].price_in_uah_per_kilo * fish_weight
            self.fishies.update({name: list_of_fishies})   
            return (name, fish_weight, total_price)
        elif not is_fresh and self.fish_boxes[name]:
            list_of_fishies =  self.fish_boxes[name]
            weight_list = [value.weight for value in list_of_fishies]
            price_of_fish = self.fish_boxes[name][0].fish_info.price_in_uah_per_kilo
            for i in weight_list:
                if weight-i>=0:
                    del list_of_fishies[0]
                    continue
                else:
                    list_of_fishies[0].weight = i-weight
                    break
            total_price = price_of_fish * weight
            self.fish_boxes.update({name: list_of_fishies})  
            return((name, weight, total_price))
        else:
            print('there not such fish')
            return (name, 0, 0)
    
    def get_frozen_fish_names_sorted_by_price(self) -> list(tuple()):
        fish_list = [value for value in self.fish_boxes.values()]
        buffer_list = []
        for i in fish_list:
           buffer_list.extend(i)
        fin_list = [(value.fish_info.name, value.fish_info.price_in_uah_per_kilo) for value in buffer_list]
        buffer_list = []
        prev_value = fin_list[0][1]
        for i in fin_list:
            if i[1] >= prev_value:
                buffer_list.append(i)
            elif i[1] < prev_value:
                buffer_list.insert(0, i)
                prev_value = i[1]
        return buffer_list
