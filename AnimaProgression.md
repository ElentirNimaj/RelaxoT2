# Anima progrès et problèmes

## Avant la semaine 19

Problème: Impossibilité à lancer le programme au départ. 
Cause: Mauvaise installation des binaries.
Solution: Reprise de l'installation avec Florent.

Problème: Programme ne tourne pas.
Cause: Mauvais format de fichier. 
Solution: Télécharger les données en Nifti et non en Dicom.

Problème: Version scriptée non fonctionnelle.
Cause: Ne connaît pas assez le bat. 
Solution: Tester et chercher des docs. 

Problème: Obtention d'une image de fin "vide".
Cause: 

## Semaine 19

(Peut être ajouter une ligne pour indiquer où on en est) 

Problème: Obtention d'une image de fin "vide".
Cause: ? 
Test: 	Essayer en ajoutant d'autres paramètres.
			N'a pas fonctionné.
		Essayer avec tous les fichiers d'un patient.
			
Problème: Fichiers qui s'écrasent
Cause: Pas de compteur simple (ou problème d'espace dans la déclaration de la variable). 
Solution: Besoin d'ajouter un extension localement et non pas %% qui est la variable de base mais !! 
qui est la variable dans notre boucle.

Problème: Fichiers bruités
Cause: Je donne les fichiers 1/1 et non pas une liste !
Solution: Faire une liste de fichier puis lancer le prog.

Problème: Semble bloquer après le loading. 
Cause: Fichiers pas dans l'ordre ? Commence par une ligne vide ? Peut être besoin de quelques 
minutes supplémentaires pour load ?
Solution: Le laisser mouliner !

Problème: Ne prend qu'un des 256 volumes.
Cause : L'utilisation du fichier txt.
Solution: Si un fichier plusieurs volumes alors le fichier brut. Si plusieurs fichiers 
alors un fichier txt qui liste les patshs.

Problème: Image très bruitée
Cause: ?
Test effectué: Utilisation d'un T1 pour mieux corriger les artefacts ? 
Solution

Problème: EPG ne semble pas fonctionner.
Cause: Présence du scalp ?
Test: Retirer le scalp.
