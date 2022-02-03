package com.example.tutorialkotlin

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        variablesYConstantes()

        whenStatement()

        arrays()

        mapsD()

        loops()

        safetyNull()

        classes()

        enumClasses()
    }
    /*
       Es un tipo de lenguaje estatico.
    */
    private fun variablesYConstantes() {
        /*
            Los tipos de las variables son inmutables

            Para definir una variables lo hacemos con la palabra var
        */

        var myVariable: String = "Hola"

        myVariable = "Jeez"

        println(myVariable)

        /*
            Para definir una constante usamos la palabra val
        */

        val myVariableConstante = "HelloMF"

        print(myVariableConstante)
    }

    private fun whenStatement() {
        when("Cabo"){
            "Cabo" -> {
                println("Es el Cabo")
            }
            "Argentina" -> {
                println("Es Argentina")
            }
            "Pero" -> {
                println("Es Peru")
            } else -> {
                print("Ningun Pais")
            }
        }
    }

    private fun arrays() {
        /*
            Los array se definen con la funcion arrayListOf()
            Los arrays creados  son de un solo tipo
            Tambien podemos añadir un conjunto de datos todos a la vez con la funcion addAll()
            Tambien se pueden crear listas con la funcion listOf()
        */

        val name = "Nico"
        val surname = "Stirnemann"
        val age = "32"

        val myArray = arrayListOf<String>()

        myArray.add(name)
        myArray.add(surname)
        myArray.add(age)

        print(myArray)

        myArray.addAll(listOf("Hola", "Bienvenidos al Tutorial"))

        val myList: List<String> = listOf("h", "j")

        println(myList)

        myArray.forEach {
            println(it)
        }

        myArray.count()
    }

    private fun mapsD(){
        /*
            Un mapa se define con la funcion

            val myMap: Map<TypeKey, TypeValue> = mapOf("Brais" to 1, "Elena" to 2)

            Con mapOf creamos un mapa inmutable, solamente va a tener los elementos que le pasemos adentro del mapOf

            Si queremos crear un mapa mutable tenemos que usar mutableMapOf() y el tipo

            MutableMap<k,v>
         */

        val myInmutableMap: Map<String,Int> = mapOf("Brais" to 1, "Elena" to 2)

        println(myInmutableMap)

        val myMutableMap: MutableMap<String, Int> = mutableMapOf()

        myMutableMap["Brais"] = 4
        myMutableMap["Jorge"] = 3

        print(myMutableMap)
    }

    private fun loops() {
        for (x in 1..10) {
            println(x)
        }

        for (x in 1..10 step 2) {
            println(x) // De dos en dos
        }

        for (x in 0 until 10) { // Sin incluir el 10
            println(x)
        }

        for (x in 10 downTo 0) { //Cuenta regresiva
            println(x)
        }

        val myArray:List<String> = listOf("Hola", "chau", "joder")

        val myMap:MutableMap<String, Int> = mutableMapOf("Brais" to 1, "Sara" to 5)

        for (myString in myArray) {
            println(myString)
        }

        for (name in myMap) {
            println("${name.key} - ${name.value}")
        }

        var int = 10

        while(int < 20) {
            println ("Hi")
            int += 1
        }
    }

    private fun safetyNull() {
        /*
            Definimos que una variable puede ser nulla agregandole ? al final
            del tipo

            Trabajar con variables nullas es diferente a otros lenguajes
            Por ejemplo no podemos imprimir variables que puedan ser nullas
            para imprimit o trabajar con variables que pueden ser nullas, hay que
            agregarle al final !!

            Estas variables tienen metodos especiales para trabajar con ellas y no llenar
            de if comprobando si es null, estos metodos se llaman Safes Call

            Para usar safe calls tenemos que poner al final de la variable el operador
            "?" por ejemplo mySafetyString?.lenght

            O por ejemplo correr codigo cuando una variable no sea nulla con la operacion let

            mySafetyString?.let{
                println(it) // Este corre cuando no es nulla
            } ?: run {
                println(mySafetyString) // Este codigo corre cuando es nulla
            }
         */
        val miString = "NicolasStirnemann"

        // miString = null Esto daria un error de compilacion
        println(miString)

        // Variable que puede ser nulla
        val mySafetyString: String?
        mySafetyString = "Subs"
        println(mySafetyString)

        mySafetyString?.length // Si es nulla esta operacion no se ejecuta evitando el error

        mySafetyString?.let {
            println(it) // Este codigo se va a ejecutar cuando la variable no sea nulla
        } ?: run{
            println(mySafetyString) // Este codigo se va a ejecutar cuando la variable es nulla
        }

    }

    private fun classes() {
        /*
            Si no
         */
        val nico = Programmer(100000,"Nicolas", "29", arrayOf(Programmer.Languaje.Java, Programmer.Languaje.Kotlin))
        println(nico.name)
    }

    enum class Direction(val dir: Int) {
        NORTE(1),
        SUR(2),
        ESTE(3),
        OESTE(4);

        fun description(): String{
            return when(this){
                NORTE -> "La direccion es norte"
                SUR -> "La direccion es sur"
                ESTE -> "La direccion es este"
                OESTE -> "La direccion es oeste"
            }
        }
    }

    private fun enumClasses() {
        var userDirection: Direction? = null

        println("Direction: ${userDirection}")

        userDirection = Direction.NORTE

        println(userDirection)
        println("Property Value ${userDirection.name} - Index ${userDirection.ordinal}")

        println(userDirection.description()) // Esto imprime La direccion es norte

        println(userDirection.dir) // Devuelve 1
    }
}
}