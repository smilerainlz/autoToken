while true
do
  loginCount=`ps -ef | grep testPhone-swithTab1.py | wc -l`
  if (($loginCount < 2))
  then
    python3 testPhone-swithTab1.py
  fi
  sleep 1
done
