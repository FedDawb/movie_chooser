
# **Group Project (Team 2)**  

This project aims to create a user-friendly app/website that helps users decide what to watch by providing tailored movie and TV show suggestions. The app leverages an external entertainment API to deliver personalized recommendations based on preferences such as genre, actors, directors, or release year.  

---

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
git clone https://github.com/emilyphillips02/CFG-GroupProject-Team2.git
cd CFG-GroupProject-Team2
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
