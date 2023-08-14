while true
do
  loginCount=`ps -ef | grep testPhone007.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone007.py
  fi
  sleep 1
done
