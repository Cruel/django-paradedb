# Advanced Search

## Phrase Search

Search for exact phrases:

```python
from paradedb.search import ParadeDB, Phrase

Product.objects.filter(description=ParadeDB(Phrase('wireless bluetooth')))
```

## Fuzzy Search

Allow typos and misspellings:

```python
from paradedb.search import ParadeDB, Fuzzy

Product.objects.filter(description=ParadeDB(Fuzzy('shoez', distance=1)))
```

## Regex Search

Pattern matching:

```python
from paradedb.search import ParadeDB, Regex

Product.objects.filter(description=ParadeDB(Regex(r'shoe[s]?')))
```

## Complex Boolean Logic

Combine conditions with PQ:

```python
from paradedb.search import ParadeDB, PQ, Phrase

# (shoes OR sandals) AND leather
Product.objects.filter(
    description=ParadeDB(
        (PQ('shoes') | PQ('sandals')) & PQ('leather')
    )
)
```
