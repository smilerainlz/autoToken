while true
do
  loginCount=`ps -ef | grep ipad-sencond.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad-sencond.py
  fi
  sleep 1
done
