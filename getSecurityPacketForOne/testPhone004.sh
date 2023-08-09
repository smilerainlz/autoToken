while true
do
  loginCount=`ps -ef | grep testPhone004.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone004.py
  fi
  sleep 1
done
