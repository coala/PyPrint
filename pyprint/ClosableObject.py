# -*- coding: utf-8 -*-
def close_objects(*objs):
    """
    Determines for all given objects if an object is closable and closes
    it if possible.

    :param objs: The objects to close.
    """
    for obj in objs:
        if isinstance(obj, ClosableObject):
            obj.close()


class ClosableObject:
    """
    Any class deriving from ClosableObject needs to be closed.
    """

    def __init__(self):
        self._closed = False

    def _close(self):
        """
        Override this method to implement own closing behaviour.
        """
        pass

    def close(self):
        """
        Closes any IO Objects this object may hold.
        """
        if not self._closed:
            self._close()
            self._closed = True

    def __del__(self):  # pragma: no cover
        """
        May warn if not closed properly - programmer error!

        Obviously cannot deterministically be tested.
        """
        if not self._closed:
            print("WARNING: {} was not closed. Cleaning up "
                  "automatically. Note that this cleanup may not work "
                  "on other interpreters and is nondeterministic."
                  .format(repr(self)))
            self.close()
