import Config_Storage as cfg

def sanitize(listToSanitize):
    result = list()
    for string in listToSanitize:
        result.append(str(string).replace('"', ''))
    return result

class ConfExport:

    def __init__(self, sFileInput):
        self.conf = cfg.ConfStorage(sFileInput)


    def section21(self):
        result = [self.conf.name, self.conf.version, self.conf.build, self.conf.number]
        return sanitize(result)

    def section22(self):
        result = list()
        temp = self.conf.getConfig("config system global")
        result.append(self.conf.getSet3("set admin-sport", temp))
        self.conf.setCurrentConfig("config system admin")
        self.conf.setEdit('edit "admin"')
        temp = [self.conf.getSet("set trusthost1"), self.conf.getSet("set trusthost2"), self.conf.getSet("set trusthost3")]
        for item in temp:
            result.append(item)
        return sanitize(result)
    
    def section23(self):
        result = list()
        temp = self.conf.getConfig("config system dns")
        result.append(self.conf.getSet3("set primary", temp))
        result.append(self.conf.getSet3("set secondary", temp))
        result.append(self.conf.getSet3("set domain", temp))
        return sanitize(result)

    def section24(self):
        result = list()
        self.conf.setCurrentConfig("config system interface")
        AllEdits = self.conf.getAllEdits()
        edits = list()
        for edit in AllEdits:
            if 'port' in edit:
                edits.append(edit)
        del AllEdits
                
        for edit in edits:
            result.append(edit)
            result.append(self.conf.getSet2("edit "+edit, "set alias"))
            result.append(self.conf.getSet2("edit "+edit, "set ip"))
            result.append(self.conf.getSet2("edit "+edit, "set dhcp-relay-ip"))
        return sanitize(result)
    
    def section25(self):
        result = list()
        self.conf.setCurrentConfig("config router static")
        edits = self.conf.getAllEdits()
        result.append(len(edits))
        prioritats = list()
        for edit in edits:
            self.conf.setEdit('edit '+edit)
            result.append(self.conf.getSet('set gateway'))
            result.append(self.conf.getSet('set device'))
            sPrio = self.conf.getSet('set priority')
            result.append(sPrio)
            if sPrio.isnumeric():
                prioritats.append(int(sPrio))
            
        index = prioritats.index(min(prioritats))
        result.insert(index+1, self.conf.getSet2('edit '+edits[index], 'set gateway'))
        result.insert(index+2, self.conf.getSet2('edit '+edits[index+1], 'set gateway'))
        self.conf.setCurrentConfig('config system link-monitor')
        edits = self.conf.getAllEdits()
        for edit in edits:
            self.conf.setEdit('edit '+edit)
            sets = self.conf.getSets(['set server', 'set gateway-ip', 'set srcintf', 'set interval', 'set failtime', 'set recoverytime'])
            for item in sets:
                result.append(item)
        return sanitize(result)

    def section26(self):
        result = list()
        self.conf.setCurrentConfig('config firewall address')
        edits = [
                '"inside_srv"',
                '"inside_wrk"',
                '"cloud1"',
                '"cloud2"',
                '"srv-demeter"',
                '"srv-devrepo"',
                '"srv-nebulaz"',
                '"vpn-net"'
                ]

        for edit in edits:
            self.conf.setEdit('edit '+edit)
            result.append(edit)
            result.append('Address')
            setType = self.conf.getSet('set type')
            if 'iprange' in setType:
                setType = 'Range'
                startIp = self.conf.getSet('set start-ip')
                endIp = self.conf.getSet('set end-ip')
                result.append(startIp+'.'+endIp)
                result.append('Any')
            else:
                setType = 'Subnet'
                ip = self.conf.getSet('set subnet')
                if ip != '-':
                    ip = ip[0:ip.index(' ')]
                result.append(ip)
                result.append('Any')
            result.append(setType)
        return sanitize(result)

    def section27(self):
        result = list()
        self.conf.setCurrentConfig('config firewall service custom')
        edits = self.conf.getAllEdits()
        for edit in edits:
            result.append(edit)
            self.conf.setEdit('edit '+edit)
            sets = self.conf.getSets(['set category', 'set tcp-portrange', 'set udp-portrange', 'set protocol'])
            sets[1] = sets[1].replace(' ', '\n')
            sets[2] = sets[2].replace(' ', '\n')
            for sSet in sets:
                result.append(sSet)
        return sanitize(result)

    def section28(self):
        result = list()
        self.conf.setCurrentConfig('config firewall vip')
        edits = ['"VIP_srv-01"', '"VIP-srv-02"']
        for edit in edits:
            result.append(edit)
            self.conf.setEdit('edit '+edit)
            sets = self.conf.getSets(['set extintf', 'set extip'])
            result.append(sets[0]+'/'+sets[1])
            sets = self.conf.getSets(['set extport', 'set protocol'])
            result.append(sets[0]+'/'+sets[1])
            result.append(self.conf.getSet('set mappedip'))
            sets = self.conf.getSets(['set mappedport', 'set protocol'])
            result.append(sets[0]+'/'+sets[1])
        return sanitize(result)
    
    def section29(self):
        result = list()
        self.conf.setCurrentConfig('config firewall policy')
        edits = self.conf.getAllEdits()
        for edit in edits:
            self.conf.setEdit('edit '+edit)
            result.append(edit)
            sets = self.conf.getSets([
                'set srcintf',
                'set srcaddr',
                'set dstintf',
                'set srcaddr',
                'set groups',
                'set dstaddr',
                'set service',
                'set action',
                'set av-profile',
                'set webfilter-profile',
                'set application-list',
                'set ips-sensor',
                'set ssl-shh-profile',
                'set logtraffic',
                'set nat'
            ])
            result.append(sets[0]+'/'+sets[1])
            result.append(sets[2])
            result.append(sets[3]+'('+sets[4]+')')
            for i in range(5, 15):
                result.append(sets[i])
        return sanitize(result)

    def section210(self):
        self.conf.setCurrentConfig('config antivirus profile')
        edits = self.conf.getAllEdits()
        edits.remove('"default"')
        result = edits
        return sanitize(result)

    def section211(self):
        self.conf.setCurrentConfig('config webfilter profile')
        allEdits = ['"default"', '"web-filter-flow"',  '"monitor-all"', '"flow-monitor-all"']
        edits = self.conf.getAllEdits()
        for edit in allEdits:
            edits.remove(edit)
        result = edits
        return sanitize(result)
    
    def section212(self):
        result = list()
        self.conf.setCurrentConfig('config application list')
        result.append(self.conf.getAllEdits()[-1])
        return sanitize(result)
    
    def section213(self):
        result = list()
        self.conf.setCurrentConfig('config ips sensor')
        edit = self.conf.getAllEdits()[-1]
        result.append(edit)
        self.conf.setEdit(edit)
        sets = self.conf.getSets(['set location', 'set severity', 'set os'])
        for item in sets:
            result.append(item)
        return sanitize(result)
    
    def draw(self):
        result = list()
        temp = self.section24()
        result.append(temp[0]) # draw[0] = Port1
        result.append(temp[2].split(" ")[0]) # draw[1] = IP Port1
        result.append(temp[4]) # draw[2] = Port2
        result.append(temp[6].split(" ")[0]) # draw[3] = IP Port2
        result.append(temp[8]) # draw[4] = Port3
        result.append(temp[10].split(" ")[0]) # draw[5] = IP Port3
        result.append(temp[12]) # draw[6] = Port4
        result.append(temp[14].split(" ")[0]) # draw[7] = IP Port4

        temp = self.section25()
        result.append(temp[1]) # draw[8] = Line from Port1 (IP de sortida internet principal)
        result.append(temp[2]) # draw[9] = Line from Port4 (IP de Backup + WIFI)

        temp = self.section26()
        result.append(temp[0]) # draw[10] = Line from Port2 (Text - inside_srv)
        result.append(temp[2]) # draw[11] = Line from Port2 (IP/DNS under inside_srv)
        result.append(temp[5]) # draw[12] = Line from Port3 (Text - inside_wrk)
        result.append(temp[7]) # draw[13] = Line from Port3 (IP/DNS under inside_wrk)

        return result
