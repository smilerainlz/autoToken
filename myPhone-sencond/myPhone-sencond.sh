while true
do
  loginCount=`ps -ef | grep myPhone-sencond.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone-sencond.py
  fi
  sleep 1
done
