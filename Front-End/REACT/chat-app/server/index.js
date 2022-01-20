const port = 8000;

const express = require('express');
const cors = require('cors');
const bcrypt = require('bcrypt');
const {v1: uuidv1} = require('uuid');
const { connect } = require('getstream');

const app = express();

const StreamChat = require('stream-chat').StreamChat;

app.use(cors());
app.use(express.json());

app.post('/singup', async (req, res) => {
    try {
        const { username, password } = req.body
        const userId = uuidv1();
        const hashedPassword = await bcrypt.hash(password, 10);
        
        const client = connect('pnrxun2q6zgd', '5r8gyjub5uf8t2d6pz924c2ne7n56nbnpdf7vamu3rykwjxa5wtbad74udqnk7ec', '1158519')
        const token = client.createUserToken(userId);

        res.status(200).json({ username, userId, hashedPassword, token });
    } catch (error) {
        console.log(error);

        res.status(500).json({message : error})
    }
})

app.post('/login', async(req, res) => {
    try {
        const api_key = 'pnrxun2q6zgd';
        const api_secret = '5r8gyjub5uf8t2d6pz924c2ne7n56nbnpdf7vamu3rykwjxa5wtbad74udqnk7ec';
        const api_id = '1158519';

        const { username, password } = req.body;
        const client = connect(api_key, api_secret, api_id)
   
        const chatClient = StreamChat.getInstance()
        const { users } = await chatClient.queryUsers({ name: username })

        if (!username.length) return res.status(400).json({ message: 'Username does not exist' })

        const success = bcrypt.compare(password, users[0].hashedPassword);
        const token = clinet.createUserToken(users[0].id);
        const confirmedName = users[0].username
        const userId = users[0].id

        if (success) res.status(200).json({  token, username: confirmedName, userId })

        res.status(400).json({ message: 'Password is incorrect' })

    } catch (error) {
        console.log(error);
    }
})

app.listen(port, () => {
    console.log('Server running on port ' + port);
});