const express = require('express');
const app = express();
const cors = require('cors');
const axios = require('axios');

app.use(cors());
app.use(express.json())

app.get('/api/test', (req, res) => {

    res.json('test ok');

});

app.post('/api/coordinates', async (req, res) => {
    const data = req.body;

    try {
        const response = await axios.post('http://localhost:5000/api/getAvailableMoves', data);
        res.json(response.data);
        console.log(data)
    } catch (error) {
        console.error('Error sending data to Python backend:', error);
        res.status(500).json({ error: 'Failed to send data to Python backend' });
    }
});

app.post('/api/board', async (req, res) => {
    const data = req.body;

    try {
        const response = await axios.post('http://localhost:5000/api/sendBoard', data);
        res.json(response.data);
        console.log(data)
    } catch (error) {
        console.error('Error sending data to Python backend:', error);
        res.status(500).json({ error: 'Failed to send data to Python backend' });
    }
});

app.listen(4000)