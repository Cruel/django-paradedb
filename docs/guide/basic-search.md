# Basic Search

## Single Term Search

```python
from paradedb.search import ParadeDB

Product.objects.filter(description=ParadeDB('shoes'))
```

**Generated SQL:**
```sql
SELECT * FROM products WHERE description &&& 'shoes';
```

## AND Search (Conjunction)

Pass multiple terms to require all of them:

```python
Product.objects.filter(description=ParadeDB('running', 'shoes'))
```

**Generated SQL:**
```sql
SELECT * FROM products WHERE description &&& ARRAY['running', 'shoes'];
```

## OR Search (Disjunction)

Use `PQ` objects for OR logic:

```python
from paradedb.search import ParadeDB, PQ

Product.objects.filter(
    description=ParadeDB(PQ('wireless') | PQ('bluetooth'))
)
```

**Generated SQL:**
```sql
SELECT * FROM products WHERE description ||| ARRAY['wireless', 'bluetooth'];
```

## Combining with Django Filters

Mix ParadeDB search with standard Django ORM:

```python
Product.objects.filter(
    description=ParadeDB('shoes')
).filter(
    price__lt=100,
    in_stock=True,
)
```

**Generated SQL:**
```sql
SELECT * FROM products
WHERE description &&& 'shoes'
AND price < 100
AND in_stock = true;
```
