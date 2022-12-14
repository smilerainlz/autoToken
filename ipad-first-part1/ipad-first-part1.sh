while true
do
  loginCount=`ps -ef | grep ipad-first-part1.py | wc -l`
  if (($loginCount < 2))
  then
    python3 ipad-first-part1.py
  fi
  sleep 1
done
