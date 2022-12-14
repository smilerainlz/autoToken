while true
do
  loginCount=`ps -ef | grep myPhone-first-part2.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhone-first-part2.py
  fi
  sleep 1
done
