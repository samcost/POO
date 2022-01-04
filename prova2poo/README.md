# Prova 2

Um sistema envolvendo diferentes tipos de polígonos possui hierarquia como descrita a seguir.

Desta forma:

- Implemente o sistema
    - Alguns métodos estão implementados
    - No código não se encontra que classe deve herdar de outra e nem que classe deve ser abstrata:
      insira esta informação
        - Existe uma classe `Poligono` que não deve ser instanciada
        - Um `PoligonoRegular` é um `Poligono`
        - Um `Retangulo` é um `Poligono`
        - Um `TrianguloEquilatero` e um `Quadrado` são `PoligonoRegular`
- Entregue o diagrama de classes
    - Não precisa detalhar os atributos/métodos das classes
    - Basta informar as relações entre classes e classes abstratas

*Saída esperada:*

```
Retângulo com base 5.0 e altura 10.0  em (-1.0,1.0)
    >Perimetro: 30.0
    >Area: 50.0
Triangulo equilatero com lado igual a 2  em (5.0,5.0)
    >Perimetro: 6
    >Area: 1.7320508075688779
Triangulo equilatero com lado igual a 3  em (0.0,-2.0)
    >Perimetro: 9
    >Area: 3.8971143170299753
Quadrado com lado igual a 4  em (10.0,10.0)
    >Perimetro: 16
    >Area: 16.000000000000004
Poligono regular de 5 lados, lado igual a 7  em (-10.0,-10.0)
    >Perimetro: 35
    >Area: 84.30339262885938
Distancia entre o quadrado e o pentagono: 28.284271247461902
Lados informados nao formam um poligono regular

```