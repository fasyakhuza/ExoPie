#include <iostream>

using namespace std;
void tmp(){
	int i,j;
	vector<float> t, d;
	t.push_back(.133);
	t.push_back(.134);
	t.push_back(.071);
	t.push_back(.665);
	for (i=0;i<3;i++)	d.push_back(.006);
	d.push_back(.014);
	
	// calculate
	float BR1=0,BR2=0,BR3=0, sigma;
	float dd1=0,dd2=0, dd3=0;
	
	for (i=0;i<3;i++){
		for ( j=0;j<3;j++) {
            //TT->leptonic
			BR1 += t[i] * t[j];
			sigma = t[i] * t[j] * TMath::Sqrt( (d[i]/t[i]) * (d[i]/t[i]) + (d[j]/t[j]) * (d[j]/t[j]) );
			dd1 += sigma * sigma;
		}
        //TT->Semileptonic
		BR2 += t[i]*t[3] * 2;
		sigma = t[i]*t[3] * TMath::Sqrt( (d[i]/t[i]) * (d[i]/t[i]) + (d[3]/t[3]) * (d[3]/t[3]) );
		dd2 += sigma * sigma * 2;
	}
    //TT->hadronic
	BR3 = t[3] * t[3];
	sigma = t[3] * t[3] * TMath::Sqrt( (d[3]/t[3]) * (d[3]/t[3]) + (d[3]/t[3]) * (d[3]/t[3]) );
	dd3 = sigma * sigma;
	cout << "BR1= " << BR1 << endl;
	cout << "dd1= " << TMath::Sqrt(dd1) << endl;
    cout << "XS_eff_lep= " << 831.76*BR1 << " +- " << 831.76*dd1 << endl; //NNLO
	cout << "BR2= " << BR2 << endl;
	cout << "dd2= " << TMath::Sqrt(dd2) << endl;
    cout << "XS_eff_semilep= " << 831.76*BR2 << " +- " << 831.76*dd2 << endl; //NNLO
	cout << "BR3= " << BR3 << endl;
	cout << "dd3= " << TMath::Sqrt(dd3) << endl;
    cout << "XS_eff_had= " << 831.76*BR3 << " +- " << 831.76*dd3 << endl; //NNLO
}
