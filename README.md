# Wikiglass-analyzer - a data visulization tool for mediawiki #


## Installing Virtual Environment and Dependencies ##
**Step1.** Installing conda, you may find the installation guide here:

    https://conda.io/docs/user-guide/install/index.html

**Step2.** Create conda virtual environment from ``requirements.txt``
Navigate to the root directory of wikiglass-analyzer and run:

    conda env create -n wikiglass_venv -f requirements.txt

You can check wether the environment has been created for you by running:

    conda env list

Then, ``activate`` the environment

    source activate wikiglass_venv

For more informatin about conda, please refer to [conda user guide](https://conda.io/docs/user-guide/index.html)

**Step3.** Install ``pymysql``, it's a python mysql client library.

    pip install PyMySQL

For more informatin about pymysql, please refer to [this link](https://pypi.org/project/PyMySQL/)
