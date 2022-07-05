# nohup : if you shut down cmd, nohup auto running its.
nohup python app.py &

# end nohup : if you shut down nohub
ps -ef | grep 'python app.py' | awk '{print $2}' | xargs kill