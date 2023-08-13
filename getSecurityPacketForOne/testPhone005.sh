while true
do
  loginCount=`ps -ef | grep testPhone005.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone005.py
  fi
  sleep 1
done
