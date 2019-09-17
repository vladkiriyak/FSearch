# FSearch - система полнотекстового поиска

Для реализации  системы используется поисковый индекс

--------------------------------------------------------------------------------------------------------


Поиско́вый и́ндекс — структура данных, которая содержит информацию о документах и используется в поисковых системах. Индекси́рование, совершаемое поисковой машиной, — процесс сбора, сортировки и хранения данных с целью обеспечить быстрый и точный поиск информации. Создание индекса включает междисциплинарные понятия из лингвистики, когнитивной психологии, математики, информатики и физики. Веб-индексированием называют процесс индексирования в контексте поисковых машин, разработанных, чтобы искать веб-страницы в Интернете.

Популярные поисковые машины сосредотачиваются на полнотекстовой индексации документов, написанных на естественных языках. Мультимедийные документы, такие как видео и аудио и графика, также могут участвовать в поиске.

Метапоисковые машины используют индексы других поисковых сервисов и не хранят локальный индекс, в то время как поисковые машины, основанные на кешированных страницах, долго хранят как индекс, так и текстовые корпусы. В отличие от полнотекстовых индексов, частично-текстовые сервисы ограничивают глубину индексации, чтобы уменьшить размер индекса. Большие сервисы, как правило, выполняют индексацию в заданном временно́м интервале из-за необходимого времени и затрат на обработку, в то время как поисковые машины, основанные на агентах, строят индекс в масштабе реального времени.

Индексация!!!!!
---------------------
Цель использования индекса — повышение скорости поиска релевантных документов по поисковому запросу. Без индекса поисковая машина должна была бы сканировать каждый документ в корпусе, что потребовало бы большого количества времени и вычислительной мощности. Например, в то время, как индекс 10 000 документов может быть опрошен в пределах миллисекунд, последовательный просмотр каждого слова в 10 000 больших документов мог бы занять часы. Дополнительная память, выделяемая для хранения индекса, и увеличение времени, требуемое для обновления индекса, компенсируется уменьшением времени на поиск информации.

Факторы, влияющие на проектирование поисковых систем
---

#### Факторы слияния
Как данные входят в индекс? Как слова и подчиненные функции добавляются в индекс во время текстового корпусного обхода? И могут ли несколько поисковых роботов работать асинхронно? Поисковый робот должен сначала проверить, обновляет он старое содержание или добавляет новое. Слияние индекса поисковой системы подобно SQL Merge и другим алгоритмам слияния.

---
#### Методы хранения
Как хранить индексируемые данные? То есть определяют вид хранимой информации: сжатый или отфильтрованный.

---
#### Размер индекса
Сколько памяти компьютера необходимо, чтобы поддерживать индекс.

---
#### Скорость поиска
Как быстро можно найти слово в инвертированном индексе. Важным для информатики является сравнение скорости нахождения записи в структуре данных и скорости обновления/удаления индекса.

---
#### Хранение
Как хранится индекс в течение длительного времени.

---

#### Отказоустойчивость
Для поисковой службы важно быть надежной. Вопросы отказоустойчивости включают проблему повреждения индекса, определяя, можно ли отдельно рассматривать некорректные данные, связанные с плохими аппаратными средствами, секционированием и схемами на основе хеш-функций и композитного секционирования, а также репликации.

Индексные структуры данных
---
Архитектура поисковой системы различается по способам индексирования и по методам хранения индексов, удовлетворяя факторы. Индексы бывают следующих типов:

---
#### Суффиксное дерево

Образно структурировано как дерево, поддерживает линейное время поиска. Построено на хранении суффиксов слов. Деревья поддерживают расширенное хеширование, которое важно для индексации поисковой системы. Используется для поиска по шаблону в последовательностях ДНК и кластеризации. Основным недостатком является то, что хранение слова в дереве может потребовать пространство за пределами необходимого для хранения самого слова. Альтернативное представление — суффиксный массив. Считается, что он требуют меньше виртуальной памяти и поддерживает блочно-сортирующее сжатие данных.

---
#### Инвертированный индекс
Хранилище списка вхождений каждого критерия поиска, обычно в форме хеш-таблиц или бинарного дерева.

Прямой индекс
---
Прямой индекс хранит список слов для каждого документа. Ниже приведена упрощенная форма прямого индекса:

|Слова |  Документ |
| ------------ | ------------ |
|мама, папа   | Документ 1   |
| дом, школа | Документ 2   |

Необходимость разработки прямого индекса объясняется тем, что лучше сразу сохранять слова за документами, поскольку их в дальнейшем анализируют для создания поискового индекса. Формирование прямого индекса включает асинхронную системную обработку, которая частично обходит узкое место обновления инвертированного индекса. Прямой индекс сортируют, чтобы преобразовать в инвертированный. Прямой индекс по сути представляет собой список пар, состоящих из документов и слов, отсортированный по документам. Преобразование прямого индекса к инвертированному является только вопросом сортировки пар по словам. В этом отношении инвертированный индекс — отсортированный по словам прямой индекс.

