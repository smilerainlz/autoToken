ps -ef | grep 'monitor' | grep 'sh login' | awk '{print $2}' | xargs kill
ps -ef | grep 'login' | grep 'Python' | awk '{print $2}' | xargs kill
