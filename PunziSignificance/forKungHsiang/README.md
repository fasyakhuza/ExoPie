## How to calculate the punzi significance uncertainty

#### Produce singlevaluesignal3.root
use EfficiencyPlot_FJetCSVforKungHsiang.py for producing it

* Change the line 11 for the signal input file directory path
* Change the line 13 for the signal file name
* when you run this macro, you will get that root file and the signal efficiency value

#### Get the punzi significance uncertainty
use ErrorPropagationPunziSignificance.py for producing it

* Change the line 9 for the background input file directory path
* Change the line 11 for the background file name
* Change the line 13 for the background cross section
* Change L18 for the integrated luminosity
* Change L105 for the signal efficiency that you get from previous macro
* When you run this second macro, you will get the punzi significance
