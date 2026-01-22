# Scoring & Snippets

## Relevance Scoring

Get BM25 relevance scores:

```python
from paradedb.search import ParadeDB
from paradedb.functions import Score

Product.objects.filter(
    description=ParadeDB('wireless', 'bluetooth')
).annotate(
    score=Score()
).order_by('-score')
```

## Highlighted Snippets

Get search term highlights:

```python
from paradedb.functions import Snippet

Product.objects.filter(
    description=ParadeDB('wireless', 'bluetooth')
).annotate(
    snippet=Snippet('description')
).values('description', 'snippet')
```

## Custom Snippet Formatting

```python
Product.objects.filter(
    description=ParadeDB('running', 'shoes')
).annotate(
    snippet=Snippet(
        'description',
        start_tag='<mark>',
        end_tag='</mark>',
        max_chars=100
    )
)
```
