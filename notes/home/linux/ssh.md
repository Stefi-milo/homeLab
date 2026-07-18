ssh keygen

ssh milo@192.168.100.20 -p 2200

# Forward to remote server and port running there
ssh -N -L 88888:localhost:80 marek@server2
ssh -N -L localhost:88888:127.0.0.1:80 marek@server2

# Conncting to server2 throuh the jumphost serer1
ssh -A -J kata@server1 marek@server2 
ssh  -N kata@server1 -J marek@server2 localhost:88888:localhost:80

# The same like here
ssh  -N kata@server1 -J marek@server2 88888:localhost:80

