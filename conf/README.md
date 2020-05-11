# Production Configuration Files

## Postfix

This file lives in /etc/postfix as main.cf

```
cp postfix.cp /etc/postfix/main.cf
```

## Apache

This file lives in /etc/apache2 with a symlink from sites-available to sites-enabled.

```
sudo cp apache.conf /etc/apache2/sites-available/mailman-ssl.conf
cd /etc/apache2/sites-enabled
sudo ln -s ../sites-available/mailman-ssl.conf .
```
