# python -m unittest test_EJ_2.py
import unittest
from unittest.mock import patch
from io import StringIO
from EJ_2 import Oxzutify

class TestOxzutify(unittest.TestCase):

    def setUp(self):
        self.service = Oxzutify()

    # Test Caso de Uso 1: Reproducir por artista
    # Se simulan las entradas de manera que el usuario reproduce las canciones de Kanye West.
    @patch('builtins.input', side_effect=[1,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_by_artist(self, mock_stdout, mock_input):
        self.service.play_by_artist()
        output = mock_stdout.getvalue()
        self.assertIn("--- Lista de Artistas ---", output)
        self.assertIn("1. Kanye West", output)
        self.assertIn("--- Reproduciendo canciones de Kanye West ---", output)
        self.assertIn("- Stronger", output)

    # Test Caso de Uso 2: Reproducir por álbum
    # Se simulan las entradas de manera que el usuario reproduce las canciones del álbum Madvilliany de MF DOOM.
    @patch('builtins.input', side_effect=[3,2,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_by_album(self, mock_stdout, mock_input):
        self.service.play_by_album()
        output = mock_stdout.getvalue()
        self.assertIn("--- Lista de Artistas ---", output)
        self.assertIn("3. MF DOOM", output)
        self.assertIn("--- Álbumes de MF DOOM ---", output)
        self.assertIn("2. Madvillainy", output)
        self.assertIn("--- Reproduciendo canciones del álbum Madvillainy de MF DOOM ---", output)
        self.assertIn("- Figaro", output)

    # Test Caso de Uso 3: Reproducir por canción
    # Se simulan las entradas de manera que el usuario reproduce la canción
    # Everybody Dies in Their Nightmares del álbum 17 de XXXTENTACION.
    @patch('builtins.input', side_effect=[5,1,2,0,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_by_song(self, mock_stdout, mock_input):
        self.service.play_by_song()
        output = mock_stdout.getvalue()
        self.assertIn("--- Lista de Artistas ---", output)
        self.assertIn("5. XXXTentacion", output)
        self.assertIn("--- Álbumes de XXXTentacion ---", output)
        self.assertIn("1. 17", output)
        self.assertIn("--- Canciones del álbum 17 de XXXTentacion ---", output)
        self.assertIn("2. Everybody Dies in Their Nightmares", output)
        self.assertIn("--- Reproduciendo Everybody Dies in Their Nightmares de XXXTentacion del álbum 17 ---", output)


    # Tests Relacionados a Entradas Inválidas
    # Test 1: El usuario elige un artista que no existe.
    @patch('builtins.input', side_effect=[10,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_artist(self, mock_stdout, mock_input):
        self.service.play_by_artist()
        output = mock_stdout.getvalue()
        self.assertIn("Opción no encontrada.", output)
    
    # Test 1.5: El usuario no ingresa un entero en la opción de artista.
    @patch('builtins.input', side_effect=["a",0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_artist_input(self, mock_stdout, mock_input):
        self.service.play_by_artist()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada no válida. Por favor, ingresa un número.", output)
                      
    # Test 2: El usuario elige un álbum que no existe.
    @patch('builtins.input', side_effect=[1,10,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_album(self, mock_stdout, mock_input):
        self.service.play_by_album()
        output = mock_stdout.getvalue()
        self.assertIn("Opción no encontrada.", output)
    
    # Test 2.5: El usuario no ingresa un entero en la opción de álbum.
    @patch('builtins.input', side_effect=[1,"a",0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_album_input(self, mock_stdout, mock_input):
        self.service.play_by_album()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada no válida. Por favor, ingresa un número.", output)
    
    # Test 3: El usuario elige una canción que no existe.
    @patch('builtins.input', side_effect=[1,1,10,0,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_song(self, mock_stdout, mock_input):
        self.service.play_by_song()
        output = mock_stdout.getvalue()
        self.assertIn("Opción no encontrada.", output)
    
    # Test 3.5: El usuario no ingresa un entero en la opción de canción.
    @patch('builtins.input', side_effect=[1,1,"a",0,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_song_input(self, mock_stdout, mock_input):
        self.service.play_by_song()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada no válida. Por favor, ingresa un número.", output)
    
    # Test 4: El usuario elige una opción inválida en el menú principal.
    @patch('builtins.input', side_effect=["5","4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout, mock_input):
        self.service.main()
        output = mock_stdout.getvalue()
        self.assertIn("Oxzutify", output)
        self.assertIn("1. Reproducir por Artista", output)
        self.assertIn("4. Salir", output)
        self.assertIn("Opción no válida. Por favor, intenta de nuevo.", output)
    

    #Test Relacionados a Entradas Vacías
    # Test 1: El usuario no ingresa un artista.
    @patch('builtins.input', side_effect=['',0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_artist(self, mock_stdout, mock_input):
        self.service.play_by_artist()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada vacía. Por favor, intenta de nuevo.", output)
    
    # Test 2: El usuario no ingresa un álbum.
    @patch('builtins.input', side_effect=[1,'',0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_album(self, mock_stdout, mock_input):
        self.service.play_by_album()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada vacía. Por favor, intenta de nuevo.", output)
    
    # Test 3: El usuario no ingresa una canción.
    @patch('builtins.input', side_effect=[1,1,'',0,0,0])
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_song(self, mock_stdout, mock_input):
        self.service.play_by_song()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada vacía. Por favor, intenta de nuevo.", output)
    
    # Test 4: El usuario no ingresa una opción en el menú principal.
    @patch('builtins.input', side_effect=['',"4"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_choice(self, mock_stdout, mock_input):
        self.service.main()
        output = mock_stdout.getvalue()
        self.assertIn("Entrada vacía. Por favor, intenta de nuevo.", output)

if __name__ == '__main__':
    unittest.main()