while true
do
  loginCount=`ps -ef | grep blindbox.py | wc -l`
  if (($loginCount < 2))
  then
    python3 blindbox.py
  fi
  sleep 1
done
