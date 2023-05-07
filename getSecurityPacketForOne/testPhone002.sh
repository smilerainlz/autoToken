while true
do
  loginCount=`ps -ef | grep testPhone002.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone002.py
  fi
  sleep 1
done
