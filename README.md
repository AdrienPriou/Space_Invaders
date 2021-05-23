B3 Robotique & Ingénierie Systèmes - MicroPython - 2020/2021 - PRIOU Adrien

Pour conclure notre apprentissage en µPython et mettre en application les compétences acquises au cours de notre 3è année, nous avons eu comme projet a réalisé : le plus connu des jeux, le fameux Space Invaders. A partir de notre carte microcontrôleur (hardware) et de VisualStudioCode (software), et en nous aidant des différents tp réalisés durant les cours.

Nous avions ces différentes tâches obligatoires :

- Déplacement à l'accéléromètre
- Tir au bouton poussoir bleu
- Affichage par UART
- Certaines choses seront contrôlées par timer
- Liberté dans les règles du jeu



I - Présentation du projet 

Tout d'abord, au cours de l'année, nous avons eu un travaux-pratiques a réalisé, le fameux casse-brique qui à un rapport tout particulier avec ce projet.
En effet, il s'agissait de programmer ce jeu qui nous donnerait une bonne base par la suite pour notre projet.

Le jeu Space Invaders est un Shoot'em up, il s'agit d'un jeu en 2Dimensions. Le but du jeu est de tuer des aliens qui se déplacent latéralement au milieu de l'écran à l'aide d'un canon laser placé en bas de l'écran dirigeable horizontalement. 


   ![image](https://user-images.githubusercontent.com/70941244/119239151-8d24bf80-bb47-11eb-87ae-d41ea0b3ec8b.png)

Image d'une reproduction du jeu sur une borne d'arcade

Nous avions donc pour objectif et avec une certaine liberté, de reproduire le méchanisme du jeu et ses interfaces, à travers la console PowerShell sur Windows.
A travers un environnement virtuel, nous génerions notre jeu, en fonction de notre code et des spécificités données.



II - Mode d'emploi

Pour l'utilisation du jeu, rien de plus simple. 
- Brancher la carte STM32F408 sur votre ordinateur
- Ouvrir la console PowerShell sous Windows
- Lancer l'environnement virtuel .\venv\Scripts\Activate.ps1
- Lancer le programme du code à travers le PowerShell
- Une fênetre s'ouvre avec le jeu actif



III - Difficultés rencontrées 

Personnellement, ma plus grande difficulté a été de comprendre correctement le fonctionnement du Python, ayant de base des lacunes en programmation, à force d'entraînement, et d'entraide avec les camarades de classe, je suis parvenu au résultat final qui était demandé.
Pour ce qui est des différentes difficultés rencontrées par rapport au projet, je dirai qu'il s'agit de la représentation spatiale, du positionnement aux différentes coordonnées de chaque entitée.
D'autre part, il y a également l'utilisation du déplacement à l'accélèromètre qui pour ma part, la prise en main n'a pas été très facile au départ.



IV - Notions acquises au cours du projet

Personnellement, ce projet m'a permis de consolider certaines notions en C sur lesquels j'avais des difficultés comme par exemple les pointeurs, ou encore les chaînes de caractère. Cela peut paraître tout bête mais cela m'a débloqué sur certains points par rapport à l'immuabilité de certaines lignes de code. J'ai également découvert le 'elif' qui n'est utilisée qu'en Python qui est véritablement bien pratique !

V - Retour d'expérience du projet

En effet, ce projet m'a permis d'avoir une meilleure appréhension et approche quant au codage en Python qui va m'être très important dans le futur. Du fait qu'il soit un langage de choix donc à usage général, cela nous offre une multitude de possibilités tel que l'orienté objet dans notre cas. J'ai également amélioré ma logique quant au codage. 
Je trouve que l'idée d'un projet sur la conception en 2D d'un jeu est très original, et nous a tout bonnement permis de travailler sérieusement tout en faisant cela de manière ludique comme on était libre de pouvoir "customiser" le jeu en fonction de ses envies. Cela change vraiment de d'habitude et nous a donné envie de s'investir d'avantage.
