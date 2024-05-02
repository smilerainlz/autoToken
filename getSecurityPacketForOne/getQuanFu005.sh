while true
do
  loginCount=`ps -ef | grep getQuanFu005.py | wc -l`
  if (($loginCount < 2))
  then
    python3 getQuanFu005.py
  fi
  sleep 1
done
