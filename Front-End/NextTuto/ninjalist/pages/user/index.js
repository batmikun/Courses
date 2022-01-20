// THIS RUNS IN THE SERVER
// WHENEVER WE WANT TO FETCH DATA IN THE SERVER INSTEAD OF THE BROWSER
// WE USE export const getStaticProps = async () => {
//     const res = await fetch('https://jsonplaceholder.typicode.com/users');
//     const data = await res.json();
//     return {
//         props: {
//             users: data
//         }
//     }
// }
//}

import Link from "next/link";



export const getStaticProps = async () => {
    const res = await fetch('https://api.github.com/users');
    const data = await res.json();

    return {
        props: {
           users : data
        }
    }    
}

const index = ({ users }) => {
    return ( 
        <div>
            { users.map(user => (
            <Link key={user.id} href={ `/user/${ user.id }` }>
                <a><li>{user.login}</li></a>
            </Link>
            )) }
        </div>
     );
}
 
export default index;