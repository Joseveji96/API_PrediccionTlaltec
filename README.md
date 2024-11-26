<h1 align="center">Hi 👋, I'm Eduardo Form TlalTec</h1>
<h3 align="center">A Passionate Software Developer From Mexico</h3>

## 📱 TlalTec API SERVER

### Description
API SERVER to response the results of a powerful and efficient artificial vision model that allows preventing, detecting and treating diseases and pests in avocado crops.

### 🚀 Features
- Artificial Vision capable of detecting different pests and diseases with 80% accuracy

### 📋 Prerequisites
- Python
- Flask

### 🔧 Installation

1. Clone the repository for frontend (Maybe you need acces to AvocadoCareAPI)
```bash
git clone https://github.com/Joseveji96/TlalTecApp.git
```

2. Clone this repository
```bash
git clone https://github.com/Joseveji96/API_PrediccionTlalTec.git
```


3. Run API SERVER
```bash
API_PrediccionTlaltec/server.py
```

4. **Configure Environment Variables**
Create a new folder `models/Tlaltec.pt` with the following content:

Example with actual IP and Random API_KEY:
```cmd
Running on http://Your_IP:5000
// Example with actual IP
Running on http://192.168.1.1:5000

```
ON FRONTEND TlalTecApp find or create the file constants on "src/sevises/constantes.ts"
```typescript
// Replace the next line for the new IP
export const cameraIP = "YOUR_NEW_ROUTE/detect_plagas"
// Example with actual IP
export const cameraIP = "http://192.168.1.1:5000/detect_plagas"

```

> ⚠️ **Important Configuration Notes:**
> 
> - To find your IP address:
>   - **Windows**: Open CMD and type `ipconfig`
>   - **MacOS/Linux**: Open terminal and type `ifconfig` or `ip addr`
> - Make sure both your development machine and mobile device are on the same network
> - The ports (3000 and 5000) must match your backend services configuration
> - Do not use 'localhost' or '127.0.0.1' as these won't work with physical devices
> - 


### 🔍 Troubleshooting
If you have connection issues:
- Check that your device and computer are on the same network
- Confirm that ports 3000 and 5000 are not blocked by your firewall
- Try pinging your IP from the mobile device
- If you use antivirus, check that it is not blocking connections
- Make sure that the backend services are running correctly


### 🛠️ Built With
- FLASK
- Python


### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### 📫 Contact
- 🔭 I'm currently working on **API PREDICTION TLALTEC**
- 📧 Email: joseveji96@gmail.com
- 💼 LinkedIn: www.linkedin.com/in/eduardovelazco96
- 🌐 Portfolio: on Development



### 📝 License
This project is licensed under the [MIT License](LICENSE)