import unittest
from jeuxdepong import votre_fonction  # Remplacez 'votre_fonction' par la fonction à tester

class TestJeuxDePong(unittest.TestCase):
    def test_cas_utilisation_principal(self):
        self.assertEqual(votre_fonction(paramètre), résultat_attendu)  # Remplacez avec vos paramètres et résultats

    def test_scénario_erreur(self):
        with self.assertRaises(Exception):  # Remplacez 'Exception' par l'exception attendue
            votre_fonction(paramètre_invalide)  # Remplacez avec un paramètre invalide

if __name__ == '__main__':
    unittest.main()