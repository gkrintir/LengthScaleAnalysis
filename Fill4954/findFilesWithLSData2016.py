import ROOT as r


def pruneTrees(filename):
    file= r.TFile.Open(filename)

    import sys
    #whichZeroBias = filename[81:90]
    whichZeroBias = filename[72:81]
    print whichZeroBias
    if 'ZeroBias' not in whichZeroBias:
        print "Problem with form of filename, assumed to be of a form such that filename[85:93] == ZeroBias, please check"
        sys.exit(1)

    namePrunedNtupleFile = whichZeroBias +"_"+ filename.split('/')[-1]

    oldtree = file.Get("lumi/tree")

    from array import array
# event is of type unsigned int
    event = array('i', [0])
# don't have pointers in python, hence need to use arrays
# where we need pointers we create an object of type array of desired types
# with only one entry (hence "[0]") and pass that

# good documenation here: http://www.ppe.gla.ac.uk/~abuzatu/SUPAROO/PyROOT/Helper/HelperPyRoot.py 
    oldtree.SetBranchAddress("event",event)
    oldtree.SetBranchStatus("*",0);
    oldtree.SetBranchStatus("run",1);
    oldtree.SetBranchStatus("bunchCrossing",1)
    oldtree.SetBranchStatus("LS",1)
    oldtree.SetBranchStatus("timeStamp_begin",1)
    oldtree.SetBranchStatus("timeStamp_end",1)
    oldtree.SetBranchStatus("event",1)
    oldtree.SetBranchStatus("nVtx",1)
    oldtree.SetBranchStatus("vtx_x",1)
    oldtree.SetBranchStatus("vtx_y",1)
    oldtree.SetBranchStatus("vtx_z",1)
    oldtree.SetBranchStatus("vtx_xError",1)
    oldtree.SetBranchStatus("vtx_yError",1)
    oldtree.SetBranchStatus("vtx_isGood",1)
    oldtree.SetBranchStatus("vtx_isValid",1)
    oldtree.SetBranchStatus("vtx_isFake",1)
    oldtree.SetBranchStatus("vtx_nTrk",1)


#Create a new file + a clone of old tree header. Do not copy events
    newfile = r.TFile(namePrunedNtupleFile,"recreate")
    newtree = oldtree.CloneTree(0);

    newtree.GetBranch("event")
    newtree.GetBranch("run")
    newtree.GetBranch("LS")
    newtree.GetBranch("bunchCrossing")
    newtree.GetBranch("timeStamp_begin")
    newtree.GetBranch("timeStamp_end")
    newtree.GetBranch("nVtx")
    newtree.GetBranch("vtx_x")
    newtree.GetBranch("vtx_y")
    newtree.GetBranch("vtx_z")
    newtree.GetBranch("vtx_xError")
    newtree.GetBranch("vtx_yError")
    newtree.GetBranch("vtx_isGood")
    newtree.GetBranch("vtx_isValid")
    newtree.GetBranch("vtx_isFake")
    newtree.GetBranch("vtx_nTrk")

    newtree.CopyEntries(oldtree);

    newtree.Write()
    newfile.Close()

    return




if __name__ == '__main__':

# Info from Chris: run, lumisections for length scale scans

