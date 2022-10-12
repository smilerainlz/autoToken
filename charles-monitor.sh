while true
do
    ps -ef | grep Charles | grep Applications | awk '{print $2}' | xargs kill
    sleep 10
    open /Applications/Charles.app
    sleep 18000
done
