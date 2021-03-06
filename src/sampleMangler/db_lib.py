"""
Modified version of John Skinner's db_lib.py:
  - rewriting to switch from using pickle files to sampleManager API
    (using dataapi for now)

  - also did some pep8/pylint/flake8 cleanup
"""

import pickle
import time

import sampleManager.dataapi.commands as dataapi


owner_name = 0  # need to work with john on this :(


#def _createContainer(container_name, type_name, capacity):
def _createContainer(owner_name, container_name, container_type_name):
    """
    Create a new container object:

    
    """

    # generate ids in the app for now, but
    # need api to have an autogen id default

# johns code expects:
#    containerObj = {"container_id": int(time.time()),
#                    "containerName": container_name,
#                    "type_name": type_name,
#                    "item_list": [None] * capacity}
    # The item list is a list of id's, whether they be other
    # containers or samples. This is becasue samples and pucks can
    # move.

    # containerFile = open("container.db", "a+")
    # pickle.dump(containerObj, containerFile)
    # containerFile.close()


# api should need:
#    containerObj = {"container_id": int(time.time()),
#                    "container_name": container_name,
#                    "type_name": type_name,
#                    "item_list": [None] * capacity}

# dataapi needs:
    containerObj = {"owner_name": owner_name,
                    "container_name": container_name,
                    "container_type_name": container_type_name,
                    "container_props_dict": {}}

    dataapi.save_container(**containerObj)



def _createSample(sampleName):
    """
    """

# johns code expects:
#    sampleObj = {"sample_id": int(time.time()), "sampleName": sampleName,
#                 "requestList": []}
#
#    sampleFile = open("sample.db", "a+")
#    pickle.dump(sampleObj, sampleFile)
#    sampleFile.close()
#    return sampleObj["sample_id"]


def getSampleByID(sample_id):
    """
    """

    pickleFile = open("sample.db", "a+")
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["sample_id"] == sample_id):
                return retQ
    except EOFError:
        pickleFile.close()
    return None


def getSampleIDbyName(sample_name):
    """
    """

    pickleFile = open("sample.db", "a+")
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["sampleName"] == sample_name):
                return retQ["sample_id"]
    except EOFError:
        pickleFile.close()
    return -99


def getSampleNamebyID(sample_id):
    """
    """

    pickleFile = open("sample.db", "a+")
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["sample_id"] == sample_id):
                return retQ["sampleName"]
    except EOFError:
        pickleFile.close()
    return -99


def getContainerIDbyName(container_name):
    """
    """

#    pickleFile = open("container.db", "a+")
#    try:
#        while (1):
#            retQ = pickle.load(pickleFile)
#            if (retQ["containerName"] == container_name):
#                return retQ["container_id"]
#    except EOFError:
#        pickleFile.close()
#    return -99

    query_dict = {'owner_id': owner_id, 'container_name': container_name}
    dataapi.find_container(query_dict)



def getContainerNameByID(container_id):
    """
    """

    pickleFile = open("container.db", "a+")
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["container_id"] == container_id):
                return retQ["containerName"]
    except EOFError:
        pickleFile.close()
    return ""


def addRequesttoSample(sample_id, request):
    """
    """

    pickleFile = open("sample.db", "a+")
    sampList = []

    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["sample_id"] == sample_id):
                retQ["requestList"].append(request)
            sampList.append(retQ)
    except EOFError:
        pickleFile.close()

    pickleFile = open("sample.db", "w+")

    for i in range(0, len(sampList)):
        pickle.dump(sampList[i], pickleFile)
    pickleFile.close()


def createDefaultRequest(sample_id):
    """
    """

    request = {"request_id": int(time.time()), "sample_id": sample_id,
               "sweep_start": 0.0, "sweep_end": 1.0, "img_width": .1,
               "exposure_time": .1, "priority": 0, "protocol": "standard",
               "directory": "/",
               "file_prefix": getSampleNamebyID(sample_id)+"_data",
               "file_number_start": 1, "wavelength": 1.1, "resolution": 3.0,
               "slit_height": 100.0, "slit_width": 150.0, "attenuation": 0,
               "pos_x": 0, "pos_y": 0, "pos_z": 0, "pos_type": 'A', "gridW": 0,
               "gridH": 0, "gridStep": 0}
    return request
####    addRequesttoSample(sample_id, request)


def insertIntoContainer(container_name, position, itemID):
    """
    """

    origQ = getContainers()
    found = 0
    for i in range(0, len(origQ)):
        if (origQ[i]["containerName"] == container_name):
            origQ[i]["item_list"][position] = itemID
            found = 1
            break
    if (found):
        containerFile = open("container.db", "w+")
        for i in range(0, len(origQ)):
            pickle.dump(origQ[i], containerFile)
        containerFile.close()
    else:
        print "bad container name"


