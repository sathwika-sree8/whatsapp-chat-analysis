# 📊 WhatsApp Chat Analysis

## 📝 Overview
WhatsApp Chat Analysis is a data-driven project that helps users analyze their WhatsApp conversations using Python. The tool provides insights such as message statistics, emoji usage, word frequency, and more.

## 🚀 Features
- 📈 **Message statistics**: Number of messages sent per user, per day, and total messages.
- 🔤 **Word frequency analysis**: Identify commonly used words.
- 😂 **Emoji usage analysis**: Detect the most frequently used emojis.
- 📅 **Timeline analysis**: Track message activity over time.
- 📊 **Data visualization**: Graphs and charts to understand chat patterns.

## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Matplotlib** (for data visualization)
- **Seaborn** (for advanced visualizations)
- **Pandas** (for data manipulation)
- **WordCloud** (for text visualization)
- **emoji** (for emoji analysis)
- **urlextract** (for extracting links from chats)

## 📂 Project Structure
```
whatsapp-chat-analysis/
│── app.py                # Main application file
│── helper.py             # Helper functions for data processing
│── preprocessor.py       # Chat preprocessing functions
│── requirements.txt      # Dependencies
│── Procfile              # Deployment configuration (Heroku)
│── setup.sh              # Setup script for deployment
│── stop_hinglish.txt     # Stopwords list
│── WhatsApp-Chat-Analysis.ipynb  # Jupyter Notebook for analysis
└── data/
    ├── WhatsApp Chat with [Person/Group].txt  # Sample chat data
```

## 🔧 Installation & Usage
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/sathwika-sree8/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```sh
streamlit run app.py
```
### 4️⃣ Upload Your WhatsApp Chat
1. Export a chat from WhatsApp (without media).
2. Upload the `.txt` file to the app.
3. Analyze the chat insights!

## 🌐 Deployment
You can deploy this project on **Heroku** using the provided `Procfile` and `setup.sh`.

## 🤝 Contributing
Feel free to fork this repository, make enhancements, and submit a pull request! 😊

## 📜 License
This project is **open-source** and available under the [MIT License](LICENSE).

---
✨ Developed by **Sathwika Sree** 🚀
