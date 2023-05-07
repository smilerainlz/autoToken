while true
do
  loginCount=`ps -ef | grep testPhone001.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone001.py
  fi
  sleep 1
done
