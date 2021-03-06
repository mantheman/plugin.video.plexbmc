import os
import xbmcaddon
import xbmc


class AddonSettings:

    def __init__(self, name):
        print "PleXBMC.setting -> Reading settings configuration"
        self.settings = xbmcaddon.Addon(name)
        self.stream = self.settings.getSetting('streaming')

        self.kodi_settings = None
        try:
            self.kodi_settings = parse(xbmc.translatePath('special://userdata/guisettings.xml'))
        except:
            print "PleXBMC.setting -> Unable to read KODI's guisettings.xml"

    def open_settings(self):
        return self.settings.openSettings()

    def get_setting(self, name):
        value = self.settings.getSetting(name)

        if value is None or value == '':
            print "PleXBMC.setting -> setting: %s is : %s" % (name, value)

        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            return value

    def get_debug(self):
        if self.settings.getSetting('debug') == 'true':
            print "PLEXBMC < 3.6 debug setting detected - settings must be re-saved"
            self.settings.setSetting('debug', '2')
            return 2
        elif self.settings.getSetting('debug') == 'false':
            print "PLEXBMC < 3.6 debug setting detected - settings must be re-saved"
            self.settings.setSetting('debug', '1')
            return 0

        return int(self.settings.getSetting('debug'))

    def set_setting(self, name, value):
        if value == True:
            value = "true"
        elif value == False:
            value = "false"

        self.settings.setSetting(name, value)

    def get_wakeservers(self):
        wakeserver = []
        for servers in range(1, 12):
            wakeserver.append(self.settings.getSetting('wol%s' % servers))
        return wakeserver

    def get_stream(self):
        return self.stream

    def set_stream(self, value):
        self.stream = value

    def dump_settings(self):
        return self.__dict__

    def update_master_server(self, value):
        print "Updating master server to%s" % value
        self.settings.setSetting('masterServer', '%s' % value)

    def get_kodi_setting(self, name):

        if self.kodi_settings is None:
            return False
        try:
            return self.kodi_settings.getElementsByTagName(name)[0].firstChild.nodeValue
        except:
            return ""
