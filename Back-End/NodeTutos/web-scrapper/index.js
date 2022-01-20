import express from "express";
import axios from "axios";
import cheerio  from "cheerio";

const PORT = 8000;

const app = express();

const url = 'https://www.theguardian.com/uk'; 

app.get('/', (req, res) => {
    axios(url)
    .then(response => {
        const html = response.data;
        const $ = cheerio.load(html);
        const articles = [];
        $('.fc-item__container').each((i, el) => {
            const title = $(el).find('h2').text();
            const link = $(el).find('a').attr('href');
            const image = $(el).find('img').attr('src');
            const description = $(el).find('p').text();
            articles.push({
                title,
                link,
                image,
                description
            });
        });
        
        res.json(articles);
    })
    .catch(error => {
        console.log(error);
    })
})

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
})