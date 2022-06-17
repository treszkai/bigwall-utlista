## BigWall utlista parser

### Usage

Once you're [logged in to Docker Hub](https://docs.docker.com/docker-id/#log-in), you can pull the Docker image and run it by:

```
$ docker run --rm treszkai/bigwall-utlista > utlista.csv
```

You can also build this image yourself by cloning this Git repository first:

```bash
$ git clone "https://github.com/treszkai/bigwall-utlista.git" && cd bigwall-utlista
$ docker build -t treszkai/bigwall-utlista .
$ docker run --rm treszkai/bigwall-utlista > utlista.csv
```

### Output

The route list is printed on stdout as a CSV with columns `id`, `title`, `french-grade`. Routes are ordered by ID.

Convert the French grade to UIAA yourself using [this chart](https://en.wikipedia.org/wiki/Grade_%28climbing%29#Bouldering_2).

### Restrictions

Please play nice and don't run this script a thousand times a second.

### Warranty

There is no warranty.

