import sublime, sublime_plugin
import os.path

class EnableDynamicCompletionCommand(sublime_plugin.WindowCommand):
    def run(self):
    	s = sublime.load_settings("Preferences.sublime-settings")
        #current = s.get("gml_dynamic_completion_enabled", True)
        s.set("gml_dynamic_completion_enabled", True)
        sublime.save_settings("Preferences.sublime-settings")
