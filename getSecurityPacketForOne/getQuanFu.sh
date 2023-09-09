while true
do
  loginCount=`ps -ef | grep getQuanFu.py | wc -l`
  if (($loginCount < 2))
  then
    python3 getQuanFu.py
  fi
  sleep 1
done
