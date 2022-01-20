<?php

/**
 * SPL Iterators
 */

/**
 * One of the most usefull parts of SPL (Standard PHP Library)
 * 
 * Iterator are a series of classes that make it easy to traverse a structure
 * such as an array, an object, or a file with a foreach loop
 * 
 * For example, DirectoryIterator, FilesystemIterator and RecursiveIterator
 * give you quick access to the file system
 * 
 * You can create selective loops using regex, or callback func as filter
 * and CachingIterator looks ahead for the next element
 * 
 * Internally all the iterators implements the same interface
 * that has 5 methods:
 *          1- rewind() -> Moves the iterator back to the first element
 *          2- valid() -> Checks if there's another element to move to
 *          3- key() -> Returns the key of the current element (number or string)
 *          4- current() -> Value of the current element
 *          5- next() -> Moves the iterator to the next element
 * 
 * ForEach Loop call this methods automatically
 * 
 * ADVANTAGES:
 *      Simpler Code
 *      Reusable Code
 *      Faster because underlying code is written in C
 *      Often redecus memory usage
 *      Iterator Can Be Chained
 * 
 * USING SPL ITERATORS:
 *     1- Create an Iterator with the New keyword
 *     2- Set options using class constants, FileSystemIterator::SKIP_DOTS
 *     3- Set options on instantions or using setFlags()
 * 
 * CHAINING ITERATORS:
 *     We can chain iterator to fine tune wich elements are selected
 *     as we traverse the structure
 * 
 *     For example
 *          $dir = new FilesystemIterator('.'); -> This traverse the current directory
 *          $jpegs = new RegexIterator($dir, '/\.jpg$/'); -> This traverse the current directory and select only jpg files
 *          $second_two = new LimitIterator($jpegs, 2, 2); -> This traverse the current directory and select only the third and fourth jpg files
 *          foreach ($second_two as $file) {
 *             echo $file . '<br>'; -> each element is a object of SplFileInfo
 *         }
 * 
 *  Each element inside the loop is an object
 *  Use iterator_to_array() to convert the iterator to an array
 */

/**
 * DirectoryIterator
 */

$dir = new DirectoryIterator('./Exercise Files/common/images');

foreach ($dir as $key => $file) {
    if ($file->isFile()) {
        $files[] = clone $file; // we have to clone the objects to create an array of files, passing a reference doesn't work
    }
}

/**
 * FilesystemIterator
 */

// With FileSystemIterator we don't need to clone the object to store it in a array
// because the object is already cloned when we use the foreach loop

// Is not a good practice to store the object in an array
// the best practices is to perform the operations needed inside the foreach
// to avoid memory loss

// To fix the problem with the backslash in the path, we can use a option
// that we have in the filesystemiterator class constants

// We can change the name of the key to only the filename with another constast

// When we have more than one option, we use setFlags()

// setFlags(Iterator::Constanst | Iterator::Constant | ...)

$file = new FileSystemIterator('./Exercise Files/common/images');
$file->setFlags(FilesystemIterator::UNIX_PATHS | FilesystemIterator::KEY_AS_FILENAME);

foreach ($file as $key => $file) {
    if ($file->isFile()) {
        //echo $key . $file . "\n";
    }
}

/**
 * Single Directory Iteraros
 * 
 * Directory Iterator
 *      - Includes dot files
 *      - Numbered keys
 *      - Path not included in value
 *      - There are not configuration options
 * 
 * FilesystemIterator
 *      - Extends the functionally of DirectoryIterator
 *      - Dot files skipped
 *      - Pathname used for key
 *      - Path included in value
 *      - Configurable
 *      - Cloning not necessary
 * 
 * 
 */

/**
 * RECURSIVE ITERATOR
 */
$files = new RecursiveDirectoryIterator('./Exercise Files/common');
$files->setFlags(FilesystemIterator::SKIP_DOTS | FilesystemIterator::UNIX_PATHS);

// With the recursiveIteratorIterator we can traverse the directory recursively
// because RecursiveDirectoryIterator only descend one level
// we can limit the depth of the RecursiveIteratorIterar with setMaxDepth() method
$files = new RecursiveIteratorIterator($files, RecursiveIteratorIterator::SELF_FIRST);
$files->setMaxDepth(1);

foreach ($files as $file) {
    //print($file . "\n");
}

/**
 * Obtaining data from the files
 */

$files = new FilesystemIterator('./Exercise Files/common/images', FilesystemIterator::UNIX_PATHS);

foreach ($files as $file) {
    if ($file->getExtension() == 'jpg') {
        // echo $file->getFilename() . ' is ' . $file->getSize() . ' bytes. Its absolute path is ' . $file->getRealPath() . "\n";
    }
}


/**
 * Experiment with SPL File Object
 */

