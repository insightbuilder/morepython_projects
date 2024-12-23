from unittest import TestCase
import tools as t


class Tools_Test(TestCase):
    # def test_procfile_nonum(self):
    #     assert t.process_file_nonum("test1") == [
    #         "*** test1 file *** \n",
    #         "this is nline one on test1\n",
    #         "this is nline two on test 1\n",
    #         "**** test 1 end ***\n",
    #     ], t.process_file_nonum("test1")

    # def test_proc_filenum(self):
    #     assert t.process_file_num("test1") == [
    #         "1 *** test1 file *** \n",
    #         "2 this is nline one on test1\n",
    #         "3 this is nline two on test 1\n",
    #         "4 **** test 1 end ***\n",
    #     ]

    # def test_proc_fileeol(self):
    #     assert t.process_file_eol("test1") == [
    #         "*** test1 file *** $",
    #         "$",
    #         "this is nline one on test1$",
    #         "$",
    #         "this is nline two on test 1$",
    #         "$",
    #         "**** test 1 end ***$",
    #     ]

    # def test_proc_fileeol_nemp(self):
    #     assert t.process_file_num_eol("test1") == [
    #         "1 *** test1 file *** $",
    #         "2 this is nline one on test1$",
    #         "3 this is nline two on test 1$",
    #         "4 **** test 1 end ***$",
    #     ]

    # def test_proc_allline(self):
    #     assert t.process_file_allline("test1") == [
    #         "0 *** test1 file *** \n",
    #         "1 \n",
    #         "2 this is nline one on test1\n",
    #         "3 \n",
    #         "4 this is nline two on test 1\n",
    #         "5 \n",
    #         "6 **** test 1 end ***\n",
    #     ]

    # def test_proc_allline_eol(self):
    #     assert t.process_file_allline_eol("test1") == [
    #         "0 *** test1 file *** $",
    #         "1 $",
    #         "2 this is nline one on test1$",
    #         "3 $",
    #         "4 this is nline two on test 1$",
    #         "5 $",
    #         "6 **** test 1 end ***$",
    #     ]

    # def test_add_num(self):
    #     assert t.add_num("test1", 1) == "1 test1"

    # def test_add_num_eol(self):
    #     assert t.add_num_eol("test1", 1) == 2
    #     assert t.add_num_eol("\n", 1) == 1

    # def test_find_name_inpath(self):
    #     assert t.find_name_in_path(
    #         path="/home/uberdev/", obj_name="*.log", to_print=False, cliarg=False
    #     ) == ["/home/uberdev/jupy.log"]
    #     assert (
    #         t.find_name_in_path(
    #             path="/home/uberdev/", obj_name="*.log", to_print=True, cliarg=False
    #         )
    #         == []
    #     )

    # def test_fp_matcher(self):
    #     assert t.file_pattern_matcher(file_pattern="*1", search_pattern="nline") == [
    #         "nline",
    #         "nline",
    #     ], "work on output"  # t.file_pattern_matcher(file_pattern="test*", search_pattern="nline")

    # def test_parse_file(self):
    #     assert t.parse_file(file_name="cut_me", delim=" ", sections="1-2") == [
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["-rwxrwxrwx"],
    #         ["-rwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #         ["drwxrwxrwx"],
    #     ]
    #     # with self.assertRaises(Exception) as ctx:
    #     #     t.parse_file(file_name="cut_me", delim=" ", sections="1-a2")
    #     # self.assertEqual(
    #     #     str(ctx.exception), "invalid literal for int() with base 10: 'a2'"
    #     # )
    #     assert (
    #         t.parse_file(file_name="cut_me", delim=" ", sections="1-a2")
    #         == "There is issue in args"
    #     )

    def test_process_line_sed(self):
        line = "there is more than meets the eyes"
        expr = "meet"
        tgt = "cheks"
        assert t.process_line(line, expr, tgt) == "there is more than chekss the eyes"

    def test_pfile_sed(self):
        assert t.parse_file_sed(
            file_name="/home/uberdev/jupy.log",
            expr="s\\ServerApp\\Client\\g",
            output=True,
        ) == [
            "[I 2024-11-15 14:04:20.900 Client] jupyter_lsp | extension was successfully linked.\n",
            "I 2024-11-15 21:27:02.659 Client] Starting buffering for c42bcf16-06f6-4aab-85a3-7855cde3afe8:6aec2cbd-bd2f-424c-b7c1-9c607d8a7a2d\n",
        ]
