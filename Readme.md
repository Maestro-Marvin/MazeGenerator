# Генератор лабиринтов
## Структура проекта

В проекте реализованы следующие сущности: лабиринт, интерфейс, алгоритмы построения лабиринта и поиск пути.
Реализован абстрактный класс Maze, от него наследуются DfsMaze, KruskalMaze в которых переопределён метод gen.
Графический интерфейс реализован с помощью библиотки pygame в классе Interface.
Взаимодействие алгоритмов построения с интерфейсом происходит через внутренний класс Cell, в котором
храниться информация о цвете и стенах её окаймляющих

## Использование

Точка входа - main.py <br />
Запуск проекта осуществляется через консоль, командой
```sh
python3 main.py [algo] [control] [rows] [cols]
```
algo = [dfs, kruskal] - алгоритм построения лабиринта <br />
control = [auto, handle] - прохождение лабиринта автоматическое или ручное <br />
rows, cols - размеры лабиринта _советую 25 на 30, тогда красиво получается :)_ 

После генерации лабиринта, мышкой выбираются две клетки - начальная и конечная, <br />
далее с помощью стрелочек на клавиатуре можно перемещаться по лабиринту <br />
При выборе прохождения в режиме handle, если не получилось найти путь, можно нажать <br />
на кнопку f тогда путь найдётся автоматически _не забудьте убедиться что раскладка английская_

Пример команды запуска
```sh
python3 main.py kruskal handle 25 30
```

