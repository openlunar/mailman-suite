#!/bin/bash
cd /opt/mailman/mailman-suite
source venv/bin/activate
cd webapp
python manage.py qcluster
cd -
