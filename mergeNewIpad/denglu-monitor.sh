while true
do
  loginCount=`ps -ef | grep denglu.py | wc -l`
  if (($loginCount < 2))
  then
    python3 denglu.py
  fi
  sleep 1
done
