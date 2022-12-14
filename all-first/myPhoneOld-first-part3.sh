while true
do
  loginCount=`ps -ef | grep myPhoneOld-first-part3.py | wc -l`
  if (($loginCount < 2))
  then
    python3 myPhoneOld-first-part3.py
  fi
  sleep 1
done
