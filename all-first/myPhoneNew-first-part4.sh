while true
do
  loginCount=`ps -ef | grep myPhoneNew-first-part4.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhoneNew-first-part4.py
  fi
  sleep 1
done
