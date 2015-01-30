import sublime, sublime_plugin

import time

class TimetrackerCommand(sublime_plugin.EventListener):
  def on_post_save(self, view):
    # string = open("/Users/sarbull/.sublime-timetracker", 'r+').read()
    save_to = os.path.join(os.path.dirname(__file__), '.sublime-timetracker')
    string = open(save_to, 'r+').read()

    # Get the filename of your saved file
    saved_file = view.file_name()

    # Check if your in any of your development projects   
    #if 'dev/projets' in saved_file:
    #project = saved_file.split('projects/')[1].split('/')[0]
    #output = project + ":" + str(time.time()) + "\n"
    output = saved_file + ":" + str(time.time()) + "\n"
    string = string + output;

    f = open(save_to, 'w')
    f.write(string)
    f.close()

    #  pass
