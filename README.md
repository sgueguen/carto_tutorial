# carto tutorial

## Installation

* Installation de `conda`

Télécharger l'installateur ici : https://docs.conda.io/en/latest/miniconda.html

fichier à télécharger : Miniconda3-latest-Linux-x86_64.sh

puis installer:

```bash
$ bash Miniconda3-latest-Linux-x86_64.sh
```

* Désactiver l'environement `conda` de base

```bash
$ conda config --set auto_activate_base false
```

* Création d'un `conda-venv`

```bash
$ conda create --name carto_tutorial_venv
```

* activer l'environnement

```bash
$ conda activate -n carto_tutorial_venv
```


* Installer les dépendances

```bash
$ conda install --name carto_tutorial_venv numpy netCDF4 cartopy
```

* Liste les environnements conda

```bash
$ conda env list
```

## Test

Il faut d'abord ajouter le fichier netcdf dans le répertoire courant

* Lancer le code

```bash
$ python  test_cartopy.py
```
