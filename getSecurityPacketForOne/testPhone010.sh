while true
do
  loginCount=`ps -ef | grep testPhone010.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone010.py
  fi
  sleep 1
done
