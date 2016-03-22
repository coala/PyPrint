import subprocess

from pyprint.ClosableObject import ClosableObject
from pyprint.Printer import Printer


class EspeakPrinter(Printer, ClosableObject):

    def __init__(self):
        """
        :raises EnvironmentError: If VoiceOutput is impossible.
        """
        Printer.__init__(self)
        ClosableObject.__init__(self)
        # TODO retrieve language from get_locale and select appropriate voice

        try:
            self.espeak = subprocess.Popen(['espeak'], stdin=subprocess.PIPE)
        except OSError:  # pragma: no cover
            print("eSpeak doesn't seem to be installed. You cannot use the "
                  "voice output feature without eSpeak. It can be downloaded"
                  " from http://espeak.sourceforge.net/ or installed via "
                  "your usual package repositories.")
            raise EnvironmentError
        except subprocess.SubprocessError:  # pragma: no cover
            print("Failed to execute eSpeak. An unknown error occurred. "
                  "This is a bug. We are sorry for the inconvenience. "
                  "Please contact the developers for assistance.")
            raise EnvironmentError

    def _close(self):
        self.espeak.stdin.close()

    def _print(self, output, **kwargs):
        self.espeak.stdin.write(output.encode())
        self.espeak.stdin.flush()
