# Лабораторная работа 4 – Шаблоны проектирования и тестирование  

**Описание**  
Данный репозиторий содержит лабораторную работу, посвящённую изучению **шаблонов проектирования** в Python и методам тестирования (**TDD, BDD, Mock-объекты**).  

## Основные темы лабораторной работы  
### **Шаблоны проектирования**  
- **Порождающий паттерн**: `Builder` (Строитель).  
- **Структурный паттерн** (при необходимости можно добавить).  
- **Поведенческий паттерн** (можно расширить).  

### **Методы тестирования**  
- **TDD (Test-Driven Development)**: модульное тестирование через `unittest`.  
- **BDD (Behavior-Driven Development)**: тестирование с использованием `behave`.  
- **Mock-объекты**: применение `unittest.mock` для подмены вызовов.  

### **Пример предметной области**  
- Имитация **конфигуратора игровых консолей** (PlayStation 5, Xbox Series X, Nintendo Switch).  

---

## Структура репозитория 
lab4/
├── main.py               # Основная логика программы (шаблон проектирования Builder)
├── Test/                 # Папка с модульными тестами (TDD, Mock)
│   ├── TDD.py            # Тестирование методом TDD
│   ├── MOCK.py           # Тестирование с использованием Mock
├── features/             # Папка с BDD-тестами (behave)
│   ├── build.feature     # Описание сценария тестирования
│   ├── steps/            # Шаги тестирования
│   │   ├── steps.py      # Реализация шагов BDD
└── README.md             # Описание проекта

## Запуск лабораторной работы  

### Запуск основного скрипта (`main.py`)
1. Склонировать репозиторий:  
   ```bash
   git clone https://github.com/ArturBab/lab4_design_patterns.git
   cd lab4_design_patterns

2. Запустите main.py:
   ```bash
   python main.py

2.1 Запуск модульных тестов:
   ```bash
   python -m unittest Test/TDD.py
   python -m unittest Test/MOCK.py
```
**Связанные материалы:** 
- [Документация по unittest](https://docs.python.org/3/library/unittest.html)
- [BDD в Python (behave)](https://behave.readthedocs.io/en/latest/)     
