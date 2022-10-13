ps -ef | grep Charles | grep Applications | awk '{print $2}' | xargs kill
sleep 5
open /Applications/Charles.app
sleep 10
