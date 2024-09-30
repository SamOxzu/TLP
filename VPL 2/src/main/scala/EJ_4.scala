object Segmentador {
  // Main para caso de ejemplo
  def main(args: Array[String]): Unit = {
    // Lista con Strings
    val lista = List(
      // Entradas válidas
      "samgutierrezsa@unal.edu.co",
      "123-456-34-55",
      "Cra 12 # 34-5",
      "oxzutiramisu@gmail.com",
      "654-321-55-43",
      "Cll 12 # 45-6",
      "ficonorrea@med.gov.co",
      // Entradas inválidas
      "gates@hotmail.com", // Dominio inválido
      "zapataunal.edu.co", // Falta el @
      "999-999-99-99", // X = 9, Y = 9
      "Cll 654 # 32-1", // XXX
      "Av. 69 # 42-0" // Av no soportada 
    )

    // Segmentación
    val (correos, celulares, direcciones) = segmentarDatos(lista)
    
    // Imprimir por consola
    println("Correos Electrónicos:")
    println(correos.mkString("\n"))
    println("----------")
    
    println("Números Celulares:")
    println(celulares.mkString("\n"))
    println("----------")
    
    println("Direcciones:")
    println(direcciones.mkString("\n"))
  }

  // Función para segmentar los datos
  def segmentarDatos(lista: List[String]): (List[String], List[String], List[String]) = {
    // Formato de Correos Electrónicos
    val correoRegex = "^[a-zA-Z0-9.]+@(gmail\\.com|unal\\.edu\\.co|med\\.gov\\.co)$".r
    // Formato de Números de Celular
    val celularRegex = "^[0-7]{3}-[0-7]{3}-[3-5]{2}-[3-5]{2}$".r
    // Formato de Direcciones
    val direccionRegex = "^(Cra|Cll) [0-9]{1,2} # [0-9]{1,2}-[0-9]{1}$".r

    // Asignaciones de Filtrado
    val correos = lista.filter {
      case correoRegex(_*) => true
      case _ => false
    }

    val celulares = lista.filter {
      case celularRegex(_*) => true
      case _ => false
    }

    val direcciones = lista.filter {
      case direccionRegex(_*) => true
      case _ => false
    }

    (correos, celulares, direcciones)
  }
}