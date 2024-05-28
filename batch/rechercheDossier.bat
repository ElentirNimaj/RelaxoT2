:: Recherche de dossier spécifique
:: Auteur: B. Prigent
:: Creation: 06/05/24
:: Last Maj: 06/05/24

@echo off

cls

title Recherche dossier NODAL
set DATASET=C:\Users\bprigent\Datas\NODALHV

:: Créer un moyen de trier par ordre alphabétique
SET "sort[fwd]=(FOR %%S in (%%#%%) DO @ECHO %%S) ^| SORT"

::Pas besoin car ajoute une ligne vide
::echo.> %DATASET%\testtxtfile.txt

:: Création des dossiers, liste des différents fichiers par dossiers, transcription dans un fichier texte.
echo Liste de tous les dossiers
for /d %%A in (%DATASET%\*) do echo %%A 
echo.
echo Liste des dossiers Relaxo seulement
for /d %%A in (%DATASET%\*RELAXO*) do echo %%A
echo.
echo Liste des fichiers nifti dans un dossier relaxo.

if not exist %DATASET%\allFiles_RELAXO_20240419133106.txt (
    for /r %DATASET%\Dataset_NODAL_VS_001_489587_RELAXO_VHD_RELAXO_VHD_20240419133106 %%B in ("*.nii.gz") do (
	ECHO %%B>> %DATASET%\allFiles_RELAXO_20240419133106.txt
	)
) else (
        del %DATASET%\allFiles_RELAXO_20240419133106.txt
        for /r %DATASET%\Dataset_NODAL_VS_001_489587_RELAXO_VHD_RELAXO_VHD_20240419133106 %%B in ("*.nii.gz") do (
	    ECHO %%B>> %DATASET%\allFiles_RELAXO_20240419133106.txt
    )
)
