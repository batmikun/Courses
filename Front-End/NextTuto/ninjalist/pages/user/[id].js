//OTHER FUNCTION THAT RUNS IN THE SERVER
//INSIDE WE PUT ALL THE POSSIBLE VALUES THAT THE USER CAN PUT IN THE URL
export const getStaticPaths = async () => {
    const res = await fetch('https://api.github.com/users')
    const data = await res.json()

    const paths = data.map(user => {
        return {
            params: { id: user.id.toString() }
        }
    })

    // THIS BECOME AN CONTEXT OBJECT
    return {
        paths,
        fallback: false
    }
}

// IN THIS FUNCTION WE ACCEPT THE CONTEXT OBJECT AUTOMATICALLY
export const getStaticProps = async (context) => {
    console.log(context)
    const res = await fetch(`https://api.github.com/users/${context.params.id}`)
    const data = await res.json()

    return {
        props: {
            users: data
        }
    }
}

const id = ({ users }) => {
    return ( 
        <div>
            <h1>{ users.login }</h1>
            <p>{ users.avatar_url  }</p>
            <p>{ users.followers_url  }</p>
            <p>{ users.following_url  }</p>
            <p>{ users.gists_url  }</p>
        </div>
     );
}
 
export default id;