import {
    ChannelHeader,
    MessageList,
    MessageInput,
    Thread,
    Window,
  } from 'stream-chat-react';


const MessangingContainer = () => {
    return (
        <>
            <Window>
            <ChannelHeader />
            <MessageList />
            <MessageInput />
            </Window>
            <Thread />
        </>
     );
}
 
export default MessangingContainer;