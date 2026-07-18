touch file.txt              		# most common, creates empty file
nano file.txt               		# opens editor, save to create
vim file.txt                		# same with vim
echo "" > file.txt          		# creates file with empty line
echo "content" > file.txt   		# creates file with content
cat > file.txt              		# type content, Ctrl+D to save
> file.txt                  		# shortest way, just redirect
tee file.txt < /dev/null    		# using tee
install -m 644 /dev/null file.txt  	# creates with specific permissions
cp /dev/null file.txt       		# copy nothing into new file
truncate -s 0 file.txt      		# create with exact size 0
heredoc:
cat > file.txt << EOF
content here
EOF
