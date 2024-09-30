// Definición de la clase Obra que representa una obra de arte
case class Obra(autor: String, año: Int, descripcion: String, tipologia: String, precio: Int)

object Museo {
  // Generar una lista que contenga todo el inventario de obras del museo
  val inventario: List[Obra] = List(
    Obra("Leonardo da Vinci", 1503, "La Mona Lisa", "pintura", 860_000_000),
    Obra("Vincent van Gogh", 1889, "La Noche Estrellada", "pintura", 100_000_000),
    Obra("Auguste Rodin", 1902, "El Pensador", "escultura", 6_000_000),
    Obra("Ernest Cline", 2011, "Ready Player One", "escritura", 1_500_000),
    Obra("Kanye West", 2010, "Runaway", "audio", 1_800_000)
  )

  // Función para formatear una obra para su impresión detallada
  def formatoObra(obra: Obra): String = {
    s"""
    |Nombre: ${obra.autor}
    |Año: ${obra.año}
    |Descripción: ${obra.descripcion}
    |Tipología: ${obra.tipologia}
    |Precio: ${obra.precio}
    |----------
    """.stripMargin
  }

  // Función para segmentar las obras según su categoría
  def porCategoria(obras: List[Obra]): Map[String, List[Obra]] = {
    obras.groupBy(_.tipologia)
  }

  // Función para encontrar la obra más costosa que tenga más de 20 años de antigüedad
  def obraCostosa(obras: List[Obra]): Option[Obra] = {
    val obrasAntiguas = obras.filter(obra => 2023 - obra.año > 20)
    obrasAntiguas.sortBy(-_.precio).headOption
  }

  // Función para calcular el patrimonio actual del museo
  def patrimonioActual(obras: List[Obra]): Int = {
    obras.map(_.precio).sum
  }

  // Función para organizar la lista por año (mayor a menor) de manera recursiva
  def ordenarEdad(obras: List[Obra]): List[Obra] = {
    if (obras.isEmpty) obras
    else {
      val pivot = obras.head
      val (before, after) = obras.tail.partition(_.año > pivot.año)
      ordenarEdad(before) ::: pivot :: ordenarEdad(after)
    }
  }

  // Función para organizar la lista por precio (menor a mayor) utilizando métodos funcionales
  def ordenarPrecio(obras: List[Obra]): List[Obra] = {
    obras.sortBy(_.precio)
  }

  // Función para aplicar un descuento del 50% a las obras de cierta categoría definida por el usuario todos los viernes
  def descuentoViernes(obras: List[Obra], dia: String, categoria: String): List[Obra] = {
    if (dia.toLowerCase == "viernes") {
      obras.map { obra =>
        if (obra.tipologia == categoria) obra.copy(precio = (obra.precio * 0.5).toInt)
        else obra
      }
    } else obras
  }

  // Función principal para ejecutar las tareas y mostrar los resultados
  def main(args: Array[String]): Unit = {
    println("Inventario segmentado por categoría:")
    porCategoria(inventario).foreach { case (categoria, obras) =>
      println(s"Categoría: $categoria")
      obras.foreach(obra => println(formatoObra(obra)))
    }

    println("Obra más costosa mayor a 20 años:")
    obraCostosa(inventario).foreach(obra => println(formatoObra(obra)))

    println("Patrimonio actual del museo:")
    println(patrimonioActual(inventario))

    println("Inventario ordenado por año (mayor a menor):")
    ordenarEdad(inventario).foreach(obra => println(formatoObra(obra)))

    println("Inventario ordenado por precio (menor a mayor):")
    ordenarPrecio(inventario).foreach(obra => println(formatoObra(obra)))

    println("Inventario con descuento en pinturas los viernes:")
    descuentoViernes(inventario, "viernes", "pintura").foreach(obra => println(formatoObra(obra)))
  }
}