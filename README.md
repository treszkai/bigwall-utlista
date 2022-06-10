## BigWall utlista parser

### Használat

Docker containerben a legegyszerubb:

```bash
$ # build docker container
$ docker build -t bigwall-utlista .

$ # run container
$ docker run --rm bigwall-utlista > utlista.csv
```

Aztan `utlista.csv` egy CSV file `id`, `french-grade`, `title` oszlopokkal.

## Restrictions

Please play nice and don't run this script a thousand times a second.
