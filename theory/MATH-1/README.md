<style>
    h1, h2, h3, h4, h5, h6 { color: darkorange;  font-weight: 700; }
    h1 { filter: hue-rotate(0deg); }
    h2 { filter: hue-rotate(10deg); }
    h3 { filter: hue-rotate(20deg); }
    h4 { filter: hue-rotate(30deg); }
    h5 { filter: hue-rotate(40deg); }

    strong {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding-left: 0.2rem;
        padding-right: 0.2rem;
        filter: hue-rotate(40deg);
    }

    em {
        border-bottom: 2px dotted #ccc;
    }

    a, a:hover {
        text-decoration: underline;
    }

    @media (prefers-color-scheme: dark) {
        body { color: #ccc; }
        strong { border-color: #ccc; }
        em { border-color: #ccc; }
        img { background-color: rgba(255, 255, 255, 0.75) }
        a, a:hover { color: Violet; }
    }
    
    @media (prefers-color-scheme: light) {
        body { color: #333; }
        strong { border-color: #333; }
        em { border-color: #333; }
        /* img { background-color: rgba(0, 0, 0, 0.1) } */
        a, a:hover { color: DodgerBlue; }
    }
</style>

# Математика в ML (part 1)

## Линейная алгебра

Это раздел математики, который изучает объекты линейно природы:
- векторы
- матрицы
- системы линейных уравнений

### Кванторы и символы

- `∀` квантор всеобщности — любой, всякий, для любого
- `∃` квантор существования — существует, найдется
- `∃!` квантор существования и единственности — существует единственный
- `∄` квантор отсутствия — не существует, отсутствует
- `=>` знак импликации — следует, влечет, вытекает
- `<=>` знак равносильности — если и только если
- `:` — такой что
- `|` — при условии что
- `∈` — принадлежит
- `ℝ` — множество действительных чисел
- `⨂` — тензорное произведение векторов

### Векторы

#### Геометрическая интерпретация

Векторы принято начинать из точки `O`.

![](./images/MATHML_md1_2_6.png)

Множество всех возможных векторов `S` называют *векторным пространством*. Говорят: вектор `s` принадлежит пространству `S`. Записывают: `s ∈ S`.

**Нулевым вектором** называют вектор, у которого все координаты равны нулю: `w = (0, 0)`

#### Базовые операции с векторами

##### Сложежние

```python
a = np.array([10, 8, 5, 1])
b = np.array([5, 15, 9, 7])
a + b
### array([15, 23, 14,  8])
a - b
### array([ 5, -7, -4, -6])
```

##### Умножение на скаляр

```python
a = np.array([120, 45, 68])
omega = 0.2
c = a * omega
c
### array([24. ,  9. , 13.6])
```

##### Линейная комбинация

Это сумма векторов, каждый из которых умножен на некий коэфициент (скаляр)

```python
a = np.array([1, 5, 0])
b = np.array([2, 3, 5])
c = np.array([4, 2, 2])

w1, w2, w3 = 3, -1, 0
y = a*w1 + b*w2 + c*w3 # [ 1, 12, -5]
```

#### Нулевая линейная комбинация

— это такая, которая дает в результате нулевой вектор. Это особый случай, и он представляет для нас интерес. Нам будет важно дать ответ на вопрос, можно ли подобрать такие коэфициенты `w`, чтобы получить нулевую комбинацию из векторов `s`?

Один из способов этого добиться — сделать все коэфициенты нулями. Но это тривиальный случай, и нам он не интересен.

#### Линейная (не)зависимость

Допустим мы нашли такие коэфицианты `w` при который наши векторы `s` дают нулевую линейную комбинацию. Тогда наши векторы будут называться **линейно зависимыми** и будут лежать *в одной (гипер)плоскости*.

В противном случае наши векторы будут называться **линейно независимыми** и будут лежать *в разных (гипер)плоскостях*.

Понятие линейной зависимости векторов является *одним из главных* в линейной алгебре.


#### Скалярное произведение

Это число, равное сумме координат векторов, умноженных друг на друга. Есть две формы математической записи: `(a, b)` или `a・b`

(Геометрически — это площадь, полученная умножением одного вектора на проекцию другого. Но при этом СП *может быть отрицательным числом*.)

```python
a = np.array([3, 15, 10, 20])
b = np.array([2, 12, 85, 0.6])
## 3*2 + 15*12 + 10*85 + 20*0.6 = 1048

print('Скалярное произведение векторов `a` и `b`')
print('в Python вычисляется с помощью метода `np.dot`')
print(f'np.dot(a, b) = {np.dot(a, b)}')

print('\nТакже есть сокращенная запись этой команды:')
print(f'a@b = {a@b}')
```

#### Свойства скалярного произведения

##### Линейность (дистрибутивность)
`(a + b)・(c + d) = a・(c + d) + b・(c + d) = a・c + a・d + b・c + b・d`

##### Связь с углом между векторами
`a・b = |a||b|cos α`\
`cos α = a・b / |a||b|`

##### Определение ортогональности векторов
Поскольку `cos 90° = 0`, то скалярное произведение ортогональных векторов будет равно нулю.

`|a||b|cos 90° = 0`

##### Определение длины вектора
Если умножить вектор на себя то косинус можно не учитывать поскольку `cos 0° = 1`

`a・a = |a||a| => |a| = √(a・a)`

#### Норма вектора и нормирование

**Нормой вектора** `v` является такой вектор `n`, который имеет длину `1` и то же направление, что и `v`.

Для получения нормы производят деление вектора на его длину. Эта операция есть **нормирование** вектора.

```python
a = np.array([1, 3, 10])

# длина вектора вычисляется с помощью `np.linalg.norm`
a_len = np.linalg.norm(a)
print(a_len) # 10.488088481701515

# нормирование
a_norm = a / a_len
print(a_norm) # [0.09534626 0.28603878 0.95346259]

# длина нормы
a_norm_len = np.linalg.norm(a_norm)
print(a_norm_len) # 1.0
```

#### Векторная запись линейной регрессии

![](./images/linreg.png)

### Матрицы

**Матрица** — это структура, состоящая из чисел, записанных по строкам и столбцам. Или просто *таблица чисел*. В линейной алгебре матрицы обозначаются большими латинскими буквами.

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(A, type(A))
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] <class 'numpy.ndarray'>

B = np.matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(B, type(B))
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]] <class 'numpy.matrix'>
```

#### Классификация матриц

##### По форме

- прямоугольные (высокие и длинные)
- квардатные
- вектор столбец
- вектор строка

##### По содержанию

- нулевая матрица (обозначается `Null`)
- матрица единиц (все элементы — единицы)
- едничная матрица (обозначается `E`)
- треугольная (нижне/верхне)
- симметричная
- диагональная (все элементы кроме главной диагонали — нули, обозначается `diag(α₁, ..., αₙ)`)
- скалярная или шаровая (диагональная М. у которой все элементы на главной диагонали равны, обозначается `diag(α, ..., α)`)

#### Создание матриц на Python

```python
np.zeros((2,3))
# array([[0., 0., 0.],
#        [0., 0., 0.]])

np.ones((2,3))
# array([[1., 1., 1.],
#        [1., 1., 1.]])

np.eye(3)
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

np.diag([3, 5, 6])
# array([[3, 0, 0],
#        [0, 5, 0],
#        [0, 0, 6]])

np.random.randint(0, 10, (3, 3)) # from, to, size
# array([[7, 8, 6],
#        [5, 6, 2],
#        [2, 0, 8]])

np.random.random((2,2))
# array([[0.38304886, 0.90856077],
#        [0.75508134, 0.11381542]])
```

#### Базовые действия над матрицами

##### Сложение

Матрицы складываются поэлементно, так же как векторы. Они должны быть одной размерности.

##### Умножение на скаляр

Матрицы умножаются на скаляр так же как векторы.

##### Поэлементное умножение

Матрицы одного размера можно умножить поэлементно:\
`C = A ⊙ B`

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

B = np.array([
    [3, 0, 1],
    [1, -2, 0],
])

print(A * B)
# [[  3   0   3]
#  [  4 -10   0]]
```

##### Транспонирование

— это переворачивание матрицы: столбцы становятся строками, а строки — столбцами. Транспонированная матрица обозначается буквой `ᵀ`. Двойное транспонирование дает исходную матрицу:

`(Aᵀ)ᵀ = A`

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]

print(A.T.T)
# [[1 2 3]
#  [4 5 6]]
```

#### Продвинутые действия над матрицами

##### Умножение матриц

Произведение матриц не коммутативно: `A・B ≠ B・A`

Нельзя перемножить две произвольные матрицы `A` и `B`. Нужно чтобы кол-во столбцов `A` было равно кол-ву строк `B`.

```python
A = np.matrix([[1, 2], [3, 4]])
# [[1 2]
#  [3 4]]

B = np.matrix([[100], [200]])
# [[100]
#  [200]]

np.dot(A, B)
# [[ 500] — (1, 2)・(100, 200) = 100 + 400
#  [1100]] — (3, 4)・(100, 200) = 300 + 800
```

##### Деление матриц

Об этом читай в разделе "Обратная матрица"

##### Тензорное произведение векторов

Берут два вектора одинаковой размерности `n` и перемножают их как две матрицы размерами `(n, 1)` и `(1, n)`. В результате получается квадратная матрица порядка `n`.

У тензорного произведения есть специальное обозначение — `⨂`

#### Умножение специальных матриц

##### Умножение на нулевую матрицу

Дает нулевую матрицу:\
`A・Null = Null`

##### Умножение на единичную матрицу

Дает исходную матрицу:\
`A・E = A, E・A = A`

##### Умножение на шаровую (скалярную) матрицу

Дает исходную матрицу, умноженную на скаляр:\
`A・diag(α, ..., a) = αA`

##### Умножение на диагональную матрицу

При умножении `A` на диагональную матрицу `diag(α₁, ..., αₙ)`, каждый столбец `A` умножается на соответствующий коэфициент `α₁, ..., αₙ`.

При умножении д. матрицы на `A` каждая строка умножается на соответствующий коэфициент.

![](./images/MATHML_md1_6_13.png)

#### Умножение транспонированных матриц

`(A・B)ᵀ = Bᵀ・Aᵀ`

`(A・B・C)ᵀ = (A・(B・C))ᵀ = (B・C)ᵀ・Aᵀ  = Cᵀ・Bᵀ・Aᵀ`

#### Матрица Грама

**Матрицей Грама** называют матрицу, умноженную на транспонированную себя. Она всегда квадратная и симметричная.

`G = X・Xᵀ`

или

`G = Xᵀ・X`

#### Деление матриц или обратная матрица

##### Обратное число

Можно ли делть матрицы? Чтобы ответить на этот вопрос нужно вспомнить про *обратное число* — это такое число, которое дает единицу при умножении на исходное.

`a * 1/a = a * a⁻¹ = 1`

С помощью `a⁻¹` можно разделить на `a` без использования деления.

`b / a = b * a⁻¹`

*Обратные числа есть у всех чисел, кроме нуля.*

##### Обратная матрица

**Обратной матрицей** для `A` будет такая матрица `A⁻¹`, которая при умножении на `A` даст единичную матрицу.

`A・A⁻¹ = E`

или

`A⁻¹・A = E`

❗️И исходная и обратная матрицы могут быть только квадратными.

❗️Обратная матрица может быть только одна.

```python
A = np.matrix([
    [1, 2],
    [3, 5]])

A_inv = np.linalg.inv(A)

print(A_inv)
# [[-5.  2.]
#  [ 3. -1.]]

print(np.round(A @ A_inv))
# [[1. 0.]
#  [0. 1.]]
```

#### Определитель матрицы

Это числовая характеристика *квадратных* матриц, которая показывает степень *вырожденности* матрицы — чем ближе к нулю, тем больше вырожденность. Обозначается `det(A)` или `|A|`

##### Вычисление

Для матрицы порядка 2 это разность произведений главной и побочной диагоналей.

![](./images/det.formula.png)

Но мы не будем считать его вручную.

```python
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

np.linalg.det(A)
# 27.0
```

##### Свойстваа

- Определитель единичной матрицы равен `1`.
- Определитель диагональной матрицы равен произведению элементов главной диагонали.
- Определитель не меняется при транспонировании: `det(A) = det(Aᵀ)`
- Определитель произведения матриц: `det(A・B) = det(A)・det(B)`
- Определитель обратной матрицы является обратным числом определителя исходной: `det(A)⁻¹ = det(A⁻¹)`
- **Вырожденная матрица** это та, у которой определитель равен `0`

### СЛАУ

**Системой линейных алгебраических уравнений** (СЛАУ) называется совокупность уравнений первой степени, где все переменные и коэфиценты являются вещественными числами.

![](./images/slau.png)

СЛАУ бывают *однородными* (`∀bᵢ = 0`) и *неоднородными* (`∃bᵢ ≠ 0`).

Система называется *определенной* если она имеет только одно решение, и *неопределенной*, если больше одного.

Решения их бывают *тривиальными* (`aᵢⱼ = 0 ∀ i, j`) и *нетрвивиальными*.

Однородные СЛАУ могут иметь или одно тривиальное решение, или бесконечное множество решений.

#### Запись в виде матрицы

Любую СЛАУ можно записать в виде произведения матрицы и вектора. Такая запись называется **матричным уравнением**.

![](./images/slau_as_matrix.png)

#### Ранг и базис

**Ранг матрицы** — это кол-во *независимых векторов* в системе. Это число не может быть больше кол-ва столбцов высокой матрицы (или строк длинной). Обозначается `rk` или `rank`.

**Ранг системы векторов** — это ее разметрность.

Если ранг является *максимальным* (или *полным*), то значит все вектора в системе являются независимыми. Иначе вектора являются зависимыми — `∃wᵢ ≠ 0` приводящие всю систему к нулевому вектору.

```python
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

np.linalg.matrix_rank(A) # 2
```

**Базис** — это минимальный набор независимых векторов. В задаче регрессии это набор признаков, через который можно выразить все остальные признаки.

#### Решение неоднородных СЛАУ

**Расширенная матрица** — такая где свободные члены `bᵢ` записаны в дополнительном столбце и отделяются от столбцов с коэфициентами `aᵢⱼ` вертикальной чертой.

Существуют три случая при решении неоднородных СЛАУ

- только одно решение — `1`
- бесконечное кол-во решений — `∞`
- решение отсутствует — `0`

##### Только одно решение

*Теорема Кронекера — Капелли* говорит, что единственное решение возможно тогда и только тогда, когда ранг матрицы системы `A` равен рангу расширенной матрицы системы `A|b` и равен кол-ву неизвестных коэфициентов `m`:

`rk(A) = rk(A|b) = m <=> ∃!w = (w₁, w₂, ..., wₘ)ᵀ`

Причем решение будет равно:

`w = A⁻¹b`

##### Бесконечное кол-во решений

Согласно первому следствию из вышеупомянутой теоремы:

`rk(A) = rk(A|b) < m <=> ∞ решений`

##### Решение отсутствует

Согласно второму следствию из той же теоремы:

`rk(A) < rk(A|b) <=> ∄ решений`

##### Приближенное решение

Для последнего случая можно найти приближенное решение, то есть такой вектор коэфициентов `w’`, который позволит вычислить такой вектор решений `b’`, который будет *минимально* оличаться от вектора `b` (ниже `e` — это векторо ошибки, мы хотим минимизировать его длину).

`A・w’ = b’, e = b’ - b, |e| -> min`

Как его найти? Это можно сделать математически.

![](./images/MATHML_md2_2_49.png)

Голубой вектор `b’` который мы хотим получить должен быть *проекцией* коричневого вектора `b` на плоскость векторов матрицы `A`. А это значит, что скалярное произведение голубого вектора на `A` будет равно скалярному произведению коричневого вектора на `A`:

`Aᵀ・b’ = Aᵀ・b`, где

`b’ = A・w’`, поэтому

`Aᵀ・A・w’ = Aᵀ・b`

Здесь `Aᵀ・A` есть матрица Грама `G`.

`G・w’ = Aᵀ・b`

Далее мы предполагаем, что для `G` существует `G⁻¹`.

`G⁻¹・G・w’ = G⁻¹・Aᵀ・b`

`w’ = G⁻¹・Aᵀ・b`

`w’ = (Aᵀ・A)⁻¹・Aᵀ・b`

##### Рассчет коэфициентов

На практике метод применяется следующим образом (средствами Numpy).

```python
X = data.drop(columns=['Prod']).values # X.shape = (200, 7)
A = np.column_stack((np.ones(200), X)) # A.shape = (200, 8)
y = data[['Prod']].values # y.shape = (200, 1)

w = np.linalg.inv(A.T@A) @ A.T @ y # w.shape (8, 1) 
```

##### Ограничения OLS метода

Если исходные данные **плохо обусловлены**, то матрица Грама будет вырожденной, и наша формула не сработает.

Одним из методов борьбы с этой проблемой является *устранение мультиколлинеарности*, а также *нормализация/стандартизация* данных.

Другой способ — метод под названием **сингулярное разложение** (SVD), о котором мы будем говорить позже. Он позволяет бороться с ошибками при обращении матриц. Данный метод встроен в класс `LinearRegression`, так что он сможет обработать даже плохо обусловленные данные, но при этом получение правильных коэфициентов *не гарантиравно*.

#### Матрица корреляции

##### Стандартизация векторов

В модуле `sklearn` есть несколько классов для стандартизации и нормализации. Стандартизация в линейной алгебре отличается от них всех. Она состоит из двух шагов:

1. центрирование вектора (помещение его цента в нулевую координату)
2. нормирование вектора (приведение его размера к единице)

Если после такой обработки построить матрицу Грама, то мы получим матрицу корреляции признаков❗️

В Python такую матрицу можно получить двумя способами. Один из них мы знаем, это `pd.corr`. А другой — `np.linalg.corrcoef`:

```python
v1 = np.array([1,2,3,2,1])
v2 = np.array([1,3,2,3,6])
v3 = np.array([4,2,0,2,4])

np.corrcoef(np.array([v1, v2, v3]))
np.corrcoef(v1, v2)
# [[ 1.        , -0.31943828, -1.        ],
#  [-0.31943828,  1.        ,  0.31943828],
#  [-1.        ,  0.31943828,  1.        ]]
```

##### Корреляция векторов

Корреляцию между двумя векторами можно посчитать по формуле:

`a・b / |a||b|`

По сути это косинус угла между векторами, поэтому

|корреляция|угол|интерпретация|
|-|-|-|
|`1`|`0°`|вектора сонаправлены; факторы имеют прямую зависимость|
|`0.71`|`45°`|факторы имеют сильную зависимость|
|`0.12`|`83°`|угол почти прямой, факторы имеют очень слабую зависимость|
|`0`|`90°`|вектора ортогональны, независимы; факторы никак не влияют друг на друга|
|`-1`|`190°`|вектора противонаправлены; факторы имеют обратную зависимость|

##### Корреляция факторов

Мы должны бороться с корреляцией между факторами потому что:

- мы не можем доверять найденным коэфициентам
- мы не сможем их проинтерпретировать

Если корреляция между факторами прямая, то ее легко заметить на матрице корреляций, и легко устранить.

Если же корреляция скрытая (ранг матрицы максимальный, не определитель близок к нулю) то значит имеется мультиколлинеарность, и мы скоро узнаем, как с ней можно бороться.

### Модификации линейной регрессии

#### Полиноминальная регрессия

##### Мононом

Одночлен (мононом) — это произведение из числовых множетелей и переменных в неотрицательной целой степени, например: `xy`, `⅔ab³c`, `4x²y`, `-4mn³`, `𝜋r²`. Степенью одночлена называется сумма степеней его переменных, например:

- `xy` имеет степень `2 = 1 + 1` 
- `⅔ab³c` имеет степень `5 = 1 + 3 + 1`

##### Полином

Многочлен (он же полином) — это сумма одночленов. Полином для `k` переменных это функция вида:

![](./images/polynom.png)

где

- `i` — *степени полинома* — целые неотрицательные числа
- `w` — *коэфициенты полинома*

**Степенью полинома** называют максимальную степень его членов. Мы будем обозначать ее литерой `d`.

Если переменная всего одна, то функция принимает такой вид:

![](./images/polynom-one-x.png)

##### Коэфициенты полинома

Кол-во коэфициентов зависит от степени полинома `d` и кол-ва переменных `k`. Его можно вычислить по вот такой формуле:

`C = (k + d)! / k!d!`

Получается что для самого простого случая кол-во коэфициентов будет равно `C(1, 1) = 2`.

`y = w₀x⁰ + w₁x¹ = ax + b` — формула прямой на плоскости

Если их три, то это либо `C(2, 1)` — парабола:

`y = w₀x⁰ + w₁x¹ + w₂x² = ax² + bx + c`

либо `C(1, 2)` — плоскость в 3D пространстве:

`z = w₀ + w₁x¹ + w₂y¹ = ax + by + c`

Для случая `C(2, 2) = 6` полином принимает такую форму:

`P = w₀ + w₁x¹ + w₂x² + w₃y¹ + w₄y² + w₅xy`

##### Применение

С помощью полинома `k` степени можно описать кривую любой сложности.

![](./images/polynom-usage.png)

На практике для этого нужно лишь выбрать степень `k` и создать из имеющихся векторов `x` дополнительные вектора с их комбинацией в соответствующей степени.

То есть по сути мы лишь добавим данных в нашу матрицу, и затем сможем найти коэфициенты с помощью OLS.

##### Решение на Python

Мы можем воспользоваться следующей функцией для добавления комбинаций векторов `x` нужной степени `d` и вычисления коэфициентов методом OLS:

```python
# from sklearn import preprocessing

def calc_poly(X, y, d):
    poly = preprocessing.PolynomialFeatures(degree=d, include_bias=True)

    X_poly = poly.fit_transform(X)

    w = np.linalg.inv(X_poly.T@X_poly) @ X_poly.T @ y

    return X_poly, w
```

##### Side effects

Предложенное выше решение может добавить такие вектора `x` которые будут выражаться через уже существующие (зависимые). В результате ранг матрицы не будет максимальным, при вычислении коэфициентов будет происходить деление на число близкое к нулю, и они могут получиться огромными.

Данную проблему можно обойти, воспользовавшись классом `LinearRegression`, который внути использует не исходную матрицу, а ее сингулярное разложение, которое не является вырожденным.

Но самой большой проблемой является склонность таких моделей к переобучению.

![](./images/poly-overrtained.png)

Чтобы ее решить используется *регуляризация*.

#### Регуляризация

**Регуляризация** — это способ борьбы с переобучением модели путем намеренного увеличения ее смещения с целью уменьшения ее разброса.

##### С точки зрения математики

Наша цель — избежать слишком больших коэфициентов. Для этого нам нужно решить нашу задачу OLS с условием:

![](./images/ols-with-cond.png)

Условие говорит, что норма вектора `w` порядка `p` в степени `p` не должна превышать величину `b`.

Задачи с условиями мы пока не можем решать, но благодаря методу множителей Лагранжа мы можем свести ее к безусловному виду.

![](./images/lagrange.png)

##### L₂-регуляризация

Норма вектора порядка `p` определяется по формуле:

![](./images/w-norm.png)

И для второго порядка это будет просто длина вектора. То есть наша формула примет такой вид:

`|y - Aw|² + α|w|² -> min`

И для нее даже есть аналитическое решение:

`w = (Aᵀ・A + α・E)⁻¹・Aᵀ・y`

Чтобы не считать вручную можно воспользоваться классом [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)

```python
# from sklearn import linear_model

ridge = linear_model.Ridge(alpha=1, fit_intercept=False)
ridge.fit(M, y)

print(ridge.coef_)
```

##### L₁-регуляризация

Как следует из названия, в данном методе применяется регуляризация Лагранжа первого порядка. 

`|y - Aw|² + α∑|wᵢ| -> min`

В таком виде задача не решается аналитически. Для ее решения используется *метод координатного спуска* (Coordinate Descent). Метод реализован в классе [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html).

Поскольку метод является чиленным, то для лучшей сходимости нужно стандартизировать данные с помощью `StandardScaler`.

```python
# from sklearn import preprocessing as ce
# from sklearn import linear_model

scaler = ce.StandardScaler()
X = scaler.fit_transform(X)

lasso = linear_model.Lasso(alpha=0.1, fit_intercept=False)
lasso.fit(X, y)

print(lasso.coef_)
```

##### Elastic-Net

Это комбинация методов `L₁` и `L₂`. Она реализована в классе [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html).

![](./images/elastic-net.png)

У него кроме `α` есть дополнительный параметр `ƛ`, который меняется от `0` до `1` и определяет в какой пропорции влияет на результат каждый из методов `L₁` и `L₂`.

Использовать данный метод с `α = 0` не имеет смысла (нужно выбрть Ridge, который даст более точный результат благодаря аналитическому решению).

```python
# from sklearn import linear_model

elasticnet = linear_model.ElasticNet(alpha=0.1, l1_ratio=0.2, fit_intercept=False)
elasticnet.fit(A, y)

print(elasticnet.coef_)
```











Но нужно отметить, что для успешного решения данной задачи необходимо чтобы матрица `A` была стандартизирована, причем не в математическом смысле, а с помощью `StandardScaler`