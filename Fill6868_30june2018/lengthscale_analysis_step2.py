
import ROOT as r
import sys
import os
import pickle

def generateOffsetPositions(whichScan):

    nomPos = [ -246, -123, 0, 123, 246 ]

    return nomPos

def makeCalibPlot(whichScan,rootOutFile,pdfOutFile):

    ###whichVtx = "vtx_y" #hardcoded, change accordingly for a X scan to "vtx_x"

    if 'X' in whichScan:
        whichVtx = "vtx_x"

    if 'Y' in whichScan:
        whichVtx = "vtx_y"

    nomOff = generateOffsetPositions(whichScan)
    
    rfile = r.TFile(rootOutFile,"recreate")

    canvas = r.TCanvas()

    mult = r.TMultiGraph()
    mult.SetTitle("; Nominal Position [#mum]; Measured Vertex Position [#mum]");

    vtxVsOff_B1=r.TGraphErrors()
    vtxVsOff_B1.SetTitle("LS scan " + whichScan + ": Mean " + whichVtx + " position in microns vs bump amplitude in microns")

    vtxVsOff_B2=r.TGraphErrors()
    vtxVsOff_B2.SetTitle("LS scan " + whichScan + " \"Fro\": Mean " + whichVtx + " position in microns vs nominal offset in microns")

    if whichVtx == "vtx_x":
        b1y  = [   1186,    1065,   941.5,   818.7,   695.8] # bump position of beam 1 in X                                          
        b1y1 = [0.03989, 0.04008, 0.04036, 0.03995, 0.04025] # bump error of beam 1  in X                                                          

        b2y  = [   1188,    1066,   944.1,   821.9,   699.5] # bump position of beam 2 in X                                        
        b2y1 = [0.04036, 0.04023, 0.04025, 0.04199, 0.0409] # bump error of beam 2  in X   

    if whichVtx == "vtx_y":
        b1y  = [ -841.4,  -720.1,  -597.1,  -473.8,  -349.8] # bump position of beam 1 in Y
        b1y1 = [0.03412, 0.03392, 0.03415, 0.03374, 0.03401] # bump error of beam 1  in Y
        
        b2y  = [ -841.4,  -718.8,  -596.7,  -472.8,  -350.3] # bump position of beam 2 in Y
        b2y1 = [0.03391, 0.03399, 0.03416, 0.03364, 0.03385] # bump error of beam 2  in Y


    for i in range(0,5):

        vtxVsOff_B1.SetPoint(i, nomOff[i],b1y[i])
        ####vtxVsOff_B1.SetPointError(i, 0, b1y1[i])   # the chi2/dof from fit doesn't make sense 
        vtxVsOff_B1.SetPointError(i, 0, b1y1[i]*10)
        
        vtxVsOff_B2.SetPoint(i, nomOff[i],b2y[i])  
        ####vtxVsOff_B2.SetPointError(i, 0, b2y1[i])   # the chi2/dof from fit doesn't make sense 
        vtxVsOff_B2.SetPointError(i, 0, b2y1[i]*10)


    pad1 = r.TPad('pad1', 'pad1', 0, 0., 1, 1)
    pad1.Draw()


    pad1.cd()
    r.gStyle.SetOptStat()#111)
    r.gStyle.SetOptFit()#111)


    vtxVsOff_B1.SetMarkerStyle(8)
    vtxVsOff_B1.GetXaxis().SetTitle("mpa")
    vtxVsOff_B1.SetMarkerSize(1.5)
    vtxVsOff_B1.SetMarkerStyle(21)
    vtxVsOff_B1.SetMarkerColor(2+2*0)
    vtxVsOff_B2.SetMarkerStyle(25)
    vtxVsOff_B2.SetMarkerColor(2+2*1)
    vtxVsOff_B2.SetMarkerSize(1.5)
    vtxVsOff_B1.GetXaxis().SetTitle("bump amplitude in microns")
    vtxVsOff_B1.GetYaxis().SetTitle("Measured " + whichVtx + "  in microns")
    mult.Add(vtxVsOff_B1)
    mult.Add(vtxVsOff_B2)

    mult.Draw("AP")
    vtxVsOff_B1.Write()
    vtxVsOff_B2.Write()
    #####vtxVsOff_B1_B2.Write()
    vtxVsOff_B1.Fit("pol1")
    pad1.Modified()
    pad1.Update()
    
    
    stats = vtxVsOff_B1.GetListOfFunctions().FindObject('stats')
    #stats.SetName("mystats")
    stats.SetBorderSize(0)
    stats.SetTextColor(2+2*0)    ### red color 
    stats.SetX1NDC(0.15+0.55*0)
    stats.SetX2NDC(0.45+0.55*0)
    if whichVtx == "vtx_x":
        stats.SetY1NDC(0.12)
        stats.SetY2NDC(0.28)
    if whichVtx == "vtx_y":
        stats.SetY1NDC(0.72)
        stats.SetY2NDC(0.88)

    pad1.Modified()
    pad1.Update()

    
    fitpol1=vtxVsOff_B1.GetFunction("pol1")
    fitpol1.SetLineColor(2+2*0)
    fitpol1.SetLineStyle(5)
    vtxVsOff_B2.Fit("pol1")
    fitpol2=vtxVsOff_B2.GetFunction("pol1")
    fitpol2.SetLineColor(2+2*1)
    fitpol2.SetLineWidth(1)

    pad1.Modified()
    pad1.Update()


    
    stats1 = vtxVsOff_B2.GetListOfFunctions().FindObject('stats')
    stats1.SetBorderSize(0)
    stats1.SetTextColor(2+2*1)   ### blue color
    stats1.SetX1NDC(0.1+0.5*1)
    stats1.SetX2NDC(0.40+0.5*1)
    if whichVtx == "vtx_x":
        stats1.SetY1NDC(0.72)
        stats1.SetY2NDC(0.88)
    if whichVtx == "vtx_y":
        stats1.SetY1NDC(0.12)
        stats1.SetY2NDC(0.28)

    stats1.GetListOfLines().ls()


    stats1.Draw("same")
    stats1.GetListOfLines().ls()
    pad1.Modified()
    pad1.Update()
        
      
    text2=r.TLatex(0.10,0.91,"CMS #bf{#scale[0.75]{#it{Preliminary}}}")
    text2.SetNDC()
    text2.SetTextSize(0.05)
    text2.SetTextFont(62)
    text=r.TLatex(0.90,0.91,"2018 (13 TeV)")
    text.SetNDC()
    #text.SetTextFont(62)
    text.SetTextSize(0.05)
    text.SetTextAlign(31)
    text2.Draw("same")
    text.Draw("same")
    pad1.Modified()
    pad1.Update()
   
    canvas.cd()

    canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs("calib_"+whichScan+".root")

    ####canvas.SaveAs(pdfOutFile+"(")
    canvas.SaveAs(pdfOutFile+"]")

    #fitpol1.Write()
    rfile.Write()
    rfile.Close()
    
    


if __name__ == '__main__':

    string="nominalLHC_constrWindow_5points"

    makeCalibPlot("B1B2Y", "LScalib_B1B2Y_v1.root", "plotsLScalib_B1Y_"+string+"_p1.pdf")
    makeCalibPlot("B1B2X", "LScalib_B1B2X_v1.root", "plotsLScalib_B1X_"+string+"_p1.pdf")