Инвертированный индекс
---
Многие поисковые системы используют инвертированный индекс при оценке поискового запроса, чтобы быстро определить местоположение документов, содержащих слова из запроса, а затем ранжировать эти документы по релевантности. Поскольку инвертированный индекс хранит список документов, содержащих каждое слово, поисковая система может использовать прямой доступ, чтобы найти документы, связанные с каждым словом в запросе, и быстро получить их. Ниже приведено упрощенное представление инвертированного индекса:

|Слово | Документы |
|-----|-----|
|мама | Документ 1, Документ 2, Документ 3 |
|папа | Документ 3, Документ 1, Документ 3 |

Инвертированный индекс может только определить, существует ли слово в пределах конкретного документа, так как не хранит никакой информации относительно частоты и позиции слова, и поэтому его считают логическим индексом. Инвертированный индекс определяет, какие документы соответствуют запросу, но не оценивает соответствующие документы. В некоторых случаях индекс включает дополнительную информацию, такую как частота каждого слова в каждом документе или позиция слова в документе[16]. Информация о позиции слова позволяет поисковому алгоритму идентифицировать близость слова, чтобы поддерживать поиск фраз. Частота может использоваться, чтобы помочь в ранжировании документов по запросу. Такие темы в центре внимания исследований информационного поиска.

Инвертированный индекс представлен разреженной матрицей, так как не все слова присутствуют в каждом документе. Индекс подобен матрице термов документа, используемом в ЛСА. Инвертированный индекс можно считать формой хеш-таблицы. В некоторых случаях индекс представлен в форме двоичного дерева, которая требует дополнительной памяти, но может уменьшить время поиска. В больших индексах архитектура, как правило, представлена распределенной хеш-таблицей.

Слияние индекса
---
Инвертированный индекс заполняется путём слияния или восстановления. Архитектура может быть спроектирована так, чтобы поддерживать инкрементную индексацию, где слияние определяет документ или документы, которые будут добавлены или обновлены, а затем анализирует каждый документ в слова. Для технической точности, слияние объединяет недавно индексированные документы, обычно находящиеся в виртуальной памяти, с индексным кэшем, который находится на одном или нескольких жестких дисках компьютера.

После синтаксического анализа индексатор добавляет указанный документ в список документов для соответствующих слов. В более крупной поисковой системе процесс нахождения каждого слова для инвертированного индекса может быть слишком трудоемким, поэтому его, как правило, разделяют на две части:

разработка прямого индекса,
сортировка прямого индекса в инвертированный индекс.
Инвертированный индекс называется так из-за того, что он является инверсией прямого индекса.


Сжатие
---
Создание и поддержка крупномасштабного поискового индекса требует значительной памяти и выполнения задач обработки. Многие поисковые системы используют ту или иную форму сжатия, чтобы уменьшить размер индексов на диске. Рассмотрим следующий сценарий для полнотекстового механизма поиска в Интернете:

Требуется 8 битов (1 байт) для хранения одного символа. Некоторые кодировки используют 2 байта на символ.
Среднее число символов в любом слове на странице примем за 5.
Учитывая этот сценарий, несжатый индекс для 2 миллиардов веб-страниц должен был бы хранить 500 миллиардов записей слов. 1 байт за символ или 5 байт за слово — потребовалось бы 2500 гигабайт одного только пространства памяти. Это больше, чем среднее свободное пространство на диске 2 персональных компьютеров. Для отказоустойчивой распределенной архитектуры требуется еще больше памяти. В зависимости от выбранного метода сжатия индекс может быть уменьшен до части такого размера. Компромисс времени и вычислительной мощности, требуемой для выполнения сжатия и распаковки.

Примечательно, что крупномасштабные проекты поисковых систем включают затраты на хранение, а также на электроэнергию для осуществления хранения









Пример таблиц индексирования
---

- Table documents

|  id  |name   |
|--------|---------|
|1|Doc1.doc|
|2|hh12.doc|
|3|test.doc|

- Table inverted index

|word|docID|wordQuantity|
|------------------|---|--------------------|
|cat|1|3|
|cat|2|44|
|dog|2|23|

Table word position

|word|docID|wordPosition(line, number)|
|-------|------------|----------------------|
|cat|1|'3, 3'|
|cat|1|'5, 23'|
|cat|1|'13, 354'|
|cat|2|'21, 73'|
|cat|2|'23, 7'|
|dog|2|'67,1'|









Источники
---

- James Lee. [Software Learns to Tag Photos](http://www.technologyreview.com/news/406833/software-learns-to-tag-photos/) 

- Stephen V. Rice, Stephen M. Bailey. [Searching for Sounds Comparisonics Searching for Sounds](http://www.comparisonics.com/SearchingForSounds.html)
- С. Брин, Л. Пейдж [The Anatomy of a Large-Scale Hypertextual Web Search Engine](http://infolab.stanford.edu/~backrub/google.html)

- Vreda Pieterse and Paul E. Black. "trie" in [Dictionary of Algorithms and Data Structures](http://www.nist.gov/dads/HTML/invertedIndex.html)

- Christofer D. Manning [Introduction to information retrieval](http://nlp.stanford.edu/IR-book/html/htmledition/irbook.html)


