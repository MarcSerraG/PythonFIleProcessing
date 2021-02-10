class ConfStorage:

    def __init__(self, sFileInput):
        with open( sFileInput, 'r' ) as fileInput:
            self.dicConfigs = dict() # Main dictionary with all configs
            self.sCurrentKey = "" # Current Key for the dictionary
            self.listCurrentKey = list() # Holds all the lines of the current selected config
            self.listEditContent = list() # Holds all the lines of the current selected edit within the current config

            for sLine in fileInput:
                ## Read initial variables like build number, version etc ##
                sLine.replace('\n', '').replace('\r', '')
                if "#config-version" in sLine:
                    configInfo = sLine.split("-")
                    self.name = configInfo[1].split("=")[1][3:6]
                    self.version = configInfo[2]
                    self.build = configInfo[4][5:8]
                    self.number = configInfo[5].split(":")[0]
                    ## More variables can be added if needed...
                
                ## Read a config block entirely ##
                elif "config" in sLine:
                    self.sCurrentKey = sLine
                    self.dicConfigs[self.sCurrentKey] = list()
                    self.listCurrentKey = self.dicConfigs.get(self.sCurrentKey)
                    while not sLine == 'end':
                        sLine = fileInput.readline().replace('\n', '').replace('\r', '')
                        self.listCurrentKey.append(sLine)
    

    ## Sets the current Key to work on ##
    ## Returns true if the key exists ##
    ## Returns false if it is not found ##
    def setCurrentConfig(self, sKey):
        for key in self.dicConfigs.keys():
            if sKey in key:
                self.sCurrentKey = key
                self.listCurrentKey = self.dicConfigs.get(key)
                return True
        return False
    

    
    ## Sets the current Edit list ##
    ## Returns false if the edit cannot be found, and leaves the current edit empty ##
    ## Returns true if the edit is found ##
    def setEdit(self, sEdit):
        found = False
        tabs = 0
        self.listEditContent = list()
        for sLine in self.listCurrentKey:
            if not found:
                if sEdit in sLine:
                    found = True
                    tabs = sLine.count(" ")-1
            elif ("next" in sLine) and (tabs == sLine.count(" ")):
                return True
            else:
                self.listEditContent.append(sLine)
        return False


    ## Returns the sub-values of the CURRENT edit ##
    ## Can be empty if the current Edit has not been set ##
    def getCurrentEdit(self):
        return self.listEditContent

    ## Finds the Set parameter from the CURRENT Edit list ##
    ## Returns the sanitised Set as a string with everything but the parameter ##
    ## Returns a "-" string if the Set is NOT found ##
    def getSet(self, sSet):
        found = False
        for line in self.listEditContent:
            if not found:
                if sSet in line:
                    listSet = line.split()
                    found = True
        if found:
            for part in sSet.split():
                if part in listSet:
                    listSet.remove(part)
            return " ".join(listSet)
        else:
            return "-"
    
    ## Finds all the Sets in the parameter list from CURRENT Edit list ##
    ## Returns a list of strings with all sanitised Sets, in order ##
    ## Includes not found sets as "-" ##
    def getSets(self, listSets):
        listSanitisedSets = list()
        for sSet in listSets:
            listSanitisedSets.append(self.getSet(sSet))
        return listSanitisedSets
    
    
    ## Convenience methods using previous ones for ease of processing ##
    ## Ugly, but convenient! ##

    ## Finds the set within the edit in the given config ##
    def getSet1(self, sConfig, sEdit, sSet):
        self.setCurrentConfig(sConfig)
        return self.getSet2(sEdit, sSet)

    ## Finds the set in the given edit ##
    ## Current config only ##
    def getSet2(self, sEdit, sSet):
        self.setEdit(sEdit)
        return self.getSet(sSet)
    
    ## Finds the set within the entire config ##
    ## getConfig must be called for the config parameter ##
    ## Returns the first set found only ##
    ## Returns '-' if the set is not found ##
    def getSet3(self, sSet, listConfig):
        self.listEditContent = listConfig
        return self.getSet(sSet)

    ## Returns a list with all sets from the given list of sets ##
    ## Searches only in the given edit ##
    def getSets1(self, listSets, sEdit):
        self.setEdit(sEdit)
        return self.getSets(listSets)

    ## Returns a list with all the unmodified config's content ##
    def getConfig(self, sConfig):
        self.setCurrentConfig(sConfig)
        return self.listCurrentKey
    
    ## Returns a list with every edit name within the current config ##
    ## Does NOT return their content ##
    def getAllEdits(self):
        result = list()
        for line in self.listCurrentKey:
            if ("edit" in line) and (line.count(' ') == 5):
                result.append(line.replace("edit ", "").replace(" ", ""))
        return result
