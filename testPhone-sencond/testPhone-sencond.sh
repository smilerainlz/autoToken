while true
do
  loginCount=`ps -ef | grep testPhone-sencond.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone-sencond.py
  fi
  sleep 1
done
