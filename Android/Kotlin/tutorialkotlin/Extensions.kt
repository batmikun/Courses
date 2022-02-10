package com.example.tutorialkotlin

import java.util.*

fun Date?.customFormat() : string? {
    val formatter = SimpleDateFormat("dd/MM/yyyy")

    if (this != null) {
        return formatter.format(this)
    }

    return null
}

val Date?.formatSize : Int
    get() = customFormat().length ?: 0