$docs = new FilesystemIterator('./Exercise Files/common/documents', FilesystemIterator::UNIX_PATHS);

// READ

foreach ($docs as $doc) {
    if ($doc->getExtension() == 'txt') {
        $textfile = $doc->openFile();
        $textfile->setFlags(SplFileObject::SKIP_EMPTY | SplFileObject::READ_AHEAD | SplFileObject::DROP_NEW_LINE);
        //echo $textfile->getFilename() . ' is ' . $textfile->getSize() . ' bytes. Its absolute path is ' . $textfile->getRealPath() . "\n";
        //foreach ($textfile as $line) {
        //    echo $line . "\n";
        //}
        $textfile->seek(2); // seek to the third line
        //echo $textfile->current(); // and we display the line that we are curretly reading
    }
}

// WRITE

$docs = new FilesystemIterator('./Exercise Files/common/documents', FilesystemIterator::UNIX_PATHS);

foreach ($docs as $doc) {
    if ($doc->getExtension() == 'txt') {
        $textfile = $doc->openFile('r+');
        $textfile->setFlags(SplFileObject::SKIP_EMPTY | SplFileObject::READ_AHEAD | SplFileObject::DROP_NEW_LINE);
        //while (!$textfile->eof()) {
        //$line = $textfile->fgets();
        //if (strpos($line, 'PHP') !== false) {
        //    $textfile->fwrite('<span style="color: red;">' . $line . '</span>');
        //} else {
        //    $textfile->fwrite($line);
        //}
        //}
    }
}

/**
 * CONVERT A CSV INTO AN ARRAY
 * 
 */

$csvfile = new SplFileObject('Exercise Files/common/data/cars.csv');
$csvfile->setFlags(SplFileObject::READ_CSV);
foreach ($csvfile as $line) {
    $cars[] = $line;
}
//echo print_r($cars);

/**
 * By default SplFileObject expects that the CSV file uses
 * comma for delimiter and double quotes for enclosure and the backslash for escape
 * 
 * If we want to use different format we have to use setCsvControl(delimiter, enclousure, escape) method
 */


$csvfile = new SplFileObject('Exercise Files/common/data/cars_tab.csv');
$csvfile->setFlags(SplFileObject::READ_CSV);
$csvfile->setCsvControl("\t");
foreach ($csvfile as $line) {
    $cars[] = $line;
}
//echo print_r($cars);

/**
 * FILTERING WITH GLOBITERATOR
 * 
 * When traversing the file system,we are often interested only
 * in certain types of files.
 * 
 * In previous excersise we filter the file with an if extension plus the method ->getExtension()
 * 
 * We can filter files by globbing
 * 
 * 
 * 
 */

$files = new GlobIterator(__DIR__ . '/Exercise Files/common/images/*.jpg'); // This extends from the FilesystemIterator

foreach ($files as $file) {
    // Because GlobIterator extends from FilesystemIterator, we can use the methods of the FilesystemInfo
    //echo $file->getFilename() . "\n";
}

/**
 * REGEXITERATOR
 * 
 * we chain RegexIterator to filter things by regular expression
 * 
 * Regular expression are used to match patterns in strings
 *      - The pattern is a string that defines the criteria for matching
 * 
 * /pattern/ : a regular expression
 * 
 * Patterns : 
 *          - ^ : start of string
 *          - $ : end of string
 *          - . : any character
 *          - * : zero or more
 *          - + : one or more
 *          - ? : zero or one
 *          - {n} : exactly n characters
 *          - i : case insensitive
 *          - \d : digit
 *          - \D : non digit
 *          - \w : word character
 *          - \W : non word character
 *          - \s : whitespace
 *          - \S : non whitespace
 *          - [abc] : a, b or c
 *          - [^abc] : anything except a, b or c
 *          - [a-z] : a through z
 *          - [^a-z] : anything except a through z
 *          - [a-zA-Z] : a through z or A through Z
 *          - [^a-zA-Z] : anything except a through z or A through Z
 *          - [a-zA-Z0-9] : a through z or A through Z or 0 through 9
 *          - [^a-zA-Z0-9] : anything except a through z or A through Z or 0 through 9
 *          - [a-zA-Z0-9_] : a through z or A through Z or 0 through 9 or _
 * 
 * Examples :
 *          - /^[a-zA-Z0-9_]{3,20}$/ : 3 to 20 characters long, letters, numbers or underscore
 *          - '/^.+\.php$/i : any file ending with .php'
 *          - /\.(?:jpg|png)$/i : any file ending with .jpg or .png
 */

$files = new RecursiveDirectoryIterator('.', FilesystemIterator::UNIX_PATHS);
$files = new RecursiveIteratorIterator($files, RecursiveIteratorIterator::SELF_FIRST);
$files = new RegexIterator($files, '/\.(?:jpg|png)$/i');

