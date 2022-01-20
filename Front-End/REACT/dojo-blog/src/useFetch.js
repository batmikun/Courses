import { useState ,useEffect } from "react";

const useFetch = (url) => {

    const [data, setData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const abortController = new AbortController();


        fetch(url, {signal: abortController.signal, method: 'GET'})
            .then(response => {
                if(!response.ok) {
                    throw new Error(response.statusText);
                }
                return response.json()
            })
            .then(data => {
                setData(data)
            })
            .catch(error => {
                if(error.name === "AbortError") {
                    console.log("Request aborted");
                } else {
                    setError(error.message)
                }
            })

        return () => { abortController.abort() }   
    }, [url]);

    return { data, error }
}

export default useFetch;