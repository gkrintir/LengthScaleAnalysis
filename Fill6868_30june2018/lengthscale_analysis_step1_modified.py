
import ROOT as r
import sys
import os
import pickle

def generateTimeWindows(whichScan):
### the time stamps can be accessed from    
### https://github.com/gkrintir/VdMFramework-1/blob/atlas_lsc_2018/Fill6868_Jul012018_MiniScans/cond/Scan_6868.csv#L17-#L97
    if whichScan == "B1Y1":
        begin = [
            1530417492,         # -1sigma [start]
            1530417562,         # 0sigma/head-on [start]
            1530417633          # +1sigma [start]
            ]
        end = [
            1530417537,         # -1sigma [end]
            1530417607,         # 0sigma/head-on [end]
            1530417677          # +1sigma [end]
            ]
    if whichScan == "B1Y2":
        begin = [
            1530417706,
            1530417778,
            1530417847
            ]
        end = [
            1530417751,
            1530417821,
            1530417893
            ]
    if whichScan == "B1Y3":
        begin = [
            1530417920,
            1530417992,
            1530418062
            ]
        end = [
            1530417965,
            1530418035,
            1530418107
            ]
    if whichScan == "B1Y4":
        begin = [
            1530418135,
            1530418204,
            1530418276
            ]
        end = [
            1530418180,
            1530418250,
            1530418321
            ]
    if whichScan == "B1Y5":
        begin = [
            1530418349,
            1530418419,
            1530418490
            ]
        end = [
            1530418394,
            1530418464,
            1530418534
            ]

    if whichScan == "B1X1":
        begin = [
            1530418959,
            1530419030,
            1530419103
            ]
        end = [
            1530419004,
            1530419076,
            1530419147
            ]
    if whichScan == "B1X2":
        begin = [
            1530419175,
            1530419248,
            1530419319
            ]
        end = [
            1530419220,
            1530419291,
            1530419364
            ]
    if whichScan == "B1X3":
        begin = [
            1530419392,
            1530419463,
            1530419535
            ]
        end = [
            1530419436,
            1530419507,
            1530419580
            ]
    if whichScan == "B1X4":
        begin = [
            1530419606,
            1530419677,
            1530419750
            ]
        end = [
            1530419651,
            1530419723,
            1530419795
            ]
    if whichScan == "B1X5":
        begin = [
            1530419822,
            1530419894,
            1530419967
            ]
        end = [
            1530419867,
            1530419938,
            1530420011
            ]

    if whichScan == "B2Y1":
        begin = [
            1530420649,
            1530420723,
            1530420796
            ]
        end = [
            1530420694,
            1530420767,
            1530420840
            ]
    if whichScan == "B2Y2":
        begin = [
            1530420869,
            1530420942,
            1530421016
            ]
        end = [
            1530420914,
            1530420987,
            1530421060
            ]
    if whichScan == "B2Y3":
        begin = [
            1530421089,
            1530421162,
            1530421235
            ]
        end = [
            1530421133,
            1530421206,
            1530421279
            ]
    if whichScan == "B2Y4":
        begin = [
            1530421308,
            1530421381,
            1530421453
            ]
        end = [
            1530421353,
            1530421426,
            1530421499
            ]
    if whichScan == "B2Y5":
        begin = [
            1530421526,
            1530421599,
            1530421672
            ]
        end = [
            1530421571,
            1530421644,
            1530421717
            ]

    if whichScan == "B2X1":
        begin = [
            1530422217,
            1530422287,
            1530422357
            ]
        end = [
            1530422261,
            1530422332,
            1530422402
            ]
    if whichScan == "B2X2":
        begin = [
            1530422428,
            1530422498,
            1530422568
            ]
        end = [
            1530422473,
            1530422543,
            1530422612
            ]
    if whichScan == "B2X3":
        begin = [
            1530422639,
            1530422708,
            1530422778
            ]
        end = [
            1530422683,
            1530422753,
            1530422823
            ]
    if whichScan == "B2X4":
        begin = [
            1530422849,
            1530422919,
            1530422988
            ]
        end = [
            1530422894,
            1530422963,
            1530423033
            ]
    if whichScan == "B2X5":
        begin = [
            1530423060,
            1530423129,
            1530423199
            ]
        end = [
            1530423104,
            1530423174,
            1530423243
            ]  


    return begin, end


def generateOffsetPositions(whichScan):

    if "B1" in whichScan or "B2" in whichScan:

        nomPos = [ 123.022, 0., -123.022]


    return nomPos



def makeCalibPlot(whichScan,rootOutFile,pdfOutFile,headon_offset):

