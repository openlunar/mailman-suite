# mailman-suite
A Mailman3 Suite Install

Forked from https://gitlab.com/mailman/mailman-suite

## Install

```
git clone https://github.com/openlunar/mailman-suite.git

cd mailman-suite
python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install wheel
pip install -r requirements.txt

cd mailman-suite_project
python install.py
python3 manage.py migrate
```
