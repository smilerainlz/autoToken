while true
do
  loginCount=`ps -ef | grep ipad.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad.py
  fi
  sleep 1
done
