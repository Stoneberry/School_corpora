# School_corpora


# Wikidata
### Русские писатели, умершие раньше 1949 года
```
SELECT ?item ?itemLabel ?death WHERE {
  ?item wdt:P31 wd:Q5.
  ?item wdt:P172 wd:Q49542.
  ?item wdt:P106 wd:Q36180;
    wdt:P570 ?death.
  FILTER((YEAR(?death)) <= 1949 )
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru". }
}
```

### Люди, писавшие или говорившие на русском, умершие раньше 1949 года
```
SELECT ?item ?itemLabel ?death WHERE {
  ?item wdt:P31 wd:Q5.
  ?item wdt:P172 wd:Q49542;
    wdt:P570 ?death.
  FILTER((YEAR(?death)) <= 1949 )
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ru". }
}
```
