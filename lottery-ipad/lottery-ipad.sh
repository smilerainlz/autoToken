while true
do
  loginCount=`ps -ef | grep lottery-ipad.py | wc -l`
  if (($loginCount < 2))
  then
    python3 lottery-ipad.py
  fi
  sleep 1
done
