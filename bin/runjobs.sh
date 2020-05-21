#!/bin/bash
cd /opt/mailman/mailman-suite
source venv/bin/activate
python webapp/manage.py runjobs $1
cd -