def getContainers():
    """
    """

    ret_list = []
    containerFile = open("container.db", "a+")
    try:
        while (1):
            retQ = pickle.load(containerFile)
            ret_list.append(retQ)
    except EOFError:
        containerFile.close()
    return ret_list


def getContainersByType(type_name, group_name):
    """
    """

    ret_list = []
    containerFile = open("container.db", "a+")
    try:
        while (1):
            retQ = pickle.load(containerFile)
            if (retQ["type_name"] == type_name):
                ret_list.append(retQ)
    except EOFError:
        containerFile.close()
    return ret_list


def getAllPucks():
    """
    """

    return getContainersByType("puck", "")


def getPrimaryDewar():
    """
    """

    return getContainersByType("dewar", "")[0]


def getContainerByName(container_name):
    """
    """

    containerFile = open("container.db", "a+")
    try:
        while (1):
            retQ = pickle.load(containerFile)
            if (retQ["containerName"] == container_name):
                return retQ
    except EOFError:
        containerFile.close()
    return None


def getContainerByID(container_id):
    """
    """

    containerFile = open("container.db", "a+")
    try:
        while (1):
            retQ = pickle.load(containerFile)
            if (retQ["container_id"] == container_id):
                return retQ
    except EOFError:
        containerFile.close()
    return None


# stuff I forgot - alignment type?, what about some sort of sample lock?,

def insertCollectionRequest(sample_id, sweep_start, sweep_end, img_width,
        exposure_time, priority, protocol, directory, file_prefix,
        file_number_start, wavelength, resolution, slit_height, slit_width,
        attenuation, pos_x, pos_y, pos_z, pos_type, gridW, gridH, gridStep):
    """
    """

    colobj = {"request_id": int(time.time()), "sample_id": sample_id,
              "sweep_start": sweep_start, "sweep_end": sweep_end,

              "img_width": img_width, "exposure_time": exposure_time,
              "priority": priority, "protocol": protocol,

              "directory": directory, "file_prefix": file_prefix,
              "file_number_start": file_number_start,

              "wavelength": wavelength, "resolution": resolution,

              "slit_height": slit_height, "slit_width": slit_width,

              "attenuation": attenuation,

              "pos_x": pos_x, "pos_y": pos_y, "pos_z": pos_z,
              "pos_type": pos_type,

              "gridW": gridW, "gridH": gridH, "gridStep": gridStep}

######### need to insert this into the request List for the sample
    sampleObj = getSampleByID(sample_id)
    sampleObj["requestList"].append(colobj)
    updateSample(sampleObj)

#, vec_x_start, vec_y_start, vec_z_start, vec_x_end, vec_y_end,
#vec_z_end, vec_numframes, vec_fpp
# vec_fpp means frames per point,
# vec_numframes is the total. Not sure if this is the best way.

#pinpos, sweep_start, numimages, sweep_inc, exposure_time, protocol,
#file_prefix, file_number_start, wavelength, resolution, xtal_id,
#slit_height, slit_width, attenuation, priority


def getQueue():
    """
    """

    ret_list = []
    dewar = getContainerByName("primaryDewar")

    for i in range(0, len(dewar["item_list"])):  # these are pucks
        if (dewar["item_list"][i] is not None):
            puck_id = dewar["item_list"][i]
            if (puck_id is not None):
                puck = getContainerByID(puck_id)
                sampleList = puck["item_list"]
                for j in range(0, len(sampleList)):
                    if (sampleList[j] is not None):
                        print "sample ID = " + str(sampleList[j])
                        sampleReqList = getSampleByID(sampleList[j])["requestList"]
                        for k in range(0, len(sampleReqList)):
                            if (sampleReqList[k] is not None):
                                ret_list.append(sampleReqList[k])
    return ret_list


def getDewarPosfromSampleID(sample_id):
    """
    """

    dewar = getContainerByName("primaryDewar")

    for i in range(0, len(dewar["item_list"])):  # these are pucks
        if (dewar["item_list"][i] is not None):
            puck_id = dewar["item_list"][i]
            if (puck_id is not None):
                puck = getContainerByID(puck_id)
                sampleList = puck["item_list"]

                for j in range(0, len(sampleList)):
                    if (sampleList[j] is not None):
                        if (sampleList[j] == sample_id):
                            containerID = puck_id
                            position = j
                            return (containerID, position)