# previously it was hardcoded, change accordingly for a X scan to "vtx_x", now it'll pick up according to scan.

    if 'X' in whichScan:
        whichVtx = "vtx_x" 

    if 'Y' in whichScan:
        whichVtx = "vtx_y"


    print "Now for scan ", whichScan, " and vtx coordinate ", whichVtx

    filelist = os.listdir("./")

    ##chain = r.TChain("lumi/tree")
    chain = r.TChain("pccminitree")

    with open('./filesForScan.pkl', 'rb') as f:
        filelist= pickle.load(f)


    for name in filelist[whichScan]:
        localName = name.split('/')[-1]
        posZeroBias = name.find('ZeroBias')
        print name
        if not posZeroBias:
            print "Problem with form of filename, assumed to be of a form such that filename[pos, pos+8] == ZeroBias, please check"
            sys.exit(1)
        whichZeroBias = name[posZeroBias: posZeroBias+9]
        localName = whichZeroBias + '_' + localName
        if localName.find(".root"):
            chain.Add(name)

    numFiles = chain.GetListOfFiles().GetEntries()

    print "Chain contains " + str(numFiles) + " files"
    print "Chain contains events", chain.GetEntries()

    beginTS, endTS =  generateTimeWindows(whichScan)

    nomOff = generateOffsetPositions(whichScan)
    
    rfile = r.TFile(rootOutFile,"recreate")

    canvas = r.TCanvas()
#    r.gStyle.SetPalette(1)
    r.gStyle.SetOptStat(1)
    r.gStyle.SetOptFit(1)
    if whichVtx == "vtx_y":
        r.gStyle.SetStatX(0.95)
        r.gStyle.SetStatY(0.5)
    if whichVtx == "vtx_x":
        r.gStyle.SetStatX(0.5)
        r.gStyle.SetStatY(0.55)

    hist = r.TH1F("hist",whichScan + " scan, " + whichVtx, 150, -0.15, 0.15) # hardcoded


    hList = [r.TH1F() for entry in beginTS]
    histoList = [r.TH1F() for entry in beginTS]
    avVtxPos = [0.0 for entry in beginTS]
    errAvVtxPos = [0.0 for entry in beginTS]

    vtxVsOff=r.TGraphErrors()
    vtxVsOff.SetTitle("LS scan " + whichScan + ": Mean " + whichVtx + " position in microns vs nomimal separation in microns")
    
    
    for index, value in enumerate(beginTS):

        hList[index] = hist.Clone()
        hList[index].SetName("hist"+str(index))

        
        stringCond = "timeStamp_begin >= " + str(beginTS[index]) + " && timeStamp_begin <= " + str(endTS[index]) +" && vtx_isGood"
        print stringCond
        chain.Draw(whichVtx + " >>hist"+str(index), stringCond)

        histoList[index]= r.gDirectory.Get("hist"+str(index))
        histoList[index].GetXaxis().SetTitle(whichVtx + " [mm]")
        histoList[index].GetYaxis().SetTitle("Offset in [#mum]")
        histoList[index].SetTitle("%i" %index)
        if histoList[index].GetEntries()==0:
            continue
        
        histoList[index].Fit("gaus")
        fit = histoList[index].GetFunction("gaus")
        avVtxPos[index]=fit.GetParameter(1)
        errAvVtxPos[index] = fit.GetParError(1)                
        histoList[index].Draw()
        histoList[index].Write()
        canvas.SaveAs(pdfOutFile+"(")

       
        vtxVsOff.SetPoint(index, nomOff[index],10000*avVtxPos[index])
        vtxVsOff.SetPointError(index, 0. ,10000*errAvVtxPos[index])
       
    canvas.Divide(1,2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0,0.3,1.0,1.0)

    vtxVsOff.SetMarkerStyle(8)
    vtxVsOff.SetMarkerSize(0.5)
    vtxVsOff.GetXaxis().SetTitle("nominal offset in microns")
    vtxVsOff.GetYaxis().SetTitle("Measured " + whichVtx + "  in microns")
    vtxVsOff.Draw("AP")
    vtxVsOff.Write()
    vtxVsOff.Fit("pol1")
    fitpol1=vtxVsOff.GetFunction("pol1")
    x=r.Double()
    y=r.Double()
    x1=r.Double()
    y1=r.Double()
    canvas.cd(2)
    canvas.cd(2).SetPad(0,0,1.0,0.3)
    pulls=r.TGraphErrors()
  

    for i in range(0,3):
	vtxVsOff.GetPoint(i,x,y)
	yError=vtxVsOff.GetErrorY(i)
        yFit=fitpol1.Eval(headon_offset)
    	pulls.SetPoint(i,x,(y-yFit))
	pulls.SetPointError(i,0,yError)
    
    
    
    
    pulls.SetMarkerStyle(8)
    pulls.SetMarkerSize(1.0)
    pulls.GetYaxis().SetTitle("Residuals [#mum]")
    pulls.GetYaxis().SetLabelSize(0.07)
    pulls.GetYaxis().SetTitleSize(0.07)
    pulls.GetYaxis().SetTitleOffset(0.5)
    pulls.SetTitle("")
    
    pulls.Draw("PA")
    pulls.Write()
    canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs("calib_"+whichScan+".root")

    canvas.cd(1)

   
    canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs(pdfOutFile+"]")

    #fitpol1.Write()
    rfile.Write()
    rfile.Close()
    
    


