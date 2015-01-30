import sublime, sublime_plugin
import time
from os.path import expanduser

class TimetrackerCommand(sublime_plugin.EventListener):
  def on_post_save(self, view):
    home       = expanduser("~")
    string     = open(home + '/.sublime-timetracker', 'r+').read()
    saved_file = view.file_name()
    output     = saved_file + ":" + str(time.time()) + "\n"
    string     = string + output;
    f          = open(home + '/.sublime-timetracker', 'w')

    f.write(string)
    f.close()

    #data = open(home + "/.sublime-timetracker", "r+").read()
    #array = data.split("\n")
    #for (i, item) in enumerate(array):
    #  array[i] = item.split(":")

    #for (i, item) in enumerate(array):
    #  d = datetime.utcfromtimestamp(float(array[i][1]))
    #  array[i] = [array[i][0], d]
