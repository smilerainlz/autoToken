while true
do
  loginCount=`ps -ef | grep myNewPhone-first.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myNewPhone-first.py
  fi
  sleep 1
done
