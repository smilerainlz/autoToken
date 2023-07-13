while true
do
  loginCount=`ps -ef | grep testPhone003.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone003.py
  fi
  sleep 1
done
