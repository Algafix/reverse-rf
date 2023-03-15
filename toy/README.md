

Burst A
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ----- - - - --`

`init 1 2 5 1 1 1 2`

Burst B
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ------ - - - -`

`init 1 2 6 1 1 1 1`


Stop A
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- -- ----- - - -`

`init 1 2 2 5 1 1 1`


Stop B
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- -- --- -- - --`

`init 1 2 2 3 2 1 2`


Stop C
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- - -- --- -`

`init 1 2 3 1 2 3 1`


Stop D
===

Repetition: 

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- - - - ----`

`init 1 2 3 1 1 1 4`


Change 1
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- -- - -- -`

`init 1 2 4 2 1 2 1`


Change 2
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- - - - ---`

`init 1 2 4 1 1 1 3`


Change 3
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- --- -- - -`

`init 1 2 3 3 2 1 1`


Change 4
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- -- - -- -`

`init 1 2 4 2 1 2 1`


Change 5
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- - - - ---`

`init 1 2 4 1 1 1 3`


Change 6
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- --- -- - -`

`init 1 2 3 3 2 1 1`


Change 7
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- -- - -- -`

`init 1 2 4 2 1 2 1`


Change 8
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- - - - ---`

`init 1 2 4 1 1 1 3`


Change 9
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- --- -- - -`

`init 1 2 3 3 2 1 1`


Change 10
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- -- - -- -`

`init 1 2 4 2 1 2 1`


Change 1-b
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- ---- - - - ---`

`init 1 2 4 1 1 1 3`


Change 2-b
===

Repetition: 13 times

Modulation: OOK

Encoding: ?  -> init + 7 blocks

`— - -- --- --- -- - -`

`init 1 2 3 3 2 1 1`



Code Analysis
===

Table View
---

|Mode| Round 1            | Round 2            |
|:--:|:------------------:|:------------------:|
| 1  | init 1 2 4 2 1 2 1 | init 1 2 4 1 1 1 3 |
| 2  | init 1 2 4 1 1 1 3 | init 1 2 3 3 2 1 1 |
| 3  | init 1 2 3 3 2 1 1 |          etc
| 4  | init 1 2 4 2 1 2 1 |
| 5  | init 1 2 4 1 1 1 3 |
| 6  | init 1 2 3 3 2 1 1 |
| 7  | init 1 2 4 2 1 2 1 |
| 8  | init 1 2 4 1 1 1 3 |
| 9  | init 1 2 3 3 2 1 1 |
| 10 | init 1 2 4 2 1 2 1 |
|    |          
| BA | init 1 2 5 1 1 1 2 |
| BB | init 1 2 6 1 1 1 1 |
|    |
| SA | init 1 2 2 5 1 1 1 |
| SB | init 1 2 2 3 2 1 2 |
| SC | init 1 2 3 1 2 3 1 |
| SD | init 1 2 3 1 1 1 4 |


Analysis
---

|  Common  |  Unique   |
|:--------:|:---------:|
| init 1 2 | 4 2 1 2 1 |
| init 1 2 | 4 1 1 1 3 |
| init 1 2 | 3 3 2 1 1 |
| init 1 2 | 5 1 1 1 2 |
| init 1 2 | 6 1 1 1 1 |
| init 1 2 | 2 5 1 1 1 |
| init 1 2 | 2 3 2 1 2 |
| init 1 2 | 3 1 2 3 1 |
| init 1 2 | 3 1 1 1 4 |

### Change

The change seems a bucle of 3 codes:

`init 1 2 4 2 1 2 1` --> `init 1 2 4 1 1 1 3` --> `init 1 2 3 3 2 1 1`

Stoping the device and starting again accepts any code.
* Transformation function to get the next code?
* Internal table?

### General

All codes start the same: `init 1 2`

There are 9 codes of 5 changing values

The values change, but always sum 10 (13 counting the common part):

```
4 2 1 2 1 = 10
4 1 1 1 3 = 10
3 3 2 1 1 = 10
5 1 1 1 2 = 10
6 1 1 1 1 = 10
2 5 1 1 1 = 10
2 3 2 1 2 = 10
3 1 2 3 1 = 10
3 1 1 1 4 = 10
```

Having 5 positions and counting 10, there are 6 possible unordered codes:

| Unordered code | Count |
|:--------------:|:-----:|
| 6 1 1 1 1      |   1   |
| 5 2 1 1 1      |   2   |
| 4 3 1 1 1      |   2   |
| 4 2 2 1 1      |   1   |
| 3 3 2 1 1      |   2   |
| 3 2 2 2 1      |   1   |
| 2 2 2 2 2      |   0   |

Never the `2 2 2 2 2` code. 👀 __Should I...?__


