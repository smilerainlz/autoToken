while true
do
  loginCount=`ps -ef | grep ipad-first.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad-first.py
  fi
  sleep 1
done
