while true
do
  loginCount=`ps -ef | grep myPhone-swithTab1.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone-swithTab1.py
  fi
  sleep 1
done
