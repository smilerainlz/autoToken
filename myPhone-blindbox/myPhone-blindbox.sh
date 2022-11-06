while true
do
  loginCount=`ps -ef | grep myPhone-blindbox.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone-blindbox.py
  fi
  sleep 1
done
