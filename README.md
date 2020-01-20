# APISolarplane
Backend for the solar plane web app. By Alessandro Gregolin

* [Installing](#installing)
  * [Environment setup](#environment-setup)
  * [Install packages](#install-packages)


## Installing
### Environment setup
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
The following packages need to be installed
  * Scipy
  * Plotly
  * Flask
  
In order to do so type the following command

```
$ conda install scipy plotly flask -n solarplane
```
