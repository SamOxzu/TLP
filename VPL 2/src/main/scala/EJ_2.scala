object MCD {
  // Función recursiva para hallar el MCD de dos números mediante Euclides
  def mcd(a: Int, b: Int): Int = {
    if (b == 0) a else mcd(b, a % b)
  }

  // Main para ejecutar un ejemplo de la función
  def main(args: Array[String]): Unit = {
    val n1 = 56
    val n2 = 98
    val res = mcd(n1, n2)
    println(s"El MCD de $n1 y $n2 es: $res")
  }  
}