def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 3, 3, 10, 7, 8, 7]
print(list(dedupe(a)))
