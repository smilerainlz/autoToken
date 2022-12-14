while true
do
  loginCount=`ps -ef | grep myOldPhone.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myOldPhone.py
  fi
  sleep 1
done
