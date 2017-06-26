import ROOT as r
import sys
import os
import pickle

def generateTimeWindows(whichScan):
    
    # X1
    # fill 4266 stable beams (SB) declared 24.08.2015 21:06:24 GMT
    stableBeamsDeclared = 1464347152

    if whichScan == "X1":

    # from Olena's plots of BPM beam positions, format: min from start of SB
        #beginMin = [307, 309, 311, 313, 315, 317, 320, 322, 324, 326]
        #beginSec = [30, 30, 30, 30, 30, 48, 0, 0, 0, 12]
        #endMin = [308, 310, 312, 314, 316, 319, 321, 323, 325, 328]
        #endSec = [36, 36, 36, 36, 48, 0, 0, 0, 24, 48]

#	beginMin = [0, 1, 3, 5, 7, 9, 10, 12, 14, 16]
#        beginSec = [5, 55, 40, 30, 15, 5, 50, 40, 25, 10]
#        endMin = [0, 2, 4, 6, 8, 9, 11, 13, 15, 17]
#        endSec = [55, 45, 35, 20, 5, 55, 40, 30, 20, 5]

#	begin=[671,676,681,685,690,694,699,704,708,713]
#	end=[671,676,681,685,690,694,699,704,708,713]
	begin=[671,676,681,685,690,694,699,704,708,713]
        end=[671,676,681,685,690,694,699,704,708,713]



    if whichScan == "Y1":

	#begin=[735,740,744,749,754,758,763,768,772,777]
	#end=[735,740,744,749,754,758,763,768,772,777]

	
	
	begin=[733,740,744,749,754,758,763,767,772,777]
        end=[733,740,744,749,754,758,763,767,772,777]

    # from Olena's plots of BPM beam positions, format: min from start of SB
        #beginMin = [333, 335, 337, 339, 341, 343, 345, 347, 349, 351, 353]
        #beginSec = [12 , 36 , 36 , 24 , 24 , 24 , 24 , 24 , 24 , 24 , 24]
        #endMin = [334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354]
        #endSec = [36 , 36 , 36 , 36 , 36 , 36 , 36 , 36 , 36 , 36 , 36]

#        beginMin = [24, 26,   28,  30, 32, 33, 35,  37,  39,  41]
#        beginSec = [45, 35,   25,  15, 0,  50, 40,  30,  20,  10]
#        endMin = [25, 27, 29, 31, 32, 34, 36, 38, 40, 42]
#        endSec = [40, 30, 15, 5,  55, 45, 35, 25, 10, 0 ]

   
	

    #begin = [stableBeamsDeclared + a*60 +b for a,b in zip(beginMin, beginSec)]
    #end = [stableBeamsDeclared + a*60 +b for a,b in zip(endMin, endSec)]

    return begin, end

def generateOffsetPositions(whichScan):

    # from Marco's write-up, in microns
    if whichScan == "X1":
        #posB1 = [204.2, 74.7, -54.8, -184.26, -315.4, -188.41, -58.1, 69.7, 199.2, 332]
        #posB2 = [79.7, -50.6, -183.4, -314.6, -180.9, -49.8, 83, 215, 346.1, 213.3]

    #Attention: exclude very first point, which, nominally, has B1 at -325 and B2 at -195, because Olena's BPM data are non-sensical for$

        posB1 = [-246, -148, -49, 49, 148, 246, 148, 49, -49, -148]
        posB2 = [-148, -49, 49, 148, 246, 148, 49, -49, -148, -246]

    if whichScan == "Y1":
        #posB1 = [-269.3, -176, -55.6, 65.6, 185.9, 308.8, 189.2, 68.9, -51.5, -172.6, -296.3]
        #posB2 = [-178.5, -58.9, 62.3, 181.8, 303, 181, 60.6, -59.8, -180.1, -299.6, -177.6]
        posB1 = [-246, -148, -49, 49, 148, 246, 148, 49, -49, -148]
        posB2 = [-148, -49, 49, 148, 246, 148, 49, -49, -148, -246]

    if whichScan == "X2":
#        posB1 = [317.9, 189.2, 61.4, -68.9, -196.7, -328.7, -200.9, -73, 57, 185.1, 318.7]
#        posB2 = [211.7, 80, -51.5, -184.3, -314.6, -181.8, -46.5, 83, 215, 345.3, 213.31]
        posB1 = [325, 195, 65, -65, -195, -325, -195, -65, 65, 195, 325]
        posB2 = [195, 65, -65, -195, -325, -195, -65, 65, 195, 325, 195]


    nomPos = [(a+b)/2. for a,b in zip(posB1, posB2)]

    print nomPos

    return nomPos

