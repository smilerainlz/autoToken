while true
do
  loginCount=`ps -ef | grep getQuanFu007.py | wc -l`
  if (($loginCount < 2))
  then
    python3 getQuanFu007.py
  fi
  sleep 1
done
