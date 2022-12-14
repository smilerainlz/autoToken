while true
do
  loginCount=`ps -ef | grep myPhone-first.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone-first.py
  fi
  sleep 1
done
