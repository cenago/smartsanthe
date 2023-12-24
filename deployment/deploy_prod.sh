#!/bin/sh

ssh -tt root@165.22.213.30 <<EOF
  cd smartsanthe
  git pull
  source /root/smartsanthe/ssenv/bin/activate
  pip install -r requirements.txt
  ./manage.py makemigrations
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF