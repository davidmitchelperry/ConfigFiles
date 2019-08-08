# ConfigFiles

/.i3/config:

    I3 Config File 

/i3blocks.conf:

    i3 blocks config file that calls python script
    to read top 10 posts on /r/politics.
   
    Installation: 
        1.) Place file in /etc/
        2.) Replace rss file path to point to correct
            location
        

/.vim/bundle:

    Vim plugin folders cloned from github are empty.
    They will have to be re-cloned to work.

/.vimrc
    
    My vimrc file with some minor changes from the
    default config 

/.Xresources

    Xresources file containing settings for "x"
    controlled programs. 

    Used to format my rxvt-unicode options

/UI/rss/rss.py

    Python script that displays the top 10 reddit
    posts for /r/politics. Rotates to a new post
    each time it is executed.

/UI/rss/rss_count:
    
    Simple text file to keep track of the last
    post number printed by rss.py