if __name__ == '__main__':

    string="nominalLHC_constrWindow_5points"
   
### values taken from http://nsahoo.web.cern.ch/nsahoo/LumiPOG/ATLAS_style_LSC/2018/FITS/SG_FittedGraphs_w_OrbitDrift.pdf    
## scan 1-5
    makeCalibPlot("B1Y1", "LScalib_B1Y1_v1.root", "plotsLScalib_B1Y1_"+string+"_p1.pdf", 0.00005318)
    makeCalibPlot("B1Y2", "LScalib_B1Y2_v1.root", "plotsLScalib_B1Y2_"+string+"_p1.pdf", 0.0008831)
    makeCalibPlot("B1Y3", "LScalib_B1Y3_v1.root", "plotsLScalib_B1Y3_"+string+"_p1.pdf", 0.001654) 
    makeCalibPlot("B1Y4", "LScalib_B1Y4_v1.root", "plotsLScalib_B1Y4_"+string+"_p1.pdf", 0.003088)
    makeCalibPlot("B1Y5", "LScalib_B1Y5_v1.root", "plotsLScalib_B1Y5_"+string+"_p1.pdf", 0.004081)
## scan 6-10
    makeCalibPlot("B1X1", "LScalib_B1X1_v1.root", "plotsLScalib_B1X1_"+string+"_p1.pdf", 0.002804)
    makeCalibPlot("B1X2", "LScalib_B1X2_v1.root", "plotsLScalib_B1X2_"+string+"_p1.pdf", 0.002207)
    makeCalibPlot("B1X3", "LScalib_B1X3_v1.root", "plotsLScalib_B1X3_"+string+"_p1.pdf", 0.003411)
    makeCalibPlot("B1X4", "LScalib_B1X4_v1.root", "plotsLScalib_B1X4_"+string+"_p1.pdf", 0.002429)
    makeCalibPlot("B1X5", "LScalib_B1X5_v1.root", "plotsLScalib_B1X5_"+string+"_p1.pdf", 0.002005)
## scan 11-15
    makeCalibPlot("B2Y1", "LScalib_B2Y1_v1.root", "plotsLScalib_B2Y1_"+string+"_p1.pdf", -0.003714)
    makeCalibPlot("B2Y2", "LScalib_B2Y2_v1.root", "plotsLScalib_B2Y2_"+string+"_p1.pdf", -0.0009348)
    makeCalibPlot("B2Y3", "LScalib_B2Y3_v1.root", "plotsLScalib_B2Y3_"+string+"_p1.pdf", -0.0007846)  
    makeCalibPlot("B2Y4", "LScalib_B2Y4_v1.root", "plotsLScalib_B2Y4_"+string+"_p1.pdf", 0.001245)
    makeCalibPlot("B2Y5", "LScalib_B2Y5_v1.root", "plotsLScalib_B2Y5_"+string+"_p1.pdf", 0.003632)
## scan 16-20
    makeCalibPlot("B2X1", "LScalib_B2X1_v1.root", "plotsLScalib_B2X1_"+string+"_p1.pdf", -0.0005713)
    makeCalibPlot("B2X2", "LScalib_B2X2_v1.root", "plotsLScalib_B2X2_"+string+"_p1.pdf", -0.001221)
    makeCalibPlot("B2X3", "LScalib_B2X3_v1.root", "plotsLScalib_B2X3_"+string+"_p1.pdf", -0.00206) 
    makeCalibPlot("B2X4", "LScalib_B2X4_v1.root", "plotsLScalib_B2X4_"+string+"_p1.pdf", -0.002739)
    makeCalibPlot("B2X5", "LScalib_B2X5_v1.root", "plotsLScalib_B2X5_"+string+"_p1.pdf", -0.003215)



'''
COMMENTS (30Nov):
1) B1X2, B1X3, B2X1 --> no files found
2) B2Y5, B1X5, B2X2, B2X5 --> matrix not definite positive

COMMENTS (Dec 7):
+++ all these issues are fixed now. 

'''
