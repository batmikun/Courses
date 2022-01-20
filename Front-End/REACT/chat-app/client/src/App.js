import { useEffect, useState } from 'react';
import { StreamChat } from 'stream-chat';
import {
  Chat,
  Channel,
} from 'stream-chat-react';
import '@stream-io/stream-chat-css/dist/css/index.css';

import MessangingContainer from './components/MessagingContainer';
import Auth from './components/Auth';
import Video from './components/Video';

import { useCookies } from 'react-cookie';

const client = StreamChat.getInstance('pnrxun2q6zgd');

const App = () => {
    const [channel, setChannel] = useState(null);
    const [cookies] = useCookies(['user']);
    const [users, setUsers] = useState(null);

    const authToken = cookies.AuthToken;

    useEffect( () => {
        const getUsers = async () => {
            if (authToken) {
                const { users } = await client.queryUsers({ role: 'user' })
                setUsers(users);
            }
        }

        getUsers();
    }, [authToken]);

    const setupClient = async () => {
        try {
            await client.connectUser(
                {
                    id: cookies.UserId,
                    name: cookies.Username,
                    hashedPassword: cookies.HashedPassword,
                },
                authToken
            );

            const channel = client.channel('gaming', 'BatmiCo', {
                name: 'BatmiCo Chat',
            })

            setChannel(channel);

        } catch (err) {
            console.log(err);
        }
    };

    if (authToken) setupClient();

    return (
        <>
            {!authToken && <Auth />}
            {authToken && <Chat client={client} darkMode={true} >
                <Channel channel={channel}>
                    <Video />
                    <MessangingContainer />
                </Channel>
                </Chat> 
            }
        </>
    );
};

export default App;