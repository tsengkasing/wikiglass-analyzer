# Wikiglass-analyzer - a data visulization system for mediawiki #

![](https://img.shields.io/badge/PyMySQL-0.9.3-brightgreen.svg?style=flat-square) ![](https://img.shields.io/badge/DBUtils-1.3-brightgreen.svg?style=flat-square)


## :rocket: Installing Virtual Environment and Dependencies ##
**Step1.** Installing conda, you may find the installation guide [here](https://conda.io/docs/user-guide/install/index.html)

**Step2.** Create conda virtual environment from ``requirements.txt``
Navigate to the root directory of wikiglass-analyzer and run:

  ```bash
    $ conda env create -n wikiglass_venv -f requirements.txt
  ```

You can check wether the environment has been created for you by running:

  ```bash
    $ conda env list
  ```

Then, ``activate`` the environment

  ```
    $ source activate wikiglass_venv
  ```

For more informatin about conda, please refer to [conda user guide](https://conda.io/docs/user-guide/index.html)

**Step3.** Install ``pymysql``, it's a python mysql client library.

    pip install PyMySQL

For more informatin about pymysql, please refer to [this link](https://pypi.org/project/PyMySQL/)


**Step4.** Install ``DBUtils``. DBUtils is a suite of Python modules allowing to connect in a safe and efficient way between a threaded Python application and a database.

    pip install DBUtils

For more informatin about pymysql, please refer to [DBUtils user guide](https://cito.github.io/DBUtils/UsersGuide.html#installation-as-a-standalone-top-level-package)

## Unit Test

```bash
$ python -m unittest tests/utilities/text_extracter.py
```
