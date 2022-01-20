// GLOBAL OBJECT
/**
 * We get acces to a global objects, his methods and properties
 * is kinda of the object window for the js browser
 * 
 * Node Global Object - global
 * 
 */

// Methods for the global object
/**
 * global.setTimeout(callback, delay)
 * global.setInterval(callback, delay)
 * global.clearTimeout(id)
 */

console.log(global);

setTimeout(() => { // Execute something after some time
    console.log('Hola');
    clearInterval(int); // Stop the interval
}, 3000);

const int = setInterval(() => { // the difference between this and setTimeout is that setInterval keeps running for ever
    console.log('Hola');
}, 1000);

console.log(__dirname); // The path of the current directory
console.log(__filename); // The path of the current file

// The window and the document object not work in NodeJs

// MODULES & REQUIRE
/**
 * 
 * To export something from a module we use the export keyword
 * module.export = {
 *    people,
 *    ages
 * }
 * 
 * If we dont have unstall an package.json file, we have to import things with the require method
 *
 * To be able to use the import we have to indicate that the program is "type": "module"
 */

const { people, ages } = require('./people.js');

console.log(people, ages);

/**
 * require modules that came with the language
 */


// sistem module
const os = require('os');

// fileSystem module
const fs = require('fs');

// read file
fs.readFile('./txt/blog.txt', 'utf-8', (err, data) => {
    if (err) throw err;
    console.log(data);
})

const { promises: fs } = require('fs');

const file = async () => {
    try {
        const data = await fs.readFile('./txt/blog.txt', 'utf-8');
        return data
    } catch (err) {
        console.log(err);
    }
}

// writing file

fs.writeFile('./txt/blog.txt', 'Hello world', err => {
    if (err) throw err;
    console.log('File created');
})

// directories

fs.mkdir('./assets', err => {
    if (err) throw err;
    console.log('Directory created');
})

// deleting files

fs.unlink('./txt/blog.txt', err => {
    if (err) throw err;
    console.log('File deleted');
})

// For large amount of data is most efficient to use streams

// STREAMS - Start using data, before it has finished ñpadomg
// Buffers - A buffer is a chunk of data that is stored in memory

/**
 * The stream is like a stream in the real life, it allows to read data while it's loading
 * the buffers are the chunks of data that we read while the file is bean readed.
 */

const readStream = fs.createReadStream('./txt/blog.txt', { encoding: 'utf-8' });
const writeStream = fs.createWriteStream('./txt/blog2.txt');

readStream.on('data', chunk => {
    console.log(chunk);
    writeStream.write(chunk);
})

// PIPE - from a redableStream to a writableStream
readStream.pipe(writeStream); //This is the same as the code above 


/**
 * We can start a project of node with the command
 * 
 * npm init -y
 * 
 * this will initialize the package.json file
 * 
 * 
 */