#Scan ranges (run, LSs):
#X1  (254991, 285-360)
#Y (254991, 260-428)
#X2 (254992, 200-257)

    LSscan = ["X1","Y1"]
    LSrun = {"X1": 274100, "Y1": 274100}
    LSLumSecRange = {"X1": [610, 715], "Y1": [716, 850]}

    #LSscan = ["Y1"]
    #LSrun = {"Y1": 274100}
    #LSLumSecRange = {"Y1": [700, 850]}

    prefix = "root://eoscms//eos/cms"

    dirListEOS = [ \
        "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias1/PCC_Run2016B-17Jan2017-v1_ZeroBias1/170130_084827/0000",
	"/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias2/PCC_Run2016B-17Jan2017-v1_ZeroBias2/170130_084841/0000",
	"/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias3/PCC_Run2016B-17Jan2017-v1_ZeroBias3/170130_084855/0000",
	"/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias4/PCC_Run2016B-17Jan2017-v1_ZeroBias4/170130_084911/0000",
	"/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias6/PCC_Run2016B-17Jan2017-v1_ZeroBias6/170130_084929/0000",
	"/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias8/PCC_Run2016B-17Jan2017-v1_ZeroBias8/170130_084943/0000"]


    #dirListEOS = [ \
    #   "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias1/PCC_MayScans_AlwaysTrue1/170102_172208/0000/"]#, "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias2/PCC_MayScans_AlwaysTrue2/170102_172222/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias3/PCC_MayScans_AlwaysTrue3/170102_172235/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias4/PCC_MayScans_AlwaysTrue4/170102_172248/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias5/PCC_MayScans_AlwaysTrue5/170102_172303/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias6/PCC_MayScans_AlwaysTrue6/170102_172320/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias7/PCC_MayScans_AlwaysTrue7/170102_172333/0000", "/store/group/comm_luminosity/PCC/VdM/May2016Scans/ZeroBias8/PCC_MayScans_AlwaysTrue8/170102_172349/0000"]    

#    dirListEOS = [ \
#        
#        "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias1/PCC_VdM_ZeroBias1_273591_ProMay212016_Event_AlwaysTrue/160524_190706/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias2/PCC_VdM_ZeroBias2_273591_ProMay212016_Event_AlwaysTrue/160524_190731/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias3/PCC_VdM_ZeroBias3_273591_ProMay212016_Event_AlwaysTrue/160524_190756/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias4/PCC_VdM_ZeroBias4_273591_ProMay212016_Event_AlwaysTrue/160524_190825/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias5/PCC_VdM_ZeroBias5_273591_ProMay212016_Event_AlwaysTrue/160524_190850/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias7/PCC_VdM_ZeroBias7_273591_ProMay212016_Event_AlwaysTrue/160524_190916/0000", \
#            "/store/group/comm_luminosity/PCC/VdM/May182016_273591/ZeroBias8/PCC_VdM_ZeroBias8_273591_ProMay212016_Event_AlwaysTrue/160524_190945/0000"]
    

    filesForScan = {"X1":[],"Y1":[]}
    fileswithLSinfo = []

# subprocess exists only from python 2.7 onwards, so need to do cmsenv under a CMSSW release before runnign this script
    import subprocess

    for entry in dirListEOS:

        print ">>>> Now at dir ", entry
        filenames=[]
        fileinfos=subprocess.check_output(["cmsLs", entry])
        fileinfos=fileinfos.split("\n")

        for fileinfo in fileinfos:
            info=fileinfo.split()
            if len(info)!=1:
                continue
            filename=info[0]
            if filename.find(".root") != -1:
                #filenames.append("file:/afs/cern.ch/work/k/krose/vdm/tempeos/cms"+entry+"/"+filename)
		filenames.append("root://eoscms//eos/cms"+entry+"/"+filename)

        print filenames
        for filename in filenames:
            tfile=r.TFile.Open(filename)
            ttree = tfile.Get("lumi/tree")
            searchCond = ""
            for scanName in LSscan:
                searchCond = "run==" + str(LSrun[scanName]) + \
                    "&&LS>=" + str(LSLumSecRange[scanName][0]) + \
                    "&&LS<=" + str(LSLumSecRange[scanName][1])

                found = 0
                try:
                    found = ttree.GetEntries(searchCond)
                except:
                    print "Failed to GetEntries for",filename
                else:
                    if found:
                        fileswithLSinfo.append(filename)
                        filesForScan[scanName].append(filename)
                        break

    import pickle
    with open('./filesForScan_Y1_4954.pkl', 'wb') as f:
        pickle.dump(filesForScan, f)


    print fileswithLSinfo

    for scanName in LSscan:
        for filename in fileswithLSinfo:
            print "<<>><<>> Going through file with LS info ", filename
            pruneTrees(filename)

        
