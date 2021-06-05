import pkgutil

folder = "user-agents/"
filetype = ".txt"
available = ["chrome", "firefox", "ie", "edge", "safari", "windows", "mac", "linux", "ios", "android", "bots"]
sets = {
        "all": ["chrome", "firefox", "ie", "edge", "safari", "ios", "android"],
        "mobile": ["ios", "android"],
        "desktop": ["windows", "mac", "linux"],
        }

def GetFileContents(f):
    # TODO: Add checks. Currently assumes files exist.
    return pkgutil.get_data(__name__, folder+f+filetype).decode("utf-8").splitlines()

def GetList(ua=["all"], limit=0):
    cList = []
    uList = []
    fList = []
    for type in ua:
        if type in available:
            uList.append(type)
        elif type in sets:
            uList.extend(sets[type])
        else:
            # Sends set "all" if the selection is invalid. Needs improving.
            uList.extend(sets["all"])
    for i in uList:
        if i not in cList:
            cList.append(i)
    for i in cList:
        fList.extend(GetFileContents(i))
    return fList