//
//  overlap.cpp
//  
//
//  Created by Fasya Khuzaimah on 09.10.19.
//

#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <TH1F.h>
#include <TFile.h>
#define overlap_cxx
#include <TCanvas.h>
#include <TLegend.h>
#include <TStyle.h>

using namespace std;
void overlap(){
    TLegend *leg = new TLegend(0.45,0.7,0.75,0.85); //0.55,0.3,0.75,0.4 //0.15,0.75,0.45,0.85
    leg->SetBorderSize(0);
    leg->SetTextSize(0.027);
    
    //bkg before b-tag
    TFile* f1 = new TFile("test.root","READ");
    TTree* t1 = (TTree*)f1->Get("outTree");
    TH1F* h1 = new TH1F("h1","Mass of Candidate Jets",50,0,1000);
    t1->Draw("st_THINjetCanMass>>h1","","goff");
    h1->SetDirectory(0);
    f1->Close();
    
    
    //signal before b-tag
    TFile* f2 = new TFile("test3.root","READ");
    TTree* t2 = (TTree*)f2->Get("outTree");
    TH1F* h2 = new TH1F("h2","Mass of Candidate Jets",50,0,1000);
    t2->Draw("st_THINjetCanMass>>h2","","goff");
    *h2 = (50)*(*h2);
    h2->SetDirectory(0);
    f2->Close();
    
    
    //bkg after b-tag
    TFile* f3 = new TFile("test4.root","READ");
    TTree* t3 = (TTree*)f3->Get("outTree");
    TH1F* h3 = new TH1F("h3","Mass of Candidate Jets",50,0,1000);
    t3->Draw("st_THINjetCanMass>>h3","","goff");
    h3->SetDirectory(0);
    f3->Close();
    
    
    //signal after b-tag
    TFile* f4 = new TFile("test5.root","READ");
    TTree* t4 = (TTree*)f4->Get("outTree");
    TH1F* h4 = new TH1F("h4","",50,0,1000);
    t4->Draw("st_THINjetCanMass>>h4","","goff");
    h4->SetDirectory(0);
    f4->Close();
    
    
    
    
    TCanvas *c1 = new TCanvas("c1","c1", 900, 900); //kiri-kanan,atas-bawah
    gStyle->SetOptStat(0);
    h1->GetXaxis()->SetTitle("mass (GeV)");
    h1->GetYaxis()->SetTitle("number of candidate jet");
    h1->GetYaxis()->SetTitleOffset(1.5); //meletakkan nama y axis seberapa jauh dari sumbu y
    h2->GetXaxis()->SetTitle("mass (GeV)");
    h2->GetYaxis()->SetTitle("number of candidate jet");
    h2->GetYaxis()->SetTitleOffset(1.5);
    h3->GetXaxis()->SetTitle("mass (GeV)");
    h3->GetYaxis()->SetTitle("number of candidate jet");
    h3->GetYaxis()->SetTitleOffset(1.5);
    
    //c1->SetLogy();
    /*h1->SetLineColor(1);
    h1->SetLineWidth(5);
    h1->Draw();
    h2->SetLineColor(4);
    h2->SetLineWidth(5);
    h2->Draw("histsame");*/
    h3->SetLineColor(1);
    h3->SetLineWidth(5);
    h3->Draw("histsame");
    h4->SetLineColor(4);
    h4->SetLineWidth(5);
    h4->Draw("histsame");
    
    //leg->AddEntry(h1,"Background before b-tag","l");
    //leg->AddEntry(h2,"Signal before b-tag","l");
    leg->AddEntry(h3,"Background after b-tagging");
    leg->AddEntry(h4,"Signal after b-tagging");
    leg->Draw();
    
    c1->SaveAs("overlap5.png");
    
}
