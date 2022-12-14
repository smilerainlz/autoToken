while true
do
  loginCount=`ps -ef | grep myNewPhone.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myNewPhone.py
  fi
  sleep 1
done
