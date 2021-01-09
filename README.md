# Python 101

# Setup and Installation
## MacOS Catalina
**Steps for installation:**
* Install HomeBrew 
  * `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
* Install Python 3
  * `$ brew install python`
* Export the path into `~/.zshrc` (create if it doesn't exist)
  * `export PATH="/usr/local/opt/python/libexec/bin:$PATH"`
* Verify your installation
  * `$ python --version` ⭢ Python 3.x.x printed
  * `$ python2 --version` ⭢ Python 2.x.x printed
  * `$ pip --version` ⭢ pip x.x.x from ... (python 3.x)
  
# Virtual Environment
## Pipenv
* `$ pip install --user pipenv`
* `$ cd project_folder`
* `$ pipenv install requests`
* `$ pipenv run python main.py`
* `$ pipenv shell`

## Virtualenv
* `$ pip install virtualenv`
* `$ cd project_folder`
* `$ virtualenv venv`
* `$ source venv/bin/activate`
* `$ pip install requests`
* `$ deactivate` while inside a (venv)
* `$ pip freeze > requirements.txt`
* `$ pip install -r requirements.txt`
