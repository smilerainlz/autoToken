while true
do
  loginCount=`ps -ef | grep testPhone008.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone008.py
  fi
  sleep 1
done
