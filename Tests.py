import unittest
import WallhavenApi
import os


class TestClassInitLogin(unittest.TestCase):
    def test_class_init_login(self):
        wa = WallhavenApi.WallhavenApi(username='cufocufoma', password="cufocufoma@lackmail.ru")
        self.assertTrue(wa.logged_in)

class TestClassLogin(unittest.TestCase):
    def test_class_login(self):
        wa = WallhavenApi.WallhavenApi()
        self.assertTrue(wa.login(username='cufocufoma', password="cufocufoma@lackmail.ru"))


class TestLoggedUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wa = WallhavenApi.WallhavenApi(username='cufocufoma', password="cufocufoma@lackmail.ru")

    def test_login(self):
        self.assertTrue(self.wa.login())

    def test_logout(self):
        self.assertTrue(self.wa.logout())
        self.wa.login()

    def test_get_pages_count(self):
        self.assertIsNotNone(self.wa.get_pages_count())

    def test_get_image_uploader(self):
        uploader = self.wa.get_image_uploader("329194")
        self.assertIsNotNone(uploader["Username"])
        self.assertIsNotNone(uploader["Avatar"]["32"])
        self.assertIsNotNone(uploader["Avatar"]["200"])

    def test_get_image_category(self):
        self.assertIsNotNone(self.wa.get_image_category("329194"))

    def test_get_image_short_url(self):
        self.assertIsNotNone(self.wa.get_image_short_url("329194"))

    def test_get_image_upload_time(self):
        self.assertIsNotNone(self.wa.get_image_upload_time("329194"))

    def test_get_image_ratio(self):
        self.assertIsNotNone(self.wa.get_image_ratio("329194"))

    def test_get_image_resolution(self):
        self.assertIsNotNone(self.wa.get_image_resolution("329194"))

    def test_get_image_colors(self):
        self.assertTrue(len(self.wa.get_image_colors("329194")) > 0)

    def test_get_image_favorites(self):
        self.assertIsNotNone(self.wa.get_image_favorites("329194"))

    def test_get_image_url(self):
        self.assertIsNotNone(self.wa.get_image_url("329194"))

    def test_get_image_size(self):
        self.assertIsNotNone(self.wa.get_image_size("329194"))

    def test_get_image_purity(self):
        self.assertIsNotNone(self.wa.get_image_purity("329194"))

    def test_get_image_views(self):
        self.assertIsNotNone(self.wa.get_image_views("329194"))

    def test_get_image_tags_ex(self):
        self.assertTrue(len(self.wa.get_image_tags_ex("329194")) > 0)

    def test_get_image_data(self):
        data = self.wa.get_image_data("329194")

        self.assertIn("Category", data)
        self.assertIsNotNone(data["Category"])
        self.assertEqual(data["Category"], self.wa.get_image_category("329194"))

        self.assertIn("ShortUrl", data)
        self.assertIsNotNone(data["ShortUrl"])
        self.assertEqual(data["ShortUrl"], self.wa.get_image_short_url("329194"))

        self.assertIn("UploadTime", data)
        self.assertIsNotNone(data["UploadTime"])
        self.assertEqual(data["UploadTime"], self.wa.get_image_upload_time("329194"))

        self.assertIn("Ratio", data)
        self.assertIsNotNone(data["Ratio"])
        self.assertEqual(data["Ratio"], self.wa.get_image_ratio("329194"))

        self.assertIn("Resolution", data)
        self.assertIsNotNone(data["Resolution"])
        self.assertEqual(data["Resolution"], self.wa.get_image_resolution("329194"))

        self.assertIn("ImageColors", data)
        self.assertIsNotNone(data["ImageColors"])
        self.assertSequenceEqual(data["ImageColors"], self.wa.get_image_colors("329194"))

        self.assertIn("Favorites", data)
        self.assertIsNotNone(data["Favorites"])
        self.assertEqual(data["Favorites"], self.wa.get_image_favorites("329194"))

        self.assertIn("ImageUrl", data)
        self.assertIsNotNone(data["ImageUrl"])
        self.assertEqual(data["ImageUrl"], self.wa.get_image_url("329194"))

        self.assertIn("Size", data)
        self.assertIsNotNone(data["Size"])
        self.assertEqual(data["Size"], self.wa.get_image_size("329194"))

        self.assertIn("Purity", data)
        self.assertIsNotNone(data["Purity"])
        self.assertEqual(data["Purity"], self.wa.get_image_purity("329194"))

        self.assertIn("Views", data)
        self.assertIsNotNone(data["Views"])
        self.assertEqual(data["Views"], self.wa.get_image_views("329194"))

        self.assertIn("TagsEx", data)
        self.assertIsNotNone(data["TagsEx"])

        tags_ex = sorted(self.wa.get_image_tags_ex("329194"), key=lambda k: k['Id'])
        data["TagsEx"] = sorted(data["TagsEx"], key=lambda k: k['Id'])
        self.assertEqual(len(tags_ex), len(data["TagsEx"]))
        for i in range(0, len(tags_ex)):
            self.assertDictEqual(tags_ex[i], data["TagsEx"][i])

    def test_get_get_images_numbers(self):
        self.assertGreater(len(self.wa.get_images_numbers()), 0)

    def test_download_image(self):
        self.assertTrue(self.wa.download_image("329194", "tempfile.jpg"))
        os.remove("tempfile.jpg")

    def test_get_image_puruty_nsfw(self):
        self.assertIsNotNone(self.wa.get_image_purity("166969"))

    def test_image_tag_actions(self):
        image_numbers = self.wa.get_images_numbers(sorting="random")
        self.assertGreater(len(image_numbers), 0)
        tags = self.wa.get_image_tags_ex(image_numbers[0])
        if len(tags):
            self.assertTrue(self.wa.image_tag_delete(image_numbers[0], tags[0]["Id"]))
            self.assertTrue(self.wa.image_tag_add(image_numbers[0], tags[0]["Name"]))
        else:
            self.assertTrue(False)

    def test_image_change_purity(self):
        image_numbers = self.wa.get_images_numbers(sorting="random")
        self.assertGreater(len(image_numbers), 0)
        purity = self.wa.get_image_purity(image_numbers[0])
        self.assertIsNotNone(purity)
        purity = str(purity).lower()
        self.assertTrue(self.wa.image_change_purity(image_numbers[0], list({"sfw", "sketchy", "nsfw"} - {purity})[0]))
        self.assertTrue(self.wa.image_change_purity(image_numbers[0], purity))

    def test_image_change_purity_wrong_purity(self):
        self.assertFalse(self.wa.image_change_purity("1111", "wrong"))

    def test_is_image_exists(self):
        image_numbers = self.wa.get_images_numbers(sorting="random")
        self.assertGreater(len(image_numbers), 0)
        self.wa.is_image_exists(image_numbers[0])

    def test_get_collections(self):
        collections = self.wa.get_collections()
        self.assertGreater(len(collections), 0)
        self.assertTrue('collection_name' in collections[0])
        self.assertTrue('collection_id' in collections[0])
        self.assertTrue(isinstance(collections[0]['collection_name'], str))
        self.assertTrue(isinstance(collections[0]['collection_id'], str))

    def test_add_rm_user_collections(self):
        new_collection_name = 'test'
        orig_collections = self.wa.get_collections()

        # ensure that the a collection of the same name doesn't already exist
        for c in orig_collections:
            if c['collection_name'] == new_collection_name:
                self.assertTrue(self.wa.delete_collection_by_id(c['collection_id']))

        # add new collection
        self.assertTrue(self.wa.add_collection(new_collection_name))

        # check collection was added
        collections = self.wa.get_collections()
        new_collection_found = False
        new_collection_id = None
        for c in collections:
            if c['collection_name'] == new_collection_name:
                new_collection_found = True
                new_collection_id = c['collection_id']
                break

        self.assertTrue(new_collection_found)

        # delete new collection
        self.assertTrue(self.wa.delete_collection_by_id(new_collection_id))

        # ensure that collection was deleted
        new_collection_found = False
        collections = self.wa.get_collections()
        for c in collections:
            if c['collection_name'] == new_collection_name:
                new_collection_found = True
                break

        self.assertFalse(new_collection_found)

    def test_get_add_rm_favorite_image(self):
        fav_image = "329194"
        # ensure that image is not in any of the user collections
        collections = self.wa.get_collections()
        for c in collections:
            c_id = c['collection_id']
            fav_ids = self.wa.get_images_numbers_from_user_collection_by_id(c_id)
            if fav_image in fav_ids:
                self.wa.image_remove_from_favorites(fav_image, double_check=False)

        # work with the default collection
        default_collection_id = collections[0]['collection_id']
        orig_fav_ids = self.wa.get_images_numbers_from_user_favorites()
        
        # add image to favorites and check that it appears
        self.assertTrue(self.wa.image_add_to_collection(fav_image, default_collection_id))
        new_fav_ids = self.wa.get_images_numbers_from_user_favorites()
        for image_ID in orig_fav_ids:
            new_fav_ids.remove(image_ID)
        self.assertEqual(len(new_fav_ids), 1)
        self.assertEqual(new_fav_ids[0], fav_image)

        # remove image from all collections and double check that it has 
        # gone from default collection.
        self.assertTrue(self.wa.image_remove_from_favorites(fav_image, double_check=True))


class TestAnonymousUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wa = WallhavenApi.WallhavenApi()

    def test_image_tag_delete(self):
        self.assertFalse(self.wa.image_tag_delete("1111", "1111"))

    def test_image_tag_add(self):
        self.assertFalse(self.wa.image_tag_add("1111", "1111"))

    def test_image_change_purity(self):
        self.assertFalse(self.wa.image_change_purity("1111", "swf"))

if __name__ == '__main__':
    unittest.main()