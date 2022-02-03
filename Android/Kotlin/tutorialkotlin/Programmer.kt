package com.example.tutorialkotlin

class Programmer(id:Int, val name: String, val age: String, val languages: Array<Languaje>, val programmer: Array<Programmer>? = null) {
    /*
        Entre parentesis se define el "constructor" de la clase

        Como esta en este momento las variables solamente pueden ser usadas dentro
        de la propia clase

        Para poder usarlas en alguna clase externa, tenemos que agregarle val o var
        al principio de los parametros
     */

    val variable: String? = null

    public enum class Languaje{
        Kotlin,
        Java,
        PHP
    }
}