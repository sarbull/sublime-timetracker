import sublime, sublime_plugin
import time
from os.path import expanduser

class TimetrackerCommand(sublime_plugin.EventListener):
  def on_post_save(self, view):
    # string = open("/Users/sarbull/.sublime-timetracker", 'r+').read()

    home = expanduser("~")

    string = open(home + '/.sublime-timetracker', 'r+').read()

    # Get the filename of our saved file
    saved_file = view.file_name()

    # Check if your in any of your development projects   
    #if 'dev/projes' in saved_file:
    #project = saved_file.split('projects/')[1].split('/')[0]
    #output = project + ":" + str(time.time()) + "\n"
    output = saved_file + ":" + str(time.time()) + "\n"
    string = string + output;

    f = open(home + '/.sublime-timetracker', 'w')
    f.write(string)
    f.close()

    #  pass