def generateOffsetPositionsDOROS(whichScan):


    if whichScan == "X1":
        posB1 = [4.00,   2.46,  0.90, -0.66, -2.22,  -3.80,    -2.27, -0.70, 0.84, 2.40 ]
        posB2 = [2.54,   0.96, -0.61, -2.21, -3.79,  -2.18,    -0.60,  1.00, 2.59, 4.17 ]

    if whichScan == "Y1":

        posB1 = [-3.57,    -2.12, -0.67, 0.79, 2.24,  3.72,    2.28,  0.83, -0.62, -2.08 , -3.57]
        posB2 = [-2.15,    -0.71,  0.75, 2.19, 3.65,  2.18,    0.73, -0.72, -2.17, -3.61 , -2.14]


    if whichScan == "X2":
        posB1 = [3.83,    2.28,  0.74, -0.83, -2.37,  -3.96,    -2.42, -0.88, 0.69, 2.23, 3.84 ]
        posB2 = [2.55,    0.97, -0.62, -2.22, -3.79,  -2.19,    -0.56,  1.00, 2.59, 4.16, 2.57 ]

# to translate into microns: multiply with 83 (single beam sigma)

    singleBeamSigma = 83.
    posB1 = [a*singleBeamSigma for a in posB1]
    posB2 = [a*singleBeamSigma for a in posB2]

    nomPos = [(a+b)/2. for a,b in zip(posB1, posB2)]

    print nomPos


    return nomPos



def makeCalibPlot(whichScan,rootOutFile,pdfOutFile):

    whichVtx = "vtx_x"

    if whichScan == "Y1":
        whichVtx = "vtx_y"

    print "Now for scan ", whichScan, " and vtx coordinate ", whichVtx

    #filelist = os.listdir("./lengthscale_Aug2015")
    filelist = os.listdir("./")

    chain = r.TChain("lumi/tree")

    with open('./filesForScan_Y1_4954.pkl', 'rb') as f:
        filelist= pickle.load(f)

#    print filelist

    for name in filelist[whichScan]:
 #       localName = name.split('/')[-1]
 #       posZeroBias = name.find('ZeroBias')
#        print name, posZeroBias
#        if not posZeroBias:
#            print "Problem with form of filename, assumed to be of a form such that filename[pos, pos+8] == ZeroBias, please check"
#            sys.exit(1)
#        whichZeroBias = name[posZeroBias: posZeroBias+9]
#        localName = whichZeroBias + '_' + localName
#        if localName.find(".root"):
	chain.Add(name)

    numFiles = chain.GetListOfFiles().GetEntries()

    print "Chain contains " + str(numFiles) + " files"
    print "Chain contains events", chain.GetEntries()

    beginTS, endTS =  generateTimeWindows(whichScan)
    print beginTS, endTS
#    print "DOROS"
#    nomOff = generateOffsetPositionsDOROS(whichScan)
#    print "fromLHC"
    nomOff = generateOffsetPositions(whichScan)
    
    rfile = r.TFile(rootOutFile,"recreate")

    canvas = r.TCanvas()
    canvas.Divide(1,2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0,0.3,1.0,1.0)
#    r.gStyle.SetPalette(1)
    r.gStyle.SetOptStat(1)
    r.gStyle.SetOptFit(1)
    r.gStyle.SetStatX(0.95)
    r.gStyle.SetStatY(0.5)

    hist = r.TH1F("hist",whichScan + " scan, " + whichVtx, 250, -0.1, 0.3)

    hList = [r.TH1F() for entry in beginTS]
    histoList = [r.TH1F() for entry in beginTS]
    avVtxPos = [0.0 for entry in beginTS]
    errAvVtxPos = [0.0 for entry in beginTS]

    vtxVsOffTo=r.TGraphErrors()
    vtxVsOffTo.SetTitle("")
    vtxVsOffFro=r.TGraphErrors()
    vtxVsOffFro.SetTitle("")

    for index, value in enumerate(beginTS):
        hList[index] = hist.Clone()
        hList[index].SetName("hist"+str(index))

        stringCond = "LS >= " + str(beginTS[index]) + " && LS <= " + str(endTS[index]) +" && vtx_isGood"
        chain.Draw(whichVtx + " >>hist"+str(index), stringCond)

        histoList[index]= r.gDirectory.Get("hist"+str(index))
        histoList[index].GetXaxis().SetTitle(whichVtx + " [mm]")
        histoList[index].GetYaxis().SetTitle("Offset in [ #mu m ]")
        histoList[index].Fit("gaus")
        fit = histoList[index].GetFunction("gaus")
	print "whichscan ", whichScan, "index " , index
	if (whichScan == "X1") or (whichScan == "X2" and index != 0) or (whichScan == "Y1"):
            avVtxPos[index]=fit.GetParameter(1)
            errAvVtxPos[index] = fit.GetParError(1)                
            histoList[index].Draw()
            histoList[index].Write()
        canvas.SaveAs(pdfOutFile+"(")

