"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class AudioXBlock(XBlock):
    """
    This XBlock will play an MP3 file as an HTML5 audio element. 
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    src = String(
           scope = Scope.settings, 
           help = "URL for MP3 file to play"
        )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the AudioXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/audio.html")
        frag = Fragment(html.format(src = self.src))
        frag.add_css(self.resource_string("static/css/audio.css"))
        frag.add_javascript(self.resource_string("static/js/src/audio.js"))
        frag.initialize_js('AudioXBlock')
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("AudioXBlock",
             """<vertical_demo>
                  <audio src="http://localhost/Ikea.mp3"> </audio>
                  <audio src="http://localhost/skull.mp3"> </audio>
                  <audio src="http://localhost/monkey.mp3"> </audio>
                </vertical_demo>
             """),
        ]
