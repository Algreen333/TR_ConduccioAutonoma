

# Conducció Autònoma mitjançant la Visió per Computador i la Intel·ligència Artificial

Aquest repositori conté el codi desenvolupat per un Treball de Recerca juntament amb altres recursos.

Les tres funcionalitats, essencials per a un sistema de conducció autònoma, que s'han desenvolupat són:
 - Detecció i seguiment de carrils
 - Detecció d'obstacles
 - Pathfinding o navegació
 
 
 ****


## Detecció i seguiment de carrils
Aquest mòdul o sistema té la funció de detectar els carrils a partir de les imatges, després calcular-ne la posició i orientació relativa amb el vehicle i, finalment, estimar el gir que s'ha de realitzar per a mantenir el vehicle centrat.

### Processat base
El codi per a processar vídeos o imatges amb el sistema de detecció de carrils s'executa amb `Lane_Detection/lane_detection.py`. S'executa amb:
``python lane_detection.py input save_path --frame_rate [frame_rate] --width [width] --height [height] --beamng --port [port]``

El paràmetre `input` especifica la ruta del vídeo o l'ID/ruta de la càmera.
El paràmetre `save_path` especifica la carpeta on es desaran les captures.
L'opció `frame_rate` permet especificar els fotogrames per segon del processat.
Les opcions `width` i `height` permeten modificar la resolució de la càmera si es tracta d'un vídeo en temps real.
Amb l'opció `--beamng` s'habilita la sortida per a la implementació al BeamNG. El port de la connexió pot ser configurat amb l'opció `--port`

Executant el codi s'obrirà una finestra on es mostrarà les deteccions que realitza el sistema:

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG1_ALL.jpg" width="49.5%"/> 
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/BNG2_ALL.jpg" width="49.5%"/> 
</p>

Prement la tecla `t` es realitzarà una captura del fotograma actual, que serà desada amb un nom a l'atzar a la carpeta especificada amb el paràmetre `save_path`. Prement la tecla `q` s'aturarà el codi.


### Implementació al BeamNG
El sistema de detecció de carrils pot ser implementat al BeamNG, podent controlar el gir del vehicle (no la velocitat, però).
#### Setup
Per a la implementació al BeamNG és necessari poder gravar en temps real el vídeo del joc. Per a fer-ho s'utilitza la càmera virtual de l'OBS Studio ([Open Broadcaster Software](https://obsproject.com)). 
Un cop instal·lat i configurat, s'ha d'afegir el joc a l'escena i finalment activar la càmera virtual:
<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/Setup/captura_escena.jpg" width="49.5%"/> 
</p>

Dins del videojoc, la càmera s'ha de col·locar a la part frontal del vehicle, de tal manera que quedi el capó fora de vista. Per tal de fer-ho de manera precisa sense requerir configuracions addicionals, s'ha de prémer la tecla `4` (que col·locarà la càmera en mode "vista lliure") i prémer la tecla `w` fins que el capó del vehicle deixi de veure's.
També seria necessari ocultar elements de la *HUD* o qualsevol element dins del camp de visió del sistema (superfície marcada amb color verd a la visualització del programa) que pugui interferir.
<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/Setup/captura_beamng.jpg" width="49.5%"/> 
</p>

#### Execució
Per a la implementació al BeamNG hi ha dos programes que funcionen en paral·lel. 

El primer és el del processat d'imatge. S'executa amb el mateix fitxer que per al processat de vídeos o en temps real, però requereix el paràmetre `--beamng` i posar com a input l'ID de la càmera virtual del OBS:
`python lane_detection.py 0 --beamng`

L'altre programa és el que es comunicarà amb el joc per a girar el vehicle. Ho realitza emulant un controlador de videojoc:
`python control_system_beamng.py [port]`
El port, per defecte 5455, també pot ser modificat; aquest ha de concordar amb el port per al programa de detecció de carrils.

Un cop executats els dos programes en paral·lel el sistema pot ser activat/desactivat prement la tecla `l` i el vehicle començarà a realitzar el gir de forma autònoma. El cotxe s'haurà d'accelerar de forma manual o programant el control de creuer del mateix joc.

<p align="center">
<img src="https://github.com/Algreen333/TR_ConduccioAutonoma/blob/main/Recursos/imgs/LaneDetection/gif.gif" width="49.5%"/> 
</p>
