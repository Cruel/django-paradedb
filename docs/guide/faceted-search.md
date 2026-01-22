# Faceted Search

## Getting Facet Counts

Use `.facets()` to get term counts for filtering UI:

```python
facets = Product.objects.filter(
    description=ParadeDB('shoes')
).facets('category', 'brand')

print(facets)
# {
#     "category": {
#         "buckets": [
#             {"key": "Running", "doc_count": 50},
#             {"key": "Casual", "doc_count": 35},
#         ]
#     },
#     "brand": {
#         "buckets": [
#             {"key": "Nike", "doc_count": 45},
#             {"key": "Adidas", "doc_count": 30},
#         ]
#     }
# }
```
