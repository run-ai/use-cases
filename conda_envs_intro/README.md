# Virtual Environments Intro with Conda
  
**A 13-minute live demo of this presentation can be found [here](https://youtu.be/ntf9gn0MHVA)**  
  
Slides can be found and downloaded here:
+ [PDF](./docs/conda_envs_intro.pdf)
+ [PPTX](./docs/conda_envs_intro.pptx)  

Conda also has a pdf [cheat sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf) available. 

## Installing conda & mamba
  
1. Install conda by following the installation instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)  
You will be asked to download a file and run it.
  
**Note:**
+ I recommend (and use) ‘miniconda’ over ‘anaconda’ because it is more lightweight. Anaconda is a much larger file with many pre-installed packages that you may not need.  
+ If you are using Windows, I recommend installing WSL (Windows Subsystem for Linux) with Ubuntu and installing conda on it. Instructions for setting up WSL can be found [here](https://ubuntu.com/wsl)
  
2. After installing conda, install mamba by running:  
~~~bash
conda install mamba -n base -c conda-forge
~~~  
More information on mamba can be found [here](https://github.com/mamba-org/mamba).
  
## Setup hints

**Never** install anything in your 'base' environment (installing mamba is an exception).  
By default, after installation, the 'base' environment will always be active when you open a terminal window.  
You can change this setting by running the following:  
~~~bash
conda config --set auto_activate_base false
~~~  

Conda install from 'channels'    
If you are going to use GPUs, you might want to add the NVIDIA cahnnel and the Rapids.ai channel:  
~~~bash
conda config --add channels nvidia
~~~  
~~~bash
conda config --add channels rapidsai
~~~  
  
The most popular, comprehensive, and well-maintained channel is 'conda-forge'  
You should make sure to add this channel, and add it *last* (the '--add' flag also sets the added cahnnel to the highest priority channel; we want conda-forge to be the highest priority channel).  
~~~bash
conda config --add channels conda-forge
~~~  
  
## The 3 main commands
   
1. To create an environment, use: mamba **create**
~~~bash
mamba create -n {YOUR-ENV-NAME}
~~~  
  
2. To activate an environment, use: conda **activate**
~~~bash
conda activate {YOUR-ENV-NAME}
~~~  
  
3. To install packages in an *active* environment, use: mamba **install**
~~~bash
mamba install {PACKAGE-NAME}
~~~  
To install packages in a *specific* (can be not-active) environment, add the '-n' flag, followed by an environment name.  
~~~bash
mamba install -n {ANY-ENV-NAME} {PACKAGE-NAME}
~~~  
  
### Note on creation, versions, and channels
  
You can **install packages when creating** a new environment, by specifying the package name(s) afterwards.  
~~~bash
mamba create -n {YOUR-ENV-NAME} {PACKAGE-NAME-1} {PACKAGE-NAME-2}
~~~  
  
You can **install a specific package version** by adding the '=' sign, followed by the version (no spaces). 
~~~bash
mamba create -n {YOUR-ENV-NAME} {PACKAGE-NAME}={VERSION}
~~~  
~~~bash
mamba install {PACKAGE-NAME}={VERSION}
~~~  
  
You can **install from a specific channel** by using the '-c' flag, followed by the channel.  
~~~bash
mamba create -n {YOUR-ENV-NAME} -c {CHANNEL-NAME} {PACKAGE-NAME}
~~~  
~~~bash
mamba install -c {CHANNEL-NAME} {PACKAGE-NAME}
~~~  
  
## Other important commands
  
+ To deactivate an environment, use: conda **deactivate**
~~~bash
conda deactivate
~~~  
  
+ To view all environment, use: conda **env list**
~~~bash
conda env list
~~~  
  
+ To view delete an environment, use: conda **env remove**
~~~bash
conda env remove -n {YOUR-ENV-NAME}
~~~  
  
+ To remove packages from an *active* environment, use: mamba **uninstall**
~~~bash
mamba uninstall {PACKAGE-NAME}
~~~  
  
+ To export an *active* environment, use: mamba **env export**
~~~bash
mamba env export > {ENV-EXPORT-FILE-NAME}
~~~  
  
+ To re-create an exported environment, use: mamba **env create**
~~~bash
mamba env create -f {ENV-EXPORT-FILE-NAME}
~~~  
  
## Miscellaneous

### Using pip

+ The preferred way of installing is using mamba/conda.
+ Sometimes mamba/conda don’t have the package version you need.
+ In these cases, you can use pip  
  
However, if you must you pip:
1. Use mamba/conda to install everything that you can
2. Use pip at the end

### Skip installation confirmation
  
By default, when installing mamba/conda packages, the user will be prompted to confirm the installs.  
You can skip this confirmation by adding the '-y' flag at the **end** of an install command:  
~~~bash
mamba install {PACKAGE-NAME} -y
~~~  

### Environment variables
  
It is possible to set environment variables in an activated environment, using the format:  
~~~bash
conda env configs vars set {ENV-VAR-NAME}={ENV-VAR-VALUE}
~~~  
  
To view variables in an activated environment, run:  
~~~bash
conda env configs vars list
~~~  
  
To remove environment variables in an activated environment, use this format:  
~~~bash
conda env configs vars unset {ENV-VAR-NAME}
~~~  
  
Set environment variables will be included in yaml file during exports, and will be set when recreating environments from yaml files.