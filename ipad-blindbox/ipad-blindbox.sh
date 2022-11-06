while true
do
  loginCount=`ps -ef | grep ipad-blindbox.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad-blindbox.py
  fi
  sleep 1
done
