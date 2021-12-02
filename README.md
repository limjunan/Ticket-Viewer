# Ticket-Viewer

<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#unit-testing">Unit Testing</a></li>
      </ul>
    </li>
    <li><a href="#challenge-requirements">Challenge Requirements</a></li>
    <li><a href="#design-considerations">Design Considerations</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A ticket viewer web application built for the Zendesk Coding Challenge 2022, Singapore. Built with the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework and designed using the [Zendesk Garden](https://garden.zendesk.com) design system. Application is in the app folder.

### Python files
- app.py is where the main code lives
- api_auth.py contains all authentication related functions
- ticket_handler.py contains all ticket related functions
- forms.py contains all WTForms
- constants.py contains all constants
- unit_test.py contains all unit tests, which are to be run

### Folders
- mocks folder contains all mocks for unit testing
- static folder contains all CSS and assets (svgs, fonts etc.)
- templates folder contains all HTML files to be routed to




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Python 3
- Git

### Installation

1. Clone the repository
  ```
  $ git clone https://github.com/limjunan/Ticket-Viewer.git
  ```
2. Navigate to the Ticket-Viewer directory
  ```
  $ cd Ticket-Viewer
  ```
3. Install external libraries in requirements.txt
  ```
  $ pip3 install -r requirements.txt
  ```

### Usage

1. Run the application on your local machine
  ```
  $ python3 app/app.py
  ```
2. Open up http://127.0.0.1:5000/ in your browser (or as specified in the output)

3. Client ID and Secret are your OAUTH credentials

### Unit Testing

1. Navigate to the app folder
  ```
  $ cd app
  ```
2. Run unit_tests.py (sample output below)
  ```
  $ python3 unit_tests.py
  Your subdomain: zcclimjunan
  ........
  ----------------------------------------------------------------------
  Ran 8 tests in 0.010s

  OK
  ```




<!-- Requirements -->
## Challenge Requirements

- [x] Connect to the Zendesk API
- [x] Request all the tickets for your account
- [x] Display them in a list
- [x] Display individual ticket details
- [x] Page through tickets when more than 25 are returned
- [x] Include a README with installation and usage instructions
- [x] Includes tests







<!-- Considerations -->
## Design Considerations

- Language of choice: Python🐍.

Besides being my go-to programming language, I decided on Python due to its simple syntax. The main audience of this application will be code reviewers, thus a simple syntax would make understanding written code much easier. 

- Browser-Based UI

I decided on a browser-based UI as opposed to the CLI option as I feel that I will enjoy this challenge much more doing this in the browser (it wouldn't be as mundane). Moreover, it would also give me the freedom to style the interface, which will be touched on below. Although the main users of the applications are the reviewers, I am sure everyone appreciates a pretty interface.

- Flask Framework

Having decided on using Python on a browser-based UI, it was a decision between the Flask and Django frameworks. I ended up choosing Flask as it was more suited for rapid development (a one week deadline). It is also a minimal platform, perfect for developing something for a small coding challenge. 

- Cursor-Based Pagination

The Zendesk Tickets API supports both cursor-based and offset pagination. Although offset pagination allows for users to choose specific pages, I felt that users have no need for that functionality. Therefore, cursor-based was the clear winner, as it is much faster when used with much bigger datasets, in the case of having thousands of tickets; and it allows for more accurate data when fetching from the API. 

- UI Design

I designed the UI as I feel that even though the main users of my application will be the reviewers, I should assume them to be the end-users. Thus, to maximize customer experience, a beautiful and easy-to-use interface is important. I wanted to make my application feel like part of the Zendesk ecosystem, so I used the Zendesk Garden design system as a base in designing the UI.




<!-- Screenshots -->
## Screenshots

![screenshot](screenshots/zendesk-screenshots.png)







<!-- CONTACT -->
## Contact

Bryan Lim - [LinkedIn](https://www.linkedin.com/in/lim-jun-an-bryan-068bba185/) - bryanlim080302@gmail.com

Project Link: [https://github.com/limjunan/Ticket-Viewer](https://github.com/limjunan/Ticket-Viewer)

🙀

<p align="right">(<a href="#top">back to top</a>)</p>
