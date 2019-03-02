# filter-out-lowest-value-duplicates
Remove lowest value duplicates by key

Benchmarks and tests of scripts from answers to a StackOverflow question: [Fastest way to uniquify a list of dicts with a rule?](https://stackoverflow.com/questions/54956979/fastest-way-to-uniquify-a-list-of-dicts-with-a-rule)

### Short List n=4

```
0.000003322 @sarcoma [{'T': 2345, 'V': 50, 'O': 5}, {'T': 1234, 'V': 10, 'O': 1}, {'T': 3456, 'V': 40, 'O': 91}]
0.000010512 @DeepSpace [{'T': 1234, 'V': 10, 'O': 1}, {'T': 2345, 'V': 50, 'O': 5}, {'T': 3456, 'V': 40, 'O': 91}]
0.000005575 @RoadRunner [{'T': 1234, 'V': 10, 'O': 1}, {'T': 2345, 'V': 50, 'O': 5}, {'T': 3456, 'V': 40, 'O': 91}]
0.000004542 @Patrick_Artner [{'T': 1234, 'V': 10, 'O': 1}, {'T': 2345, 'V': 50, 'O': 5}, {'T': 3456, 'V': 40, 'O': 91}]
```

### Long List n=100000

```
0.112315879 @sarcoma
0.176299670 @DeepSpace
0.141609290 @RoadRunner
0.150336850 @Patrick_Artner
```
