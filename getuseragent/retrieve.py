import pkgutil
import logging

folder = "user-agents/"
filetype = ".txt"
available = ["chrome", "firefox", "ie", "edge", "safari", "windows", "mac", "linux", "ios", "android", "bots"]
sets = {
        "all": ["chrome", "firefox", "ie", "edge", "safari", "ios", "android"],
        "mobile": ["ios", "android"],
        "desktop": ["windows", "mac", "linux"],
        }

def GetFileContents(f, limit=0):
    """
    Gets the list of user agents from the file.
    
    Returns a list of strings.
    If the file does not exist, returns None. 
    """
    # TODO: Improve file checking code
    li = None
    try:
        packdata = pkgutil.get_data(__name__, folder+f+filetype)
        li = packdata.decode("utf-8").splitlines()
        if limit > 0:
            li = li[0:limit]
    except OSError as e:
        logging.error("User agents file does not exist, skipping: "+f+filetype)
    return li

def GetList(ua=["all"], limit=0):
    cList = []
    uList = []
    fList = [] # Final List
    for type in ua:
        if type in available:
            uList.append(type)
        elif type in sets:
            uList.extend(sets[type])
        else:
            # Sends set "all" if the selection is invalid. Needs improving.
            logging.warning("Selected user agents list doesn't exist, using default list")
            uList.extend(sets["all"])
    # Remove duplicate lists
    for i in uList:
        if i not in cList:
            cList.append(i)
    # Get user agents from file(s)
    for i in cList:
        toAdd = GetFileContents(i, limit)
        if toAdd:
            fList.extend(toAdd)
    return fList
