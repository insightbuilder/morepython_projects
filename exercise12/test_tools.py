from unittest import TestCase
import tools as t


class Tools_Test(TestCase):
    def test_procfile_nonum(self):
        assert t.process_file_nonum("test1") == [
            "*** test1 file *** \n",
            "this is nline one on test1\n",
            "this is nline two on test 1\n",
            "**** test 1 end ***\n",
        ], t.process_file_nonum("test1")

    def test_proc_filenum(self):
        assert t.process_file_num("test1") == [
            "1 *** test1 file *** \n",
            "2 this is nline one on test1\n",
            "3 this is nline two on test 1\n",
            "4 **** test 1 end ***\n",
        ]

    def test_proc_fileeol(self):
        assert t.process_file_eol("test1") == [
            "*** test1 file *** $",
            "$",
            "this is nline one on test1$",
            "$",
            "this is nline two on test 1$",
            "$",
            "**** test 1 end ***$",
        ]

    def test_proc_fileeol_nemp(self):
        assert t.process_file_num_eol("test1") == [
            "1 *** test1 file *** $",
            "2 this is nline one on test1$",
            "3 this is nline two on test 1$",
            "4 **** test 1 end ***$",
        ]

    def test_proc_allline(self):
        assert t.process_file_allline("test1") == [
            "0 *** test1 file *** \n",
            "1 \n",
            "2 this is nline one on test1\n",
            "3 \n",
            "4 this is nline two on test 1\n",
            "5 \n",
            "6 **** test 1 end ***\n",
        ]

    def test_proc_allline_eol(self):
        assert t.process_file_allline_eol("test1") == [
            "0 *** test1 file *** $",
            "1 $",
            "2 this is nline one on test1$",
            "3 $",
            "4 this is nline two on test 1$",
            "5 $",
            "6 **** test 1 end ***$",
        ]

    def test_add_num(self):
        assert t.add_num("test1", 1) == "1 test1"

    def test_add_num_eol(self):
        assert t.add_num_eol("test1", 1) == 2
        assert t.add_num_eol("\n", 1) == 1

    def test_find_name_inpath(self):
        assert t.find_name_in_path(
            path="/home/uberdev/", obj_name="*.log", to_print=False, cliarg=False
        ) == ["/home/uberdev/jupy.log"]
        assert (
            t.find_name_in_path(
                path="/home/uberdev/", obj_name="*.log", to_print=True, cliarg=False
            )
            == []
        )
