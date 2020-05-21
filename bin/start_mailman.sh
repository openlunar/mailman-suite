#!/bin/bash
cd /opt/mailman/mailman-suite
source venv/bin/activate
mailman -C /opt/mailman/mailman-suite/mailman.cfg start -q