foreach ($files as $file) {
    //echo $file->getFilename() . "\n";
}

/**
 * SIMPLEXML TO LOAD XML AND FILTER WITH REGEXITERATOR
 */

$courses = simplexml_load_file('Exercise Files/common/data/courses.xml', 'SimpleXMLIterator');

foreach ($courses->course as $course) {
    $matches = new RegexIterator($course->author, '/joh?n peck/i');
    foreach ($matches as $match) {
        //  echo $course->title . ' with ' . $match . '(Duration: ' . $course->duration . ' )' . "\n";
    }
}

/**
 * LIMIT ITERATOR -> LIMIT THE NUMBER OF ELEMENTS
 */

$courses = simplexml_load_file('Exercise Files/common/data/courses.xml', 'SimpleXMLIterator');
$courses = new LimitIterator($courses->courses, 0, 2);

foreach ($courses as $course) {
    // echo $courses->getPosition() . '.' . $course->title . ' with ' . '(Duration: ' . $course->duration . ' )' . "\n";
}

/**
 * CallbackFilter Iterator
 */

$courses = simplexml_load_file('Exercise Files/common/data/courses.xml', 'SimpleXMLIterator');
//$courses = new CallbackFilterIterator($courses, function ($current) {
//    return $current->level == 'Intermediate';
//);



foreach ($courses as $course) {
    // echo $course->title . ' with ' . $course->author . '(Level: ' . $course->level . ' )' . "\n";
}

/**
 * FilterIterator -> This allow us to create customIterators
 * 
 * We have to create a 
 * Class AuthorFilter that extends FilterIterator {
 *      protected $author;
 * 
 *      public function __construct(Iterator $iterator, $author) {
 *         parent::__construct($iterator);
 *         $this->author = $author;
 *      }
 * 
 *      public function accept() { -> This method is called automatically by the iterator and has to return true or false
 *          return $this->current()->author == $this->author;
 *     }
 *
 * }
 */

/**
 * PARENT ITERATOR -> Is a filter that selects only elements that doesn't have childs elements
 * 
 * $dirs = new RecursiveDirectoryIterator('.', FilesystemIterator::UNIX_PATHS);
 * $dirs = new ParentIterator($dirs);
 * $dirs = new RecursiveIteratorIterator($dirs, RecursiveIteratorIterator::SELF_FIRST); -> When we chain this with parentIterator we have to pass SELF_FIRST
 * 
 */

/**
 * ARRAY ITERATOR
 */

$languages = ['php', 'java', 'python', 'c++', 'c#', 'javascript'];
// If we want to use LimitIterator with an Array we have to create a new ArrayIterator
$languages = new ArrayIterator($languages);
$languages = new LimitIterator($languages, 0, 2);
//if we want to return languajes to an array we can use
$languages = iterator_to_array($languages); // This transform back to an array but with the Filters or things that we did with the iterators

foreach ($languages as $language) {
    echo $language . "\n";
}


/**
 * Filtering values from JSON
 */

$courses = file_get_contents('Exercise Files/common/data/courses.json');
$courses = json_decode($courses); // This returns an array of anonimous objects

$courses = new ArrayIterator($courses);

/**
 * SPL DATA STRUCTURES
 */

/**
 * DOUBLY LINKED LIST -> Like a Linked List but the pointers are in both sides
 */

$doubly_linked_list = new SplDoublyLinkedList();

// ADD
$doubly_linked_list[0] = 'php';
$doubly_linked_list->push('java'); // Adds to then ends

//Last Element Inserted
$doubly_linked_list->top();
$doubly_linked_list->pop(); // Removes the last element

//First Element Inserted
$doubly_linked_list->bottom();
$doubly_linked_list->unshift('c++'); // Removes the first element

//Add element in the index
$doubly_linked_list->add(1, 'c++');
$doubly_linked_list->offsetUnset(1); // Removes the element in the index
/**
 * SPL STACK -> LAST IN, FIRST OUT
 */

$stack = new SplStack();

// ADD
$stack->push('java'); // Adds to the top of the stack
$stack->pop(); // Removes the element at the top
/**
 * SPL QUEUE -> FIRST IN, FIRST OUT
 */

$queue = new SplQueue();

//Remove first element
$queue->dequeue();

//Add new element to the end of the queue
$queue->enqueue('java');

/**
 * GLOSSARY:
 *     Globbing: Means matching file names with wildcard characters or glob patterns
 *               Main Patterns : 
 *                          - ? : Matches any single character
 *                          - * : Matches any number of characters
 *                          - [abc] : Matches one character from a selection
 *                          - [3-7] : Matches one character from a range
 *                          - [!abc] : Match one character not in a selection
 *     Traverse: Traverse a structure -> Iterate over it
 */
