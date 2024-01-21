
# Conducció Autònoma mitjançant la Visió per Computador i la Intel·ligència Artificial

Aquest repositori conté el codi desenvolupat per un Treball de Recerca juntament amb altres recursos.

Les tres funcionalitats, essencials per a un sistema de conducció autònoma, que s'han desenvolupat són:
 - Detecció i seguiment de carrils
 - Detecció d'obstacles
 - Pathfinding o navegació

## Detecció i seguiment de carrils
Aquest mòdul o sistema té la funció de detectar els carrils a partir de les imatges, després calcular-ne la posició i orentació relativa amb el vehicle i, finalment, estimar el gir que s'ha de realitzar per a mantenir el vehicle centrat.

#### Preprocessat
Partim de les imatges base:
| Imatge 1| Imatge 2|
| --- | --- |
| ![base image](https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1.jpg) | ![base image](https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2.jpg) |
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1.jpg" width="45%"/>  <img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2.jpg" width="45%"/> 

En primer lloc s'han de preprocessar les imatges, reduïnt així soroll i informació innecessària que pot interferir.


