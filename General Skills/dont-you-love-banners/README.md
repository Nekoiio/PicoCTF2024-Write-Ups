This one is fun! First, they tell that the server is leaking on {port 1}, and to connect to {port 2} to access the app.

- At this point you could try to brute force the password prompt on {port 2}, but if you use nc with {port 1} you will get the password.
- Log in, and you will get a shell, navigate to /root and see that the flag is there but you can't read it.
- Look at the script, and we can see the script is able to read files when it displays a banner.
- Then we delete the banner on the home directory and symlink /root/flag to a file called banner on the home directory.
- Try to nc {port 2} again and there is your flag.
