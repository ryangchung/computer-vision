# computer-vision
CUHacking Computer Vision Project

### Installation
#### API
```
pip install "fastapi[standard]"
pip install tensorflow
pip install Pillow
pip install selenium
```
#### Chrome Extension
```
npm install
```

### How-To Run
#### API
```
cd api
fastapi dev api.py
```
####
```
cd chrome_extension
npm run build
Navigate to chrome://extensions/ > load unpacked > import chrome_extension/build/
```

### Folder Structure
`/api`: FastAPI web server (interfacing with the frontend)  
`/client`: React-TypeScript frontend on Vite  
`/database`: SQLite database and database functions  
`/docs`: All images and documentation for demo and architecture  
`/tensor-model`: All code and datasets relating to the tensorflow model (train the model, and output responses to the FastAPI API layer to be transmitted to the client)  

### Figma Mockup
https://www.figma.com/design/PhsTDvoAb9rKnLumvbxQxQ/CV-Hackathon?node-id=0-1&t=T1WLhxZr8HmhLJvr-1
