In this read me file we are going to run our project onto your system .
step 1. extract our project from the zip file and open in any code editor like vscode or pycharm .(we will be needing pycharm for ruuning our projet later on)
step 2. after openning the project we have folder like :
* Data ; > in this folder we have the complete data that will be trained and tested on our ai mopdel 
it cointain 2 folders train , test , and two csv files : crop npk file cointain the data of all the crops and their nitrogen phosphorus and potassium requirements. and in crop recommendation file it cointain a lot of data of diffrent crops. All this data is taken from internets 
reference :
PEST DATASET: https://www.kaggle.com/simranvolunesia/pest-dataset
* 
* Irrigation folder in this folder we have a separate model for irrigation that have a separete readme aswell do check it out first.

* static folder :
this folder contain css , fonts , some images (that are used to make the front end of our website) , js (some js is also used in this project ) , user uploaded file contain some data that can be used for testing the pest detection model .

* templates :
this folder contain diffrent html files to render on our webpages (taken from internet github )

* utils 
this folder contain a python file (fertilzer.py){
    that contains a list of things that will be used according to the conditions for example when 
    Nhigh is called it will give out the respect text on the webpages 
}
* app.py is the file that render our webpages and fetch the result from our saved model
* crop_model (rl based )is the ai  agents models . you can try running these models one by one  it will genereate the Crop_recommendation.pkl that will be used later on .

* requirements contained our requiremts that are required to run our project 

step.3 To run our projet we need to install pycharm that can be installed from (https://www.jetbrains.com/pycharm/download/?section=windows)

step.4 after installing pycharm we will open our folder into pycharm .

step.5 we will be using conda environment for that install it from there official website .

//try step 7 first. If it does not work then step 6 then 7 .
step.6 after opening folder in the pycharm (now we are creating our conda environment )
click on file->settings->Projet:AgroAi->python interpretor ->add interpretor (at the right corner) ->add local interpretor -> conda environment -> then make you conda environment (accordingly)

step.7 Creating new environment using command --> conda create -n environmentname python==3.7.0

step.8 Activate environment using command --> conda activate environmentname

step.9 Install requirements by typing (cd ArgoAi) --> pip install -r requirements.txt

step.10 Now run app.py by writing command --> python app.py

this will run our website on a specific port .

on the website you can explore diffrent feature (on pesticide requiremets you can choose the image from static/user_uploaded folder)






