while true
do
  loginCount=`ps -ef | grep testPhone.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone.py
  fi
  sleep 1
done
