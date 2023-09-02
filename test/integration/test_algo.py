import pytest
import logging

log = logging.getLogger(__name__)

CUCMD = {"cmd":"./unit_test_cu -t RPC"}

ERCMD = {"cmd":"./unit_test_er -t RPC"}


class TestExec:

    BFSEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/bfs_embed ./testdb",
        "result" : ["found_vertices = 3829"]
    }

    IMPORTOPT = {
        "cmd" : "./lgraph_import -c ./data/algo/fb.conf -d ./testdb --overwrite 1",
        "cleanup_dir" : ["./testdb", "./.import_tmp"]
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [BFSEMBEDOPT], indirect=True)
    def test_exec_bfs_embed(self, importor, algo):
        pass


    BFSSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/bfs_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : ["found_vertices = 3829"]
    }

    @pytest.mark.parametrize("algo", [BFSSTANDOPT], indirect=True)
    def test_exec_bfs_standalone(self, algo):
        pass

    BFSIDMAPPING = {
        "cmd" : "OMP_NUM_THREADS=6 algo/bfs_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 1 --root 0a",
        "result" : ["found_vertices = 3829"]
    }

    @pytest.mark.parametrize("algo", [BFSIDMAPPING], indirect=True)
    def test_exec_bfs_idmapping_standalone(self, algo):
        pass

    BFSNOIDMAPPING = {
        "cmd" : "OMP_NUM_THREADS=6 algo/bfs_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 0 --root 0a",
        "result" : ["found_vertices = 3829"]
    }
    @pytest.mark.parametrize("algo", [BFSNOIDMAPPING], indirect=True)
    @pytest.mark.xfail(reason="need id mapping")
    def test_exec_bfs_without_idmapping_standalone(self, algo):
        pass

    BFSPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py bfs ./testdb",
        "result" : ['''"found_vertices": 3829''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [BFSPYTHONEMBEDOPT], indirect=True)
    def test_exec_bfs_python_embed(self, importor, algo):
        pass

    BFSPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py bfs ./data/algo/fb_weighted",
        "result" : ["found_vertices = 3829"]
    }
    @pytest.mark.parametrize("algo", [BFSPYTHONSTANDOPT], indirect=True)
    def test_exec_bfs_python_standalone(self, algo):
        pass


    PGEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/pagerank_embed ./testdb",
        "result" : [" pr[1911] = 0.009418"]
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [PGEMBEDOPT], indirect=True)
    def test_exec_pagerank_embed(self, importor, algo):
        pass


    PGSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/pagerank_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : [" pr[1911] = 0.009418"]
    }
    @pytest.mark.parametrize("algo", [PGSTANDOPT], indirect=True)
    def test_exec_pagerank_standalone(self, algo):
        pass

    PGIDMAPPINGSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/pagerank_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 1",
        "result" : [" pr[1911a] = 0.009418"]
    }
    @pytest.mark.parametrize("algo", [PGIDMAPPINGSTANDOPT], indirect=True)
    def test_exec_idmapping_pagerank_standalone(self, algo):
        pass

    PGNOIDMAPPINGSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/pagerank_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 0",
        "result" : [" pr[1911a] = 0.009418"]
    }
    @pytest.mark.parametrize("algo", [PGNOIDMAPPINGSTANDOPT], indirect=True)
    @pytest.mark.xfail(reason="need id mapping")
    def test_exec_without_idmapping_pagerank_standalone(self, algo):
        pass

    PGPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py pagerank ./testdb",
        "result" : ['''"max_pr": 0.009418''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [PGPYTHONEMBEDOPT], indirect=True)
    def test_exec_pagerank_python_embed(self, importor, algo):
        pass

    PGPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py pagerank ./data/algo/fb_weighted",
        "result" : ["pr[1911] = 0.009418"]
    }
    @pytest.mark.parametrize("algo", [PGPYTHONSTANDOPT], indirect=True)
    def test_exec_pagerank_python_standalone(self, algo):
        pass

    SSSPEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/sssp_embed ./testdb",
        "result" : ["]=5"]
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [SSSPEMBEDOPT], indirect=True)
    def test_exec_sssp_embed(self, importor, algo):
        pass


    SSSPSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/sssp_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : ["]=5"]
    }
    @pytest.mark.parametrize("algo", [SSSPSTANDOPT], indirect=True)
    def test_exec_sssp_standalone(self, algo):
        pass

    SSSPIDMAPPING = {
        "cmd" : "OMP_NUM_THREADS=6 algo/sssp_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 1 --root 0a",
        "result" : ["]=5"]
    }

    @pytest.mark.parametrize("algo", [SSSPIDMAPPING], indirect=True)
    def test_exec_sssp_idmapping_standalone(self, algo):
        pass

    SSSPNOIDMAPPING = {
        "cmd" : "OMP_NUM_THREADS=6 algo/sssp_standalone --type text --input_dir ./data/algo/fb_str_weighted --id_mapping 0 --root 0a",
        "result" : ["]=5"]
    }
    @pytest.mark.parametrize("algo", [SSSPNOIDMAPPING], indirect=True)
    @pytest.mark.xfail(reason="need id mapping")
    def test_exec_sssp_without_idmapping_standalone(self, algo):
        pass

    SSSPPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py sssp ./testdb",
        "result" : ['''"max_distance": 5''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [SSSPPYTHONEMBEDOPT], indirect=True)
    def test_exec_sssp_python_embed(self, importor, algo):
        pass

    SSSPPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py sssp ./data/algo/fb_weighted",
        "result" : ["] = 5"]
    }
    @pytest.mark.parametrize("algo", [SSSPPYTHONSTANDOPT], indirect=True)
    def test_exec_sssp_python_standalone(self, algo):
        pass

    WCCEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/wcc_embed ./testdb",
        "result" : ['''"max_component":4039,"num_components":1''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [WCCEMBEDOPT], indirect=True)
    def test_exec_wcc_embed(self, importor, algo):
        pass


    WCCSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/wcc_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : ["max_component = 4039", "num_components = 1"]
    }
    @pytest.mark.parametrize("algo", [WCCSTANDOPT], indirect=True)
    def test_exec_wcc_standalone(self, algo):
        pass

    WCCPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py wcc ./testdb",
        "result" : ['''"max_component": 4039''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [WCCPYTHONEMBEDOPT], indirect=True)
    def test_exec_wcc_python_embed(self, importor, algo):
        pass

    WCCPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py wcc ./data/algo/fb_weighted",
        "result" : ["max_component = 4039", "num_components = 1"]
    }
    @pytest.mark.parametrize("algo", [WCCPYTHONSTANDOPT], indirect=True)
    def test_exec_wcc_python_standalone(self, algo):
        pass

    LCCEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/lcc_embed ./testdb",
        "result" : ['''"average_lcc":0.60554''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [LCCEMBEDOPT], indirect=True)
    def test_exec_lcc_embed(self, importor, algo):
        pass

    LCCSTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/lcc_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : ["average_lcc is: 0.60554"]
    }
    @pytest.mark.parametrize("algo", [LCCSTANDOPT], indirect=True)
    def test_exec_lcc_standalone(self, algo):
        pass

    LCCPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py lcc ./testdb",
        "result" : ['''"average_lcc": 0.60554''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [LCCPYTHONEMBEDOPT], indirect=True)
    def test_exec_lcc_python_embed(self, importor, algo):
        pass

    LCCPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py lcc ./data/algo/fb_weighted",
        "result" : ["average_lcc = 0.60554"]
    }
    @pytest.mark.parametrize("algo", [LCCPYTHONSTANDOPT], indirect=True)
    def test_exec_lcc_python_standalone(self, algo):
        pass


    LPAEMBEDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/lpa_embed ./testdb",
        "result" : ['''"modularity":0.770773''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [LPAEMBEDOPT], indirect=True)
    def test_exec_lpa_embed(self, importor, algo):
        pass

    LPASTANDOPT = {
        "cmd" : "OMP_NUM_THREADS=6 algo/lpa_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result" : ["modularity: 0.770773"]
    }
    @pytest.mark.parametrize("algo", [LPASTANDOPT], indirect=True)
    def test_exec_lpa_standalone(self, algo):
        pass

    LPAPYTHONEMBEDOPT = {
        "cmd": "python3 python_embed.py lpa ./testdb",
        "result" : ['''"max_community": 1015''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [LPAPYTHONEMBEDOPT], indirect=True)
    def test_exec_lpa_python_embed(self, importor, algo):
        pass

    LPAPYTHONSTANDOPT = {
        "cmd": "python3 python_standalone.py lpa ./data/algo/fb_weighted",
        "result" : ["max_community = 1015"]
    }
    @pytest.mark.parametrize("algo", [LPAPYTHONSTANDOPT], indirect=True)
    def test_exec_lpa_python_standalone(self, algo):
        pass



    KHOPKTH = {
        "cmd" : "OMP_NUM_THREADS=6 algo/khop_kth_embed ./testdb",
        "result" : ['''"size":3168''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [KHOPKTH], indirect=True)
    def test_exec_khopkth_embed(self, importor, algo):
        pass

    KHOPWITHIN = {
        "cmd" : "OMP_NUM_THREADS=6 algo/khop_within_embed ./testdb",
        "result" : ['''"size":3259''']
    }
    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [KHOPWITHIN], indirect=True)
    def test_exec_khopwithin_embed(self, importor, algo):
        pass

    BCEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/bc_embed ./testdb",
        "result": ['''"max_score":1.0,"max_score_vid":1465''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [BCEMBEDOPT], indirect=True)
    def test_exec_bc_embed(self, importor, algo):
        pass

    BCSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/bc_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["max score is: score[1465]=1"]
    }

    @pytest.mark.parametrize("algo", [BCSTANDOPT], indirect=True)
    def test_exec_bc_standalone(self, algo):
        pass

    CNEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/cn_embed ./testdb",
        "result": ['''"cn_list":[[0,1,16.0],[1,2,1.0]]''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [CNEMBEDOPT], indirect=True)
    def test_exec_cn_embed(self, importor, algo):
        pass

    CNSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/cn_standalone --type text --input_dir ./data/algo/fb_weighted --search_dir ./data/algo/search_dir/ --make_symmetric 1",
        "result": ["cn(0,1) = 16", "cn(1,2) = 1", "cn(1,100) = 2", "cn(1,972) = 0", "cn(101,202) = 1"]
    }

    @pytest.mark.parametrize("algo", [CNSTANDOPT], indirect=True)
    def test_exec_cn_standalone(self, algo):
        pass

    DCEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/dc_embed ./testdb",
        "result": ['''"graph_dc":1.92524''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [DCEMBEDOPT], indirect=True)
    def test_exec_dc_embed(self, importor, algo):
        pass

    DCSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/dc_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["graph_dc:1.92524"]
    }

    @pytest.mark.parametrize("algo", [DCSTANDOPT], indirect=True)
    def test_exec_dc_standalone(self, algo):
        pass

    DEEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/de_embed ./testdb",
        "result": ['''"max_diamension":9''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [DEEMBEDOPT], indirect=True)
    def test_exec_de_embed(self, importor, algo):
        pass

    DESTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/de_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["max_diamension:9"]
    }

    @pytest.mark.parametrize("algo", [DESTANDOPT], indirect=True)
    def test_exec_de_standalone(self, algo):
        pass

    ENEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/en_embed ./testdb",
        "result": ['''"num_reachable_vertices":348''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [ENEMBEDOPT], indirect=True)
    def test_exec_en_embed(self, importor, algo):
        pass

    ENSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/en_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["num_reachable_vertices:348"]
    }

    @pytest.mark.parametrize("algo", [ENSTANDOPT], indirect=True)
    def test_exec_en_standalone(self, algo):
        pass

    FASTTRIANGLEEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/fast_triangle_counting_embed ./testdb",
        "result": ['''"discovered_triangles":1612010''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [FASTTRIANGLEEMBEDOPT], indirect=True)
    def test_exec_fast_triangle_embed(self, importor, algo):
        pass

    FASTTRIANGLESTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/fast_triangle_counting_standalone --type text --input_dir ./data/algo/fb_unweighted --make_symmetric 1",
        "result": ["discovered 1612010 triangles"]
    }

    @pytest.mark.parametrize("algo", [FASTTRIANGLESTANDOPT], indirect=True)
    def test_exec_fast_triangle_standalone(self, algo):
        pass

    HITSEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/hits_embed ./testdb",
        "result": ["max authority value is authority[2604] = 0.11527", "max hub value is hub[1912] = 0.13993"]
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [HITSEMBEDOPT], indirect=True)
    def test_exec_hits_embed(self, importor, algo):
        pass

    HITSSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/hits_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["max authority value is authority[2604] = 0.11527", "max hub value is hub[1912] = 0.13993"]
    }

    @pytest.mark.parametrize("algo", [HITSSTANDOPT], indirect=True)
    def test_exec_hits_standalone(self, algo):
        pass

    JIEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/ji_embed ./testdb",
        "result": ['''"ji_list":[[0,1,0.04597701149425287],[1,2,0.038461538461538464]]''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [JIEMBEDOPT], indirect=True)
    def test_exec_ji_embed(self, importor, algo):
        pass

    JISTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/ji_standalone --type text --input_dir ./data/algo/fb_weighted --search_dir ./data/algo/search_dir/ --make_symmetric 1",
        "result": ["ji(0,1) = 0.045977", "ji(1,2) = 0.03846", "ji(1,100) = 0.08333", "ji(1,972) = 0.00000",
                   "ji(101,202) = 0.04545"]
    }

    @pytest.mark.parametrize("algo", [JISTANDOPT], indirect=True)
    def test_exec_ji_standalone(self, algo):
        pass

    LOUVAINEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/louvain_embed ./testdb",
        "result": ['''"modularity":0.83''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [LOUVAINEMBEDOPT], indirect=True)
    def test_exec_louvain_embed(self, importor, algo):
        pass

    LOUVAINSTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/louvain_standalone --type text --input_dir ./data/algo/fb_weighted",
        "result": ["Q = 0.83"]
    }

    @pytest.mark.parametrize("algo", [LOUVAINSTANDOPT], indirect=True)
    def test_exec_louvain_standalone(self, algo):
        pass

    KCOREEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/kcore_embed ./testdb",
        "result": ['''"num_result_vertices":2987''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [KCOREEMBEDOPT], indirect=True)
    def test_exec_kcore_embed(self, importor, algo):
        pass

    KCORESTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/kcore_standalone --type text --input_dir ./data/algo/fb_weighted --make_symmetric 1",
        "result": ["number of 10-core vertices: 2987"]
    }

    @pytest.mark.parametrize("algo", [KCORESTANDOPT], indirect=True)
    def test_exec_kcore_standalone(self, algo):
        pass

    TRIANGLEEMBEDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/triangle_embed ./testdb",
        "result": ['''"discovered_triangles":1612010''']
    }

    @pytest.mark.parametrize("importor", [IMPORTOPT], indirect=True)
    @pytest.mark.parametrize("algo", [TRIANGLEEMBEDOPT], indirect=True)
    def test_exec_triangle_embed(self, importor, algo):
        pass

    TRIANGLESTANDOPT = {
        "cmd": "OMP_NUM_THREADS=6 algo/triangle_standalone --type text --input_dir ./data/algo/fb_weighted --make_symmetric 1",
        "result": ["discovered 1612010 triangles"]
    }

    @pytest.mark.parametrize("algo", [TRIANGLESTANDOPT], indirect=True)
    def test_exec_triangle_standalone(self, algo):
        pass