def getAbsoluteDewarPosfromSampleID(sample_id):
    """
    """

    dewar = getContainerByName("primaryDewar")
    dewarCapacity = len(dewar["item_list"])
    for i in range(0, dewarCapacity):  # these are pucks
        if (dewar["item_list"][i] is not None):
            puck_id = dewar["item_list"][i]
            if (puck_id is not None):
                puck = getContainerByID(puck_id)
                sampleList = puck["item_list"]
                puckCapacity = len(sampleList)  # puck
                for j in range(0, puckCapacity):
                    if (sampleList[j] is not None):
                        if (sampleList[j] == sample_id):
                            absPosition = (i*puckCapacity) + j
                            return absPosition


def popNextRequest():
    """
    """

    orderedRequests = getOrderedRequestList()
    if (orderedRequests[0]["priority"] > 0):
        return orderedRequests[0]
    else:
        return {}


def getRequest(reqID):  # qneed to get this from searching the dewar I guess
    """
    """

    reqList = getQueue()
    for i in range(0, len(reqList)):
        req = reqList[i]
        if (req["request_id"] == int(reqID)):
            return req
    return None


def getAllSamples():
    """
    """

    pickleFile = open("sample.db", "a+")
    retList = []
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            retList.append(retQ)
    except EOFError:
        pickleFile.close()
    return retList

# really need to generalize these update routines


def updateSample(sampleObj):
    """
    """

    sampleList = getAllSamples()
    for i in range(0, len(sampleList)):
        if (sampleList[i]["sample_id"] == sampleObj["sample_id"]):
            sampleList[i] = sampleObj
            break
    pickleFile = open("sample.db", "w+")
    for i in range(0, len(sampleList)):
        pickle.dump(sampleList[i], pickleFile)
    pickleFile.close()


def updateContainer(containerObj):
    """
    """

    containerList = getContainers()
    for i in range(0, len(containerList)):
        if (containerList[i]["container_id"] == containerObj["container_id"]):
            containerList[i] = containerObj
            break
    pickleFile = open("container.db", "w+")
    for i in range(0, len(containerList)):
        pickle.dump(containerList[i], pickleFile)
    pickleFile.close()


# this is really "update_sample" because the request is stored with the sample.

def updateRequest(reqObj):
    """
    """

    found = 0
    sample = getSampleByID(reqObj["sample_id"])
    reqList = sample["requestList"]
    for i in range(0, len(reqList)):
        if (reqList[i] is not None):
            if (reqObj["request_id"] == reqList[i]["request_id"]):
                sample["requestList"][i] = reqObj
                found = 1
                break
    if (found):
        updateSample(sample)
    else:
        addRequesttoSample(reqObj["sample_id"], reqObj)


def deleteRequest(reqObj):
    """
    """

    origQ = getQueue()
#    found = 0
    for i in range(0, len(origQ)):
        if (origQ[i]["request_id"] == reqObj["request_id"]):
            print "found the request to delete 1"
            s = getSampleByID(reqObj["sample_id"])
            for i in range(0, len(s["requestList"])):
                if (s["requestList"][i] is not None):
                    if (s["requestList"][i]["request_id"] == reqObj["request_id"]):
                        print "trying to delete request"
                        s["requestList"][i] = None
                        updateSample(s)


def deleteSample(samplObj):
    """
    """

    retList = []
    pickleFile = open("sample.db", "a+")
    try:
        while (1):
            retQ = pickle.load(pickleFile)
            if (retQ["sample_id"] != samplObj["sample_id"]):
                retList.append(retQ)
    except EOFError:
        pickleFile.close()
    pickleFile = open("sample.db", "w+")
    for i in range(0, len(retList)):
        pickle.dump(retList[i], pickleFile)
    pickleFile.close()


def removePuckFromDewar(dewarPos):
    """
    """

    dewar = getPrimaryDewar()
    dewar["item_list"][dewarPos] = None
    updateContainer(dewar)


def emptyLiveQueue():  # a convenience to say nothing is ready to be run
    """
    """

    q = getQueue()
    for i in range(0, len(q)):
        q[i]["priority"] = 0
        updateRequest(q[i])


def getSortedPriorityList():  # mayb an intermediate to return a list of all priorities.
    """
    """

    pList = []
    requestsList = getQueue()
    for i in range(0, len(requestsList)):
        if (requestsList[i]["priority"] not in pList):
            pList.append(requestsList[i]["priority"])
    return sorted(pList, reverse=True)


def getOrderedRequestList():
    """
    """

    orderedRequestsList = []
    priorityList = getSortedPriorityList()  # just sorts priorities
    requestsList = getQueue()  # this is everything in the dewar
#    dewarDict = getDewar()

    for i in range(0, len(priorityList)):
        for j in range(0, len(requestsList)):

            if (requestsList[j]["priority"] == priorityList[i]):
                orderedRequestsList.append(requestsList[j])

    return orderedRequestsList
