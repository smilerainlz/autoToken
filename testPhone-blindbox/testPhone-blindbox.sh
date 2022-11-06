while true
do
  loginCount=`ps -ef | grep testPhone-blindbox.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone-blindbox.py
  fi
  sleep 1
done
