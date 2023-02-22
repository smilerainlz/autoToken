while true
do
  loginCount=`ps -ef | grep blindbox-ipad.py | wc -l`
  if (($loginCount < 2))
  then
    python3 blindbox-ipad.py
  fi
  sleep 1
done
