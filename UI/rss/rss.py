from subprocess import Popen, PIPE

REDDIT_POLITICS_NUM = 10

fname = "/home/david/UI/rss/rss_count"

with open(fname) as f:
    rss_count = int(f.readlines()[0].strip())

if rss_count < REDDIT_POLITICS_NUM:

    process = Popen(["rsstail", "-N", "-1", "-u", "https://reddit.com/r/politics.rss"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.split("\n")

    print "Reddit(#" + str(rss_count + 1) + "): " + output[rss_count]

    with open(fname, "w") as f:
        f.write(str(rss_count + 1))

else:
    process = Popen(["rsstail", "-N", "-1", "-u", "https://reddit.com/r/politics.rss"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.split("\n")

    print "Reddit(#1): " + output[0]

    with open(fname, "w") as f:
        f.write(str(1))



