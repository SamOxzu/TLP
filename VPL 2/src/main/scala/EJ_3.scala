object Distancia {
  // Función de orden superior para calcular la distancia máxima
  def maxDistancia(puntos: List[(Int, Int)], distancia: ((Int, Int), (Int, Int)) => Double): Double = {
    var maxDist = 0.0
    for (i <- puntos.indices) {
      for (j <- i + 1 until puntos.length) {
        val dist = distancia(puntos(i), puntos(j))
        if (dist > maxDist) {
          maxDist = dist
        }
      }
    }
    maxDist
  }

  // Función para calcular la distancia
  def distancia(p1: (Int, Int), p2: (Int, Int)): Double = {
    math.sqrt(math.pow(p2._1 - p1._1, 2) + math.pow(p2._2 - p1._2, 2))
  }

  // Main para ejemplo de uso
  def main(args: Array[String]): Unit = {
    val puntos = List((3, 5), (7, 3), (-5, -8))
    val maxDist = maxDistancia(puntos, distancia)
    println(s"La distancia máxima es: $maxDist")
  }
}