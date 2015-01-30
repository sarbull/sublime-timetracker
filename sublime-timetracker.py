import sublime, sublime_plugin

import time

class TimetrackerCommand(sublime_plugin.EventListener):
  def on_post_save(self, view):
    string = open('~/.sublime-timetracker', 'r').read()
    # Get the filename of your saved file
    saved_file = view.file_name()

    # Check if your in any of your development projects   
    if 'dev/projects' in saved_file:
      project = saved_file.split('projects/')[1].split('/')[0]
      output = project + ":" + str(time.time()) + "\n"
      string = string + output;

      f = open('~/.timetracker', 'w')
      f.write(string)
      f.close()

      pass
