# Prática 1.4: Playlist Musical

    Desenvolva o diagrama de classes e implemente o sistema proposto a seguir. Divida o seu programa em módulos.

## Classe `Musica`

*Atributos:*

- `artista`, tipo `str`, privado
- `titulo`, tipo `str`, privado

*Métodos:*

- `__init__`: recebe como parâmetro o artista e o título da música
- `__str__`: imprime a música no formato `Artista - Musica`

## Classe `Playlist`

*Atributos:*

- `musicas`: agregação de objetos da classe `Musica` mantida em uma `list`

*Métodos:*

- `__init__`: recebe como parâmetro uma `list` de objetos da classe `Music`
- `imprime`: imprime todas as músicas da playlist
- `adiciona`: adiciona uma música como última a ser tocada na playlist
- `toca_proxima`: toca a próxima música da playlist e a remove da playlist
- `embaralha`: embaralha a playlist utilizando a função `shuffle` do módulo `random` da biblioteca padrão

## Saída esperada do programa:

```
----------------
Nirvana - Smells Like Teen Spirit
Green Day - Basket Case
The Offspring - Original Prankster
----------------
----------------
Nirvana - Smells Like Teen Spirit
Green Day - Basket Case
The Offspring - Original Prankster
Foo Fighters - Everlong
----------------
Tocando agora: Nirvana - Smells Like Teen Spirit
Tocando agora: Green Day - Basket Case
----------------
The Offspring - Original Prankster
Foo Fighters - Everlong
----------------

# !!! Por causa do random, a sua saída pode ser diferente desta
----------------
Avril Lavigne - Skater Boy 
Papa Roach - Last Resort
Foo Fighters - Everlong
The Offspring - Original Prankster
----------------
```