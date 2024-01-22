

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
``python lane_detection.py input save_path --frame_rate --width --height ``

El praràmetre `input` especifica la ruta del vídeo o l'ID/ruta de la càmera.
El paràmetre `save_path` especifica la carpeta on es desaran les captures.
L'opció `frame_rate` permet especificar els fotogrames per segon del processat.
Les opcions `width` i `height` permeten modificar la resolució de la càmera si es tracta d'un vídeo en temps real.

Executant el codi s'obrirá una finestra on es mostrarà les deteccions que realitza el sistema:

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1_ALL.jpg" width="49.5%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2_ALL.jpg" width="49.5%"/> 
</p>

Prement la tecla `t` es realitzarà una captura del frame actual, que serà desada amb un nom al atzar a la carpeta especificada amb el paràmetre `save_path`. Prement la tecla `q` s'aturarà el codi.
