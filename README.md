### Problem Statement:

This project addresses the need for a personalized way to stay informed by creating a newsletter based on the user's specific interests. 
It simplifies the process of gathering and summarizing relevant news, delivering the content in a concise, easy-to-read format.

### Summary:

This **Personalized Newsletter Generator** allows users to enter topics they're interested in—like technology, sports, or cooking—and receive 
a tailored newsletter with summarized articles. The project combines the power of the News API to gather articles with Groq's `llama3-8b-8192` AI model to summarize 
them efficiently. The app is built using Flask and includes the following features:

1. **User Interface:** A clean, responsive HTML interface where users input their interests and view the generated newsletter.
2. **Backend Logic:** Flask handles fetching articles, generating summaries, and rendering the newsletter.
3. **News API Integration:** Retrieves up-to-date news articles based on the user’s input.
4. **AI Summarization:** Uses Groq's language model to create concise summaries of the articles.
5. **Newsletter Display:** The output is styled into a visually appealing, dark-themed newsletter for easy reading.

With this system, users can quickly get a personalized summary of the latest articles on topics they care about, saving time and effort.




### Project Documentation: Personalized Newsletter Generator

This documentation explains how to set up and run the **Personalized Newsletter Generator**. 
It covers how to acquire the necessary API keys, configure them in Replit, and deploy the project to generate personalized news summaries using Flask.

---

### Prerequisites:
To build and run this project, you will need API keys from two platforms:
1. **News API** (for fetching news articles based on user input)
2. **GroqCloud API** (for summarizing articles using Groq’s AI model)

---

### Step-by-Step Setup:

#### 1. **Fork the Repository (if applicable)**:
   - Fork this project repository on GitHub to your own account.
   - Alternatively, you can upload the project files to Replit.

#### 2. **Generate API Keys**:
   You will need to generate API keys from the following services:

##### **a. News API**:
   - Visit [NewsAPI.org](https://newsapi.org/) and sign up for a free account.
   - After logging in, navigate to the **API Keys** section.
   - Generate an API key. This key will be used to fetch relevant articles based on user interests.
   - Copy the API key, as you will need it later.

##### **b. GroqCloud API**:
   - Visit [GroqCloud](https://groq.com/) and create an account if you don’t already have one.
   - Navigate to the **API Keys** section in your account.
   - Generate an API key for accessing Groq’s AI services.
   - Copy the key, as it will be required for running the summarization model.

---

#### 3. **Setting Up in Replit**:

##### **a. Create a New Replit Project**:
   - Go to [Replit](https://replit.com/) and create a new project.
   - Choose **Flask** as the template to build this web app.

##### **b. Add the Required Files**:
   - Add the provided Python code as `main.py` in your Replit workspace.
   - Under the `/templates` directory, add the `index.html` file that contains the UI for user input and newsletter display.

##### **c. Set Up API Keys in Replit**:
   1. In Replit, navigate to the **Secrets** section (usually under the padlock icon on the left sidebar).
   2. Add the following environment variables with the API keys you generated earlier:
   
      - **NEWS_API_KEY**: This should be your API key from NewsAPI.org.
      - **GROQ_API_KEY**: This should be your API key from GroqCloud.
   
   Example setup in Replit:
   - `NEWS_API_KEY=your_newsapi_key_here`
   - `GROQ_API_KEY=your_groqcloud_key_here`

---

#### 4. **Run the Project**:
   - After adding the API keys and setting up the files, click the **Run** button in Replit.
   - The Flask app will start, and you will be provided with a URL to access the web interface.
   - Enter your interests in the input box (e.g., "technology", "sports") and click the **Generate Newsletter** button.
   - The app will fetch the top 5 relevant news articles based on your input, summarize them using Groq’s model, and display the newsletter on the screen.

---

### Key Files:

- **`main.py`**: This is the main Flask application that handles fetching articles, summarizing them, and rendering the newsletter.
- **`/templates/index.html`**: This HTML file defines the web interface for users to enter their interests and view the personalized newsletter.

---

### API Rate Limits:

- **NewsAPI.org**: Free plans come with a limit of 100 requests per day.
- **GroqCloud**: Check your plan for rate limits on API calls for summarization.

---

### Conclusion:

With the **Personalized Newsletter Generator**, users can quickly get curated and summarized news based on their interests. By combining article 
fetching with AI-powered summarization, this project provides an efficient way to stay informed.




