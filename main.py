from abc import ABC, abstractmethod
from enum import Enum, auto


class Consoles_Brands(Enum):
    PlayStation = auto()
    XBOX = auto()
    Nintendo = auto()
    Steam = auto()

class Cpu_Type(Enum):
    cpu_PS = auto()
    cpu_Xbox = auto()
    cpu_Nvidia = auto()

class Size_Memory(Enum):
    S512 = auto()
    s825 = auto()
    s64 = auto()

class Gpu_Type(Enum):
    AMD_Radeon = auto()
    Intel_Celeron = auto()
    Nvidia_gpu = auto()
    Nvidia_gpu88 = auto()

class Consoles:
    def __init__(self, name):
        self.name = name
        self.brand = None
        self.cpu = None
        self.memory = None
        self.gpu = None
        self.cost = None

    def __str__(self):
       info: str = f"Название игровой консоли: {self.name} \n" \
                   f"{self.brand} \n" \
                   f"{self.cpu} \n" \
                   f"{self.memory} \n" \
                   f"{self.gpu} \n" \
                   f"Cost: {self.cost} рублей"

       return info


####################### ШАБЛОН ПРОЕКТИРОВАНИЯ - СТРОИТЕЛЬ ##########################
class Builder(ABC):

    @abstractmethod
    def add_brand(self) -> None: pass

    @abstractmethod
    def add_cpu(self) -> None: pass

    @abstractmethod
    def add_memory(self) -> None: pass

    @abstractmethod
    def add_gpu(self) -> None: pass

#################################################################################


class PlayStation5(Builder):

    def __init__(self):
        self.console = Consoles("PlayStation 5 / PS5")
        self.console.cost = 105000

    def add_brand(self) -> None:
        self.console.brand = Consoles_Brands.PlayStation

    def add_cpu(self) -> None:
        self.console.cpu = Cpu_Type.cpu_PS

    def add_memory(self) -> None:
        self.console.memory = Size_Memory.s825

    def add_gpu(self) -> None:
        self.console.gpu = Gpu_Type.AMD_Radeon

    def get_lap(self) -> Consoles:
        return self.console


class Xbox_series_X(Builder):

    def __init__(self):
        self.console = Consoles("Xbox series X / XSX")
        self.console.cost = 50000

    def add_brand(self) -> None:
        self.console.brand = Consoles_Brands.XBOX

    def add_cpu(self) -> None:
        self.console.cpu = Cpu_Type.cpu_Xbox

    def add_memory(self) -> None:
        self.console.memory = Size_Memory.s825

    def add_gpu(self) -> None:
        self.console.gpu = Gpu_Type.AMD_Radeon

    def get_lap(self) -> Consoles:
        return self.console


class Nintendo_Switch(Builder):

    def __init__(self):
        self.console = Consoles("Nintendo Switch / NS")
        self.console.cost = 38840

    def add_brand(self) -> None:
        self.console.brand = Consoles_Brands.Nintendo

    def add_cpu(self) -> None:
        self.console.cpu = Cpu_Type.cpu_Nvidia

    def add_memory(self) -> None:
        self.console.memory = Size_Memory.s64

    def add_gpu(self) -> None:
        self.console.gpu = Gpu_Type.Nvidia_gpu

    def get_lap(self) -> Consoles:
        return self.console


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_console(self):
        if not self.builder:
            raise ValueError("Builder didn't set")

        self.builder.add_brand()
        self.builder.add_cpu()
        self.builder.add_memory()
        self.builder.add_gpu()


def check_cost(name1):
    for it1 in (PlayStation5, Xbox_series_X, Nintendo_Switch):

        director1 = Director()
        builder1 = it1()

        director1.set_builder(builder1)

        director1.make_console()

        console1 = builder1.get_lap()

        if console1.name == name1:

            return console1.cost

def sum_cost(x):
    for it1 in (PlayStation5, Xbox_series_X, Nintendo_Switch):
        director1 = Director()
        builder1 = it1()
        director1.set_builder(builder1)
        director1.make_console()
        console1 = builder1.get_lap()
        x = x + console1.cost
    return x


if __name__ == "__main__":
    print("\nИгровые консоли:\n")
    director = Director()

    for it in (PlayStation5, Xbox_series_X, Nintendo_Switch):

        builder = it()
        director.set_builder(builder)

        director.make_console()
        console = builder.get_lap()

        print(console)
        print('\n//////////////////\n')

    name = "PS5"
    print(name, "Cost:", check_cost(name))

    x = 0
    print('Полная стоимость всех рассмотренных консолей = ', sum_cost(x), 'руб.')
