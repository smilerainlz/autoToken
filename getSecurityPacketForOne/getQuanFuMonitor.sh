while true
do
  loginCount=`ps -ef | grep getQuanFuMonitor.py | wc -l`
  if (($loginCount < 2))
  then
    python3 getQuanFuMonitor.py
  fi
  sleep 1
done
