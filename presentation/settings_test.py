import unittest


from settings import Settings


class SettingsTest(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_settings_default_initialization(self):
        self.assertEqual(self.settings.width, 1280)
        self.assertEqual(self.settings.height, 720)
        self.assertEqual(self.settings.bg_color, (230, 230, 230))
        self.assertEqual(self.settings.caption, Settings.CAPTION)

    def test_settings_initialization(self):
        settings = Settings(100, 200, (0, 255, 255))

        self.assertEqual(settings.width, 100)
        self.assertEqual(settings.height, 200)
        self.assertEqual(settings.bg_color, (0, 255, 255))
        self.assertEqual(settings.caption, Settings.CAPTION)


if __name__ == '__main__':
    unittest.main()
