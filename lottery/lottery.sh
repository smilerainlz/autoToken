while true
do
  loginCount=`ps -ef | grep lottery.py | wc -l`
  if (($loginCount < 2))
  then
    python3 lottery.py
  fi
  sleep 1
done
