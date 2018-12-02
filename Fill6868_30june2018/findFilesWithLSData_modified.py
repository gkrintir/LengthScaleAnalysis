import ROOT as r



def pruneTrees(filename):
    file= r.TFile.Open(filename)
    print 'filename :', filename
    import sys
    whichZeroBias = filename[93:105] #hard-coded
    if 'ZeroBias' not in whichZeroBias:
        print "Problem with form of filename, assumed to be of a form such that filename[93:105] == ZeroBias, please check"
        sys.exit(1)

    namePrunedNtupleFile = whichZeroBias +"_"+ filename.split('/')[-1]

    #####oldtree = file.Get("lumi/tree")
    oldtree = file.Get("pccminitree")

    from array import array

    event = array('i', [0])

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

    LSscan =["B1Y1","B1Y2","B1Y3","B1Y4","B1Y5","B1X1","B1X2","B1X3","B1X4","B1X5","B2Y1","B2Y2","B2Y3","B2Y4","B2Y5","B2X1","B2X2","B2X3","B2X4","B2X5"]
    LSrun = {"B1Y1": 319019, "B1Y2": 319019, "B1Y3": 319019, "B1Y4": 319019, "B1Y5": 319019, "B1X1": 319019, "B1X2": 319019, "B1X3": 319019, "B1X4": 319019, "B1X5": 319019, "B2Y1": 319019, "B2Y2": 319019, "B2Y3": 319019, "B2Y4": 319019, "B2Y5": 319019, "B2X1": 319019, "B2X2": 319019, "B2X3": 319019, "B2X4": 319019, "B2X5": 319019}
    LSLumSecRange = {"B1Y1": [1530417492, 1530417677], "B1Y2": [1530417706, 1530417893], "B1Y3": [1530417920, 1530418107], "B1Y4": [1530418135, 1530418321], "B1Y5": [1530418349, 1530418534],
                     "B1X1": [1530418959, 1530419147], "B1X2": [1530419175, 1530419364], "B1X3": [1530419392, 1530419580], "B1X4": [1530419606, 1530419795], "B1X5": [1530419822, 1530420011],
                     "B2Y1": [1530420649, 1530420840], "B2Y2": [1530420869, 1530421060], "B2Y3": [1530421089, 1530421279], "B2Y4": [1530421308, 1530421499], "B2Y5": [1530421526, 1530421717],
                     "B2X1": [1530422217, 1530422402], "B2X2": [1530422428, 1530422612], "B2X3": [1530422639, 1530422823], "B2X4": [1530422849, 1530423033], "B2X5": [1530423060, 1530423243],
                     }

    prefix = "root://eoscms//eos/cms"
    dirListEOS = [ \
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias1/crab_CMSSW_10_1_7_ZeroBias1_splitPerBXTrue/180817_121608/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias2/crab_CMSSW_10_1_7_ZeroBias2_splitPerBXTrue/180817_121630/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias3/crab_CMSSW_10_1_7_ZeroBias3_splitPerBXTrue/180817_121652/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias4/crab_CMSSW_10_1_7_ZeroBias4_splitPerBXTrue/180817_121713/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias5/crab_CMSSW_10_1_7_ZeroBias5_splitPerBXTrue/180914_182538/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias6/crab_CMSSW_10_1_7_ZeroBias6_splitPerBXTrue/180818_163932/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias7/crab_CMSSW_10_1_7_ZeroBias7_splitPerBXTrue/180817_121826/0000/minituples_supersep/",
        "/eos/cms/store/group/phys_top/gkrintir/ForLumiComputation/2018/NormalFills/6847_And_6854_And_6868/ZeroBias8/crab_CMSSW_10_1_7_ZeroBias8_splitPerBXTrue/180817_121848/0000/minituples_supersep/"
        ]
    filesForScan = {"B1Y1":[],"B1Y2":[],"B1Y3":[], "B1Y4":[], "B1Y5":[], "B1X1":[],"B1X2":[],"B1X3":[], "B1X4":[], "B1X5":[],"B2Y1":[],"B2Y2":[],"B2Y3":[], "B2Y4":[], "B2Y5":[], "B2X1":[],"B2X2":[],"B2X3":[], "B2X4":[], "B2X5":[]}
    fileswithLSinfo = []

# subprocess exists only from python 2.7 onwards, so need to do cmsenv under a CMSSW release before running this script
    import subprocess

    for entry in dirListEOS:

        print ">>>> Now at dir ", entry
        filenames=[]
        fileinfos=subprocess.check_output(["ls", entry])
        print fileinfos
        fileinfos=fileinfos.split("\n")

        for fileinfo in fileinfos:
            info=fileinfo.split()
            if len(info)!=1:
                continue
            filename=info[0]
            if filename.find(".root") != -1:
                filenames.append("root://eoscms/"+entry+"/"+filename)

        print filenames
        for filename in filenames:
            tfile=r.TFile.Open(filename)
            ####ttree = tfile.Get("lumi/tree")
            ttree = tfile.Get("pccminitree")
            searchCond = ""
            for scanName in LSscan:
                searchCond = "run==" + str(LSrun[scanName]) + \
                    "&&timeStamp_begin>=" + str(LSLumSecRange[scanName][0]) + \
                    "&&timeStamp_end<=" + str(LSLumSecRange[scanName][1])
                print searchCond
                found = 0
                try:
                    found = ttree.GetEntries(searchCond)
                except:
                    print "Failed to GetEntries for",filename
                else:
                    if found:
                        fileswithLSinfo.append(filename)
                        filesForScan[scanName].append(filename)
                        #if '274' in searchCond:
                        print 'found 274 re~~~~~~~~~~~', filename, scanName, filesForScan[scanName]
                        break

    import pickle
    with open('./filesForScan.pkl', 'wb') as f:
        pickle.dump(filesForScan, f)


    print fileswithLSinfo

