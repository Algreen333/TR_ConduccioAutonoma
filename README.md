
# Conducció Autònoma mitjançant la Visió per Computador i la Intel·ligència Artificial

Aquest repositori conté el codi desenvolupat per un Treball de Recerca juntament amb altres recursos.

Les tres funcionalitats, essencials per a un sistema de conducció autònoma, que s'han desenvolupat són:
 - Detecció i seguiment de carrils
 - Detecció d'obstacles
 - Pathfinding o navegació

## Detecció i seguiment de carrils
Aquest mòdul o sistema té la funció de detectar els carrils a partir de les imatges, després calcular-ne la posició i orentació relativa amb el vehicle i, finalment, estimar el gir que s'ha de realitzar per a mantenir el vehicle centrat.

#### Preprocessat
Partim de les imatges base, extretes en aquest cas del BeamNG:
<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1.jpg" width="48%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2.jpg" width="48%"/> 
</p>


En primer lloc s'han de preprocessar les imatges, reduïnt així soroll i informació innecessària que pot interferir. Per a fer-ho es passa la imatge a escala de grisos (per eliminar el color) i se li aplica un filtre Gabor que redueix el soroll.

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1_GRAYSCALE.jpg" width="48%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2_GRAYSCALE.jpg" width="48%"/> 
</p>


Per a detectar els carrils en aquestes imatges s'observa la intensitat dels pixels i els pics de intensitat ocasionats pels carrils poden ser detectats.

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/Figure_3.jpg" width="48%"/> 
</p>


Per a detectar els pics d'intensitats s'utilitza l'algorisme de "Canny Edge Detection".

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1_CANNY.jpg" width="48%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2_CANNY.jpg" width="48%"/> 
</p>
