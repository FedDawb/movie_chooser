
# **Group Project (Team 2)**  

This project aims to create a user-friendly app/website that helps users decide what to watch by providing tailored movie and TV show suggestions. The app leverages an external entertainment API to deliver personalized recommendations based on preferences such as genre, actors, directors, or release year.  

---
![Homepage](movie_chooser/Screenshot-2025-07-27-113847.png)




## **Activity Log Link**

[Google Spreadsheet](https://docs.google.com/spreadsheets/d/1rFKN-fSPBCfbnL2ba5ftVVI_m5hxxxLb/edit?usp=sharing&ouid=115152390265221081079&rtpof=true&sd=true)

---

## **Key Features**  
- User accounts  
- Keyword searching  
- Save favourites  
- ~~Blocking movies/actors you don't want to see~~  
- ~~Age restrictions (e.g., 18+ films)~~

---

## **Design and Architecture**  
- **Backend:** Python backend with modular structure.  
- **Frontend:** Web interface (basic Flask templates or integrated React/HTML).  
- **Database:** SQL for saving user data and favourite titles.  
- **API Integration:** Uses an external entertainment API.  
- **OOP Design:** Classes for User, Movie/TV Show, and Search to ensure efficient data handling.  

---

## **How to Run**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/FedDawb/movie_chooser.git
cd CFG-group-project-MovieChooser
```

### **2. Set-up the Environment**  
```bash
python -m venv venv  
source venv/bin/activate  # On Mac/Linux  
venv\Scripts\activate     # On Windows  
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables** 
Create a .env file in the project root directory and add the following variables:
```bash
DATABASE_URL=your_database_url  
API_KEY=your_api_key  
```

### **5. Run the Applications** 
```bash
flask run
```
The app will be available at http://127.0.0.1:5000.


### **5. Run Unit Tests** 
```bash
python -m unittest discover
```

### **7. Access the Application**
Open your web browser and navigate to:
```bash
http://127.0.0.1:5000
```
## Revisiting the Project: Addressing Access Difficulties
After a period of inactivity, you might encounter issues when trying to access or run the project again. This could be due to changes in your environment, outdated dependencies, or other factors. This section outlines a common problem we faced when revisiting the project after several months and the steps we took to resolve it, which might be helpful if you experience similar difficulties.

# Troubleshooting
Virtual Environment Activation Issues
If .\venv\Scripts\activate is not recognized, try Activate.ps1 in PowerShell or activate.bat in Command Prompt.

If you see an execution policy error in PowerShell, run:

powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Then try activating again.

Empty or Missing requirements.txt
If requirements.txt is empty, regenerate it by running:

bash
pip freeze > requirements.txt
after installing required packages.

Preventing .env from Being Pushed
Ensure .env is listed in .gitignore.

If .env was committed, remove it with:

bash
git rm --cached .env
git commit -m "Remove .env file"
git push

## Common Flask Run Errors
Make sure environment variables are correctly set (FLASK_APP, .env contents).

Ensure all dependencies are installed.

Verify your database is running and accessible if your app connects to one.

## If You Encounter Module or Import Errors
Double-check that you are running inside the activated virtual environment.
Reinstall dependencies:

bash
pip install -r requirements.txt

## After Periods of Inactivity
Reactivate the virtual environment.

Run pip install -r requirements.txt again to refresh packages if needed.

Check .env is still configured properly.


## Future improvements
Working on a site to host the project
