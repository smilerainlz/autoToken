while true
do
  loginCount=`ps -ef | grep login.py | wc -l`
  if (($loginCount < 2))
  then
    python3 login.py
  fi
  sleep 1
done
