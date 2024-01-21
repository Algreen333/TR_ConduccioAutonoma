

# Conducció Autònoma mitjançant la Visió per Computador i la Intel·ligència Artificial

Aquest repositori conté el codi desenvolupat per un Treball de Recerca juntament amb altres recursos.

Les tres funcionalitats, essencials per a un sistema de conducció autònoma, que s'han desenvolupat són:
 - Detecció i seguiment de carrils
 - Detecció d'obstacles
 - Pathfinding o navegació
 
 ****

## Detecció i seguiment de carrils
Aquest mòdul o sistema té la funció de detectar els carrils a partir de les imatges, després calcular-ne la posició i orentació relativa amb el vehicle i, finalment, estimar el gir que s'ha de realitzar per a mantenir el vehicle centrat.

#### Processat base
El codi per a processar vídeos o imatges amb el sistema de detecció de carrils s'executa amb `Lane_Detection/lane_detection.py`. S'executa amb:
````python lane_detection.py --live_feed input_source ````

Amb l'opció `--live_feed` es pot fer que el programa processi una càmera en temps real, si no es processarà un vídeo.
El praràmetre `input_source` especifica la ruta del vídeo o l'ID/ruta de la càmera.

Executant el codi s'obrirá una finestra on es mostrarà les deteccions que realitza el sistema:

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1_wCENTERS.jpg" width="49.5%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2_wCENTERS.jpg" width="49.5%"/> 
</p>
