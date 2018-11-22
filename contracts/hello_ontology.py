from boa.interop.System.Runtime import Notify
from boa.interop.System.Storage import Put, Get, GetContext

def Main(operation, args):
    if operation == 'testNumList':
        if len(args) != 1:
            return False
        numList = args[0]
        return testNumList(numList)
    if operation == 'testNumListAndStr':
        Notify([args])
        if len(args) != 2:
            return False
        numList = args[0]
        msgStr = args[1]
        return testNumListAndStr(numList, msgStr)
    if operation == 'testStrListAndStr':
        if len(args) != 2:
            return False
        strList = args[0]
        msgStr = args[1]
        return testStrListAndStr(strList, msgStr)
    if operation == 'testByteArrayListAndStr':
        if len(args) !=2:
            return False
        msgList = args[0]
        msg = args[1]
        return testByteArrayListAndStr(msgList, msg)
    if operation == 'testStructList':
        Notify(args)
        structList = args[0]
        return testStructList(structList)
    if operation == 'testStructListAndStr':
        if len(args) !=2:
            return False
        structList = args[0]
        msgStr = args[1]
        return testStructListAndStr(structList,msgStr)
    if operation == 'testMap':
        if len(args) != 2:
            return False
        key = args[0]
        value = args[1]
        return testMap(key, value)
    if operation == 'testGetMap':
        if len(args) != 1:
            return False
        key = args[0]
        return testGetMap(key)
    return False

def hello(msg):
    return msg

def testHello(msgBool, msgInt, msgByteArray,msgStr,msgAddress):
    Notify(["testHello",msgBool, msgInt, msgByteArray,msgStr,msgAddress])
    resList = []
    resList.append(msgBool)
    resList.append(msgInt)
    resList.append(msgByteArray)
    resList.append(msgStr)
    resList.append(msgAddress)
    return resList

def testNumList(numList):
    Notify(["testNumList", numList])
    return numList

def testNumListAndStr(numList, msgStr):
    Notify(["testNumListAndStr",numList,msgStr])
    resList = []
    resList.append(numList)
    resList.append(msgStr)
    return resList

def testStrListAndStr(strList, msgStr):
    Notify(["testStrListAndStr", strList, msgStr])
    resList = []
    resList.append(strList)
    resList.append(msgStr)
    return resList

def testByteArrayListAndStr(bytearrayList, msgStr):
    Notify(["testByteArrayListAndStr", bytearrayList, msgStr])
    resList = []
    resList.append(bytearrayList)
    resList.append(msgStr)
    return resList

def testStructList(structList):
    Notify(["testStructList", structList])
    return structList
def testStructListAndStr(structList, msgStr):
    Notify(["testStructListAndStr", structList, msgStr])
    resList = []
    resList.append(structList)
    resList.append(msgStr)
    return resList

def testMap(key, value):
    map = {}
    map[key] = value
    mapInfo = Serialize(map)
    Put(GetContext(), 'map_key', mapInfo)
    return True
def testGetMap(key):
    mapInfo = Get(GetContext(), 'map_key')
    map = Deserialize(mapInfo)
    return map[key]
