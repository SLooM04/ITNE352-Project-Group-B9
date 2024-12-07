# ITNE352-Project-Group-B9
<h1>Multithreaded News Client/Server</h1>
<h1>S1 2024-2025</h1>
<h1>Group</h1>
<p><strong>B9</strong></br>
Redha Mohammed Saleh-202210328 </br>
Salman Mohammed Jassim-202206207
</p>
<h1>Project Description</h1>
<p>This project is a client-server application that allows users to fetch and view news articles and sources using the NewsAPI. The system enables searching for news based on keywords, categories, or countries and displays results interactively.
</p>

<h1>Table of contant</h1>
<ul>
  <li>Project Title</li>
  <li>Project Description</li>
  <li>Requirements</li>
  <li>How to Run</li>
  <li>Scripts Description</li>
  <li>Additional Concepts</li>
  <li>Acknowledgments</li>
  <li>Conclusion</li>
</ul>

<h1>Requirements</h1>
<ol>
  <li>Install Python
Make sure you have Python installed on your computer (preferably version 3.7 or higher).</li>
  
  <li>Install Required Libraries
Run the following command to install the required library:
    (pip install requests)</li>

  <li>Set Up the Server
    Open the server.py file and replace the API_KEY variable with your own NewsAPI key.
Run the server using this command:(python server.py)</li>

<li>Set Up the Client
Open the client.py file and run it in a different terminal window or a separate device using this command:(python client.py)</li>

<li> Run the Program
Once both the server and client are running, follow the instructions displayed on the client screen to interact with the system and browse news articles.</li>
</ol>

<h1>How to Run</h1>
<P><strong>step 1:</strong> open terminal then write "python server.py"</br>
<strong>step 2:</strong> open the terminal by ctrl+shift+5 write "python client.py"</br><strong>step 3:</strong> Interact with the System: Follow the menu displayed in the client to fetch news or view sources.</P>

<h1>The Scripts</h1>
<P>
This script is a client-server application that allows users to access news articles and sources using NewsAPI. Here's a summary of what each part does:
</br>
<strong>Server:</strong></br>
- The server (server.py) runs on a specific IP and port.</br>
- It accepts client connections, shows a menu to the user, and handles requests like searching headlines, listing sources, or quitting.</br>
- The server connects to NewsAPI to fetch live news and sends the results back to the client.</br>

<strong>Client:</strong></br>
- The client (client.py) connects to the server and interacts with the user.</br>
- Users can input their name and choose options from the menu to search for news or sources.</br>
- The client sends requests to the server and displays the results received.</br>

<strong>Key Features:</strong></br>
The script is interactive, with options to search by keyword, category, or country. It uses threads on the server side to handle multiple clients simultaneously. The NewsAPI integration ensures the data is always up-to-date.
  
</P>
<h1>Additional Concept</h1>
<ul><li><strong>Object-Oriented Programming (OOP):</strong></br>
Using Object-Oriented Programming (OOP) helped organize the code by dividing it into classes that represent specific parts of the system, such as the server and client. This made the code more readable and maintainable, while also making it easier to add new features or modify existing functions without affecting other parts of the code.</li></ul>

<h1>Acknowledgments</h1>

<h1>Conclusion</h1>




