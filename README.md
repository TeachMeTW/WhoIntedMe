# WhoIntedMe

This is WhoIntedMe, a fullstack application designed to help League of Legends players determine who inted their game! With WhoIntedMe, we utilize statistical machine learning and data analysis to accurately identify who inted your ranked games. Now you can hold your teammates accountable with FACTS and LOGIC.
![Project Banner](Logo.png)

## 🚀 Soon to be features

- Accurate Int Feed Detection
- Visualize Gameplay Patterns
- Advanced Player Insights

## 🔗 Developers

- Lead Developer: [@Robin Simpson](https://github.com/TeachMeTW)
- Backend Developer: [@Sebastian Sliva](https://github.com/Cybiii)
- Frontend Developer: [@Jay Chong](https://github.com/Kizum1)
- Frontend Developer: [@Khashayar Moradpour](https://github.com/khmorad)

## Tech Stack

### Front-End:
![React](https://img.shields.io/badge/-React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/-Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Back-End:
![Python](https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/-Flask-000?style=for-the-badge&logo=flask&logoColor=white)

## Database:
![SQLite](https://img.shields.io/badge/-SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)


# How to setup

CD into WhoIntedMe, and run the following commands in the terminal.

`poetry shell`

`poetry install`

`poetry run pre-commit install`

To run the backend, run `poetry run flask run`

# To launch app

CD into app, and run the following commands in the terminal

`poetry shell`

`poetry run npm install`

`poetry run npm start`

Once node_modules folder has been created you can run "poetry run npm start" anytime to launch the app

# To load docker

`docker build -t whointedme .`

`docker run -p 8000:8000 whointedme`



