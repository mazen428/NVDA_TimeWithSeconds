import winKernel
import ui
from globalCommands import SCRCAT_SYSTEM
import scriptHandler
import globalPluginHandler


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @scriptHandler.script(
    # This is based on the NVDA dateTime script, just changed to allow getting the seconds as well.
        description=_(
            # No need to translate this as it is the same in NVDA.
            "If pressed once, reports the current time. If pressed twice, reports the current date"
        ),
        category=SCRCAT_SYSTEM,
        gesture="kb:NVDA+f12",
    )

    def script_dateTime(self, gesture):
        if scriptHandler.getLastScriptRepeatCount() == 0:
            text = winKernel.GetTimeFormatEx(
                winKernel.LOCALE_NAME_USER_DEFAULT, None, None, None
            )
        else:
            text = winKernel.GetDateFormatEx(
                winKernel.LOCALE_NAME_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None
            )
        ui.message(text)
