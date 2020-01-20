# APISolarplane
Backend for the solar plane web app. By Alessandro Gregolin

* [Installing](#installing)
  * [Environment setup](#environment-setup)
  * [Install packages](#install-packages)


## Installing
### Environment setup
Do it all at once by typing the follwing command

```
$ conda env create -f environment.yml -n solarplane_api
```

Or do it step by step:

To create a new environment open a new terminal and type the following
```
$ conda create -n solarplane_api python=3.7
```
Then activate the environment
```
$ conda activate solarplane_api
```
Add conda-forge channel to install packages
```
$ conda config --add channels conda-forge
```

### Install packages

In order to install all necessary packages and also create the environment at once, type the follwing

```
$ conda env create -f environment.yml -n solarplane_api
```
