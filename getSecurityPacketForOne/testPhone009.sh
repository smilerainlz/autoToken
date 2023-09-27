while true
do
  loginCount=`ps -ef | grep testPhone009.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone009.py
  fi
  sleep 1
done
