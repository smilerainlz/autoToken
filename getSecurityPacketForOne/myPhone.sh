while true
do
  loginCount=`ps -ef | grep myPhone.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone.py
  fi
  sleep 1
done
