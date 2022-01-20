import Link from "next/link";
import { useRouter } from "next/router";
import { useEffect } from "react";


const NotFound = () => {

    const router = useRouter();

    useEffect(() => {
        setTimeout(() => {
            router.push("/");        
        }, 3000)
    })

    return ( 
        <div>
            <h1>Oooooops...</h1>
            <h2>That page cannot be found</h2>
            <Link href="/">
                <a>Go back to homee</a>
            </Link>
        </div>
     );
}
 
export default NotFound