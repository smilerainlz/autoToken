while true
do
  loginCount=`ps -ef | grep testPhone006.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone006.py
  fi
  sleep 1
done
