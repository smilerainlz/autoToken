while true
do
  loginCount=`ps -ef | grep testPhone-first.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone-first.py
  fi
  sleep 1
done
