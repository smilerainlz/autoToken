while true
do
  loginCount=`ps -ef | grep testPhone011.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone011.py
  fi
  sleep 1
done
