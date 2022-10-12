while true
do
  loginCount=`ps -ef | grep login.py | wc -l`
  if (($loginCount < 2))
  then
    nohup python3 login.py > login.log 2>&1 &
  fi
  sleep 1
done