#        splitPoint = 5
#        beginIndex = 0
##        splitPoint = 4

#        if index <= splitPoint-1 and index >= beginIndex+1:
#            vtxVsOffTo.SetPoint(index-beginIndex-1, nomOff[index],10000*avVtxPos[index]) 
#            vtxVsOffTo.SetPointError(index-beginIndex-1, 0. ,10000*errAvVtxPos[index])
#        #if index > splitPoint+1 and index < len(beginTS):
#         #   vtxVsOffFro.SetPoint(index-splitPoint-2, nomOff[index],10000*avVtxPos[index]) 
#         #   vtxVsOffFro.SetPointError(index-splitPoint-2, 0. ,10000*errAvVtxPos[index]) 

#	if index > splitPoint and index < len(beginTS):
#            vtxVsOffFro.SetPoint(index-splitPoint-1, nomOff[index],10000*avVtxPos[index]) 
#            vtxVsOffFro.SetPointError(index-splitPoint-1, 0. ,10000*errAvVtxPos[index]) 



	splitPoint = 5
        #if whichScan == "X1":
	#	splitPoint = 4

        if index <= splitPoint-1:
            print "To"
            print index #index-(splitPoint+1)
            print whichScan
            print nomOff[index]
	    print 10000*avVtxPos[index]
            vtxVsOffTo.SetPoint(index, nomOff[index],10000*avVtxPos[index])
            vtxVsOffTo.SetPointError(index, 0. ,10000*errAvVtxPos[index])
        if index > splitPoint-1:
            print "Fro"
            print index-(splitPoint)
            print whichScan
            print nomOff[index]
	    print 10000*avVtxPos[index]
            vtxVsOffFro.SetPoint(index-(splitPoint), nomOff[index],10000*avVtxPos[index])
            vtxVsOffFro.SetPointError(index-(splitPoint), 0. ,10000*errAvVtxPos[index])

    canvas.cd(1)
    vtxVsOffTo.SetMarkerStyle(8)
    vtxVsOffTo.SetMarkerSize(0.5)
    vtxVsOffTo.GetXaxis().SetTitle("Nominal offset in microns")
    vtxVsOffTo.GetYaxis().SetTitle("Measured offset in microns")
    vtxVsOffTo.GetXaxis().SetTitle("Nominal offset [#mum]")
    vtxVsOffTo.GetYaxis().SetTitleSize(0.053)
    vtxVsOffTo.GetXaxis().SetTitleSize(0.053)
    vtxVsOffTo.GetYaxis().SetTitleOffset(0.9)
    vtxVsOffTo.GetXaxis().SetTitleOffset(0.9)
    if whichScan is "X1":
    	vtxVsOffTo.GetYaxis().SetTitle("x_{beamspot} [#mum]")
    if whichScan is "Y1":
	vtxVsOffTo.GetYaxis().SetTitle("y_{beamspot} [#mum]")
    vtxVsOffTo.Draw("AP")
    text1=r.TLatex(0.7,0.91,"2016  (13TeV)")
    text1.SetNDC()
    text1.SetTextFont(62)
    text1.SetTextSize(0.07)
    text12=r.TLatex(0.1,0.91,"CMS #bf{#scale[0.75]{#it{Preliminary}}}")
    text12.SetNDC()
    text12.SetTextSize(0.07)
    text12.SetTextFont(62)
    text1.Draw("same")
    text12.Draw("same")
    vtxVsOffTo.Write()
    vtxVsOffTo.Fit("pol1")
    fitpol1=vtxVsOffTo.GetFunction("pol1")
    x=r.Double()
    y=r.Double()
    canvas.cd(2)
    canvas.cd(2).SetPad(0,0,1.0,0.3)
    #canvas.cd(2).SetTicky(0.5)
    pullsTo=r.TGraphErrors()
    
  

    for i in range(0,5):
	vtxVsOffTo.GetPoint(i,x,y)
	yError=vtxVsOffTo.GetErrorY(i)
	yFit=fitpol1.Eval(x)
	print yFit
	print y
    	pullsTo.SetPoint(i,x,(y-yFit))
	pullsTo.SetPointError(i,0,yError)
    
    
    #canvas.SaveAs(pdfOutFile+"(")
    #canvasPullTo=r.TCanvas()
    
    pullsTo.SetMarkerStyle(8)
    pullsTo.SetMarkerSize(1.0)
    pullsTo.GetYaxis().SetTitle("Residuals [#mum]")
    pullsTo.GetYaxis().SetLabelSize(0.07)
    pullsTo.GetYaxis().SetTitleSize(0.07)
    pullsTo.GetYaxis().SetTitleOffset(0.5)
    pullsTo.SetTitle("")
    
    pullsTo.Draw("PA")
    pullsTo.Write()
    canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs("LSCTo"+whichVtx+whichScan+".root")
    #canvasPullTo.SaveAs("pulls"+whichVtx+".root")

    canvas.cd(1)
    vtxVsOffFro.SetMarkerStyle(8)
    vtxVsOffFro.SetMarkerSize(0.5)
    vtxVsOffFro.GetXaxis().SetTitle("Nominal offset in microns")
    vtxVsOffFro.GetYaxis().SetTitle("Measured offset in microns")
    vtxVsOffFro.GetXaxis().SetTitle("Nominal offset [#mum]")
    vtxVsOffFro.GetYaxis().SetTitleSize(0.053)
    vtxVsOffFro.GetXaxis().SetTitleSize(0.053)
    vtxVsOffFro.GetYaxis().SetTitleOffset(0.9)
    vtxVsOffFro.GetXaxis().SetTitleOffset(0.9)
    if whichScan is "X1":
    	vtxVsOffFro.GetYaxis().SetTitle("x_{beamspot} [#mum]")
    if whichScan is "Y1":
	vtxVsOffFro.GetYaxis().SetTitle("y_{beamspot} [#mum]")
    vtxVsOffFro.Fit("pol1")
    vtxVsOffFro.Draw("AP")
    text=r.TLatex(0.7,0.91,"2016  (13TeV)")
    text.SetNDC()
    text.SetTextFont(62)
    text.SetTextSize(0.07)
    text2=r.TLatex(0.1,0.91,"CMS #bf{#scale[0.75]{#it{Preliminary}}}")
    text2.SetNDC()
    text2.SetTextSize(0.07)
    text2.SetTextFont(62)
    text.Draw("same")
    text2.Draw("same")
    vtxVsOffFro.Write()

    fitpol2=vtxVsOffFro.GetFunction("pol1")
    x=r.Double()
    y=r.Double()
    canvas.cd(2)
    canvas.cd(2).SetPad(0,0,1.0,0.3)
    #canvas.cd(2).SetTicky(0.5)
    pullsFro=r.TGraphErrors()
    pullsFro.SetTitle("")  
    #pullsFro.GetYaxis().SetTitle("Residuals [#mu m]")  
    for i in range(0,5):
	vtxVsOffFro.GetPoint(i,x,y)
	yError=vtxVsOffFro.GetErrorY(i)
	yFit=fitpol2.Eval(x)
	print yFit
	print y
    	pullsFro.SetPoint(i,x,(y-yFit))
	pullsFro.SetPointError(i,0,yError)
    
    
    #canvas.SaveAs(pdfOutFile+"(")
    #canvasPullTo=r.TCanvas()
    
    pullsFro.SetMarkerStyle(8)
    pullsFro.SetMarkerSize(1.0)
    pullsFro.GetYaxis().SetTitle("Residuals [#mum]")
    pullsFro.GetYaxis().SetTitleSize(0.07)
    pullsFro.GetYaxis().SetLabelSize(0.07)
    pullsFro.GetYaxis().SetTitleOffset(0.5)

    pullsFro.SetTitle("")
    pullsFro.Draw("PA")
    pullsFro.Write()
   
    canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs(pdfOutFile+"]")
    canvas.SaveAs("LSCFro"+whichVtx+whichScan+".root")

    rfile.Write()
    rfile.Close()



if __name__ == '__main__':

    string="nominalLHC_constrWindow_4points"
    makeCalibPlot("X1", "LScalib_X1_v2.root", "plotsLScalib_X1_"+string+"_4954LS_ReReco_PAS.pdf")
    makeCalibPlot("Y1", "LScalib_Y1_v2.root", "plotsLScalib_Y1_"+string+"_4954LS_ReReco_PAS.pdf")
#    makeCalibPlot("X2", "LScalib_X2_v2.root", "plotsLScalib_X2_"+string+"_p1.pdf")




