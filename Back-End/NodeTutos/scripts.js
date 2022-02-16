class Person {

}

Person.prototype.constructor = (firstname, lastname) => {
    this.firstname = firstname
    this.lastname = lastname
  }
  
Object.defineProperties(Person,{
    'name': {
        writable: true,
        value : `Hola`,
    }
});

let person1 = new Person('Nico', 'Jimenes')

console.log(person1.firstname);