## Purpose of this Project:
This repo serves as the backend of the calorie agent app. This is a simple back-end built with LangChain's framework for ReAct Agents.
Project completely launched and can be seen here: https://calicoapp.netlify.app/
<img width="774" height="743" alt="image" src="https://github.com/user-attachments/assets/64046e64-4100-41c2-8fe0-a7c32fd1f8c3" />

BEST TO BE OPENED ON A MOBILE DEVICE.
- [ ] Big Caveat: Broken loading screen - so loading time may look blank but actually works.

## How to Use:
In the app, you can describe what you ate, take a picture or send a photo. The agent analyzes the user's input and brings back the caloric equivalent for the meal then logging.
The Calorie Agent has access to a free tier API for Calorie Ninja. The agent breaks down meals into simple ingredients that can be easily searched through the database.
The agent also estimates the quantity used per material / ingredient.

## Goal of the Project:
This serves as a practice on LangChain's framework and creation of a productive backend pattern.

## TODOs:
- [x] Create Agent Class
- [x] Create Singleton Instance with FastAPI
- [x] Create docker build
- [x] Launch both backend and UI to netlify and Railway.
- [ ] Update tool: Migrate from Calorie Ninja to FatSecret: https://platform.fatsecret.com/
