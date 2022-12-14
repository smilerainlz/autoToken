while true
do
  loginCount=`ps -ef | grep ipad-1.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad-1.py
  fi
  sleep 1
